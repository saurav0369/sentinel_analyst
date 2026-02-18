import streamlit as st
import pandas as pd
from utils import extract_text_from_pdf, truncate_text
from analysis import SentinelAnalyst
import time

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
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
# IMPORTS & STYLES
# -----------------------------------------------------------------------------
from styles import apply_custom_styles
apply_custom_styles()

# -----------------------------------------------------------------------------
# SIDEBAR
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## 🦅 Sentinel")
    st.caption("Financial Superintelligence (Local)")
    
    st.markdown("### 🤖 Engine Configuration")
    with st.container():
        model_name = st.selectbox(
            "AI Model", 
            ["llama3", "mistral-nemo", "gemma:7b", "phi3"], 
            index=0,
            help="Select the local Ollama model to power the analyst."
        )
        st.info("Ensure Ollama is running: `ollama serve`")
    
    st.markdown("### 📄 Input Data")
    uploaded_file = st.file_uploader("Upload Financial Doc (PDF)", type=["pdf"])
    
    st.markdown("### ⚙️ Analysis Parameters")
    analysis_depth = st.select_slider(
        "Depth", 
        options=["Quick Scan", "Deep Dive", "Forensic Mode"], 
        value="Deep Dive"
    )
    
    st.markdown("---")
    st.caption("🔒 **Security Note**: Data is processed locally on your machine. No external API calls.")

# -----------------------------------------------------------------------------
# MAIN LOGIC
# -----------------------------------------------------------------------------

# Cache the analysis to avoid re-running on interactions
@st.cache_data(show_spinner=False)
def analyze_pdf(file_bytes, model):
    # Setup Analyst
    try:
        analyst = SentinelAnalyst(model_name=model)
        
        # 1. Extract Text
        text_content = extract_text_from_pdf(io.BytesIO(file_bytes))
        if not text_content:
            return {"error": "Failed to extract text from PDF. The file might be empty or encrypted."}
        
        # 2. Analyze
        return analyst.analyze_document(text_content)
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

if not uploaded_file:
    # LANDING STATE
    st.markdown("""
    <div style="text-align: center; margin-top: 3rem;">
        <h1>🔍 Market Intelligence Terminal</h1>
        <p style="font-size: 1.2rem; color: #8b949e;">Autonomous Financial Analysis Powered by Local LLMs</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_spacer_l, col_content, col_spacer_r = st.columns([1, 2, 1])
    with col_content:
        st.markdown("### Ready to Analyze")
        st.markdown("""
        Upload an **SEC 10-K**, **Earnings Transcript**, or **Equity Research Report**.
        
        Sentinel will extract:
        - 🚩 **Hidden Risks & Red Flags** that management might act to obscure.
        - 🚀 **Organic Growth Drivers** and competitive advantages.
        - ⚖️ **Institutional Buy/Sell Verdicts** based on sentiment and facts.
        """)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Metrics Row
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="metric-card"><h4>System Status</h4><p>🟢 Online / Local</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="metric-card"><h4>Active Engine</h4><p>{model_name}</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="metric-card"><h4>Privacy Level</h4><p>Air-Gapped</p></div>', unsafe_allow_html=True)

else:
    # ANALYZING STATE
    import io
    
    with st.spinner(f"🦅 Sentinel is extracting intelligence using {model_name}..."):
        # We pass file_bytes to be cacheable
        bytes_data = uploaded_file.getvalue()
        results = analyze_pdf(bytes_data, model_name)
        
    if "error" in results:
        st.error(results["error"])
    else:
        # ---------------------------------------------------------------------
        # DASHBOARD
        # ---------------------------------------------------------------------
        st.markdown(f"## 📄 Intel: `{uploaded_file.name}`")
        
        # TABS INTERFACE
        tab_summary, tab_details, tab_raw = st.tabs(["📋 Executive Summary", "🔍 Deep Dive Analysis", "💾 Raw Data"])
        
        # --- TAB 1: EXECUTIVE SUMMARY ---
        with tab_summary:
            # Verdict Section
            verdict = results.get("verdict", "WATCH").upper()
            v_class = "verdict-watch"
            if "BUY" in verdict: v_class = "verdict-buy"
            elif "SELL" in verdict: v_class = "verdict-sell"
            
            st.markdown(f"""
            <div class="verdict-container">
                <div class="verdict-badge {v_class}">{verdict}</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"### 💡 Analyst Thesis")
            st.markdown(f"""
            <div class="highlight-box">
                {results.get("verdict_reasoning", "No specific reasoning provided.")}
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### 🗝️ Key Strategic Takeaways")
            st.markdown(f"""
            <div class="metric-card" style="border-left: 4px solid #8b949e;">
                <p style="font-size: 1rem; font-weight: 400;">{results.get('strategic_summary', 'Summary not available.')}</p>
            </div>
            """, unsafe_allow_html=True)

        # --- TAB 2: DEEP DIVE ---
        with tab_details:
            col_alpha, col_risk = st.columns(2)
            
            with col_alpha:
                st.subheader("🚀 Alpha Drivers (Growth Potentials)")
                drivers = results.get("alpha_drivers", [])
                if drivers:
                    for alpha in drivers:
                        st.markdown(f'<div class="alpha-driver">✦ {alpha}</div>', unsafe_allow_html=True)
                else:
                    st.info("No specific growth drivers detected.")
                    
            with col_risk:
                st.subheader("🚩 Red Flags (Risk Factors)")
                flags = results.get("red_flags", [])
                if flags:
                    for flag in flags:
                        st.markdown(f'<div class="red-flag">⚠ {flag}</div>', unsafe_allow_html=True)
                else:
                    st.success("No major red flags detected.")

        # --- TAB 3: RAW DATA ---
        with tab_raw:
            st.caption("Full JSON Output from LLM")
            st.json(results)
