import streamlit as st
import pandas as pd
from utils import extract_text_from_pdf, truncate_text
from analysis import SentinelAnalyst
import time

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Sentinel Analyst | Financial Superintelligence",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# CUSTOM CSS (THEME)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    /* Global Background & Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }
    
    /* Dark Theme Adjustments */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #161B22;
        border-right: 1px solid #282C34;
    }
    
    /* Headings */
    h1, h2, h3 {
        color: #F8F9FA;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    
    h1 { margin-bottom: 2rem; }
    
    /* Custom Cards for Metrics */
    div.metric-card {
        background-color: #1F242D;
        border: 1px solid #2D333B;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    
    div.metric-card:hover {
        border-color: #58A6FF;
    }
    
    div.metric-card h4 {
        color: #8B949E;
        font-size: 0.85rem;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
        letter-spacing: 1px;
    }
    
    div.metric-card p {
        color: #E6EDF3;
        font-size: 1.1rem;
        margin: 0;
        line-height: 1.5;
    }
    
    /* Alert Boxes */
    .red-flag {
        background-color: rgba(248, 81, 73, 0.1);
        border-left: 4px solid #F85149;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 10px;
        color: #FFCACA;
    }
    
    .alpha-driver {
        background-color: rgba(46, 160, 67, 0.1);
        border-left: 4px solid #3FB950;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 10px;
        color: #C3E88D;
    }

    /* Verdict Badge */
    .verdict-box {
        text-align: center;
        padding: 1rem;
        border-radius: 8px;
        font-weight: 800;
        font-size: 2rem;
        letter-spacing: 2px;
    }
    .verdict-buy { background: rgba(57, 211, 83, 0.2); color: #39D353; border: 1px solid #39D353; }
    .verdict-sell { background: rgba(248, 81, 73, 0.2); color: #F85149; border: 1px solid #F85149; }
    .verdict-watch { background: rgba(235, 172, 0, 0.2); color: #FFD33D; border: 1px solid #FFD33D; }

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SIDEBAR
# -----------------------------------------------------------------------------
with st.sidebar:
    st.title("🦅 Sentinel")
    st.caption("Financial Superintelligence (Local)")
    st.markdown("---")
    
    st.markdown("### 🤖 Local Engine")
    model_name = st.selectbox("Select Model", ["llama3", "mistral", "gemma:7b", "phi3"], index=0)
    st.caption("Ensure Ollama is running (`ollama serve`)")
    
    uploaded_file = st.file_uploader("Upload Financial Document", type=["pdf"])
    
    st.markdown("### ⚙️ Settings")
    analysis_depth = st.select_slider("Analysis Depth", options=["Quick Scan", "Deep Dive", "Forensic"], value="Deep Dive")
    
    st.markdown("---")
    st.info("🔒 Data is processed LOCALLY. No external APIs.")

# -----------------------------------------------------------------------------
# MAIN LOGIC
# -----------------------------------------------------------------------------

# Cache the analysis to avoid re-running on interactions
@st.cache_data(show_spinner=False)
def analyze_pdf(file_bytes, model):
    # Setup Analyst
    analyst = SentinelAnalyst(model_name=model)
    
    # 1. Extract Text
    text_content = extract_text_from_pdf(io.BytesIO(file_bytes))
    if not text_content:
        return {"error": "Failed to extract text from PDF."}
    
    # 2. Analyze
    return analyst.analyze_document(text_content)

if not uploaded_file:
    # LANDING STATE
    st.markdown("# 🔍 Market Intelligence Terminal")
    st.markdown("""
    ### Ready to Analyze (Independent Mode)
    Upload an **SEC 10-K**, **Earnings Transcript**, or **Research Report**.
    
    *Sentinel uses YOUR local LLM to extract:*
    - 🚩 Hidden Risks & Red Flags
    - 🚀 Alpha & Growth Drivers
    - ⚖️ Institutional Buy/Sell Verdicts
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card"><h4>System Status</h4><p>🟢 Offline/Local</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><h4>Model Engine</h4><p>{model_name}</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h4>Privacy</h4><p>Air-Gapped</p></div>', unsafe_allow_html=True)

else:
    # ANALYZING STATE
    import io
    
    st.markdown(f"## 📄 Analyzing: `{uploaded_file.name}`")
    
    with st.spinner(f"extracting intelligence using {model_name}..."):
        # We pass file_bytes to be cacheable (file objects aren't always hashable well)
        bytes_data = uploaded_file.getvalue()
        results = analyze_pdf(bytes_data, model_name)
        
    if "error" in results:
        st.error(results["error"])
    else:
        # ---------------------------------------------------------------------
        # DASHBOARD
        # ---------------------------------------------------------------------
        
        # 1. VERDICT SECTION
        verdict = results.get("verdict", "WATCH").upper()
        v_class = "verdict-watch"
        if verdict == "BUY": v_class = "verdict-buy"
        if verdict == "SELL": v_class = "verdict-sell"
        
        col_v1, col_v2 = st.columns([1, 3])
        with col_v1:
            st.markdown(f'<div class="verdict-box {v_class}">{verdict}</div>', unsafe_allow_html=True)
        with col_v2:
             st.markdown(f"### Analyst Thesis")
             st.info(results.get("verdict_reasoning", "No reasoning provided."))

        st.markdown("---")

        # 2. STRATEGIC SUMMARY
        st.subheader("📋 Strategic Executive Summary")
        st.markdown(f"""
        <div class="metric-card">
            <p>{results.get('strategic_summary', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

        # 3. ALPHA VS RED FLAGS
        col_alpha, col_risk = st.columns(2)
        
        with col_alpha:
            st.subheader("🚀 Alpha Drivers (Growth)")
            for alpha in results.get("alpha_drivers", []):
                st.markdown(f'<div class="alpha-driver">✦ {alpha}</div>', unsafe_allow_html=True)
                
        with col_risk:
            st.subheader("🚩 Red Flags (Risk)")
            for flag in results.get("red_flags", []):
                st.markdown(f'<div class="red-flag">⚠ {flag}</div>', unsafe_allow_html=True)

        # 4. RAW DATA INSPECTION (Optional)
        with st.expander("Show Raw Analysis JSON"):
            st.json(results)
