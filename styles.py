
import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        /* Global Background & Font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');
        
        html, body, [class*="css"]  {
            font-family: 'Inter', sans-serif;
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            letter-spacing: -0.02em;
        }
        
        /* Dark Theme Adjustments - Deep Space Blue */
        .stApp {
            background-color: #0d1117; 
        }
        
        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: #161b22;
            border-right: 1px solid #30363d;
        }

        div[data-testid="stSidebarNav"] {
            padding-top: 1rem;
        }
        
        /* Custom Cards for Metrics */
        .metric-card {
            background: linear-gradient(145deg, #1f242d, #161b22);
            border: 1px solid #30363d;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }
        
        .metric-card:hover {
            border-color: #58a6ff;
            transform: translateY(-2px);
        }
        
        .metric-card h4 {
            color: #8b949e;
            font-size: 0.75rem;
            text-transform: uppercase;
            font-weight: 600;
            letter-spacing: 0.1em;
            margin-bottom: 0.5rem;
        }
        
        .metric-card p {
            color: #f0f6fc;
            font-size: 1.25rem;
            font-weight: 600;
            margin: 0;
            line-height: 1.4;
        }

        /* Highlight Box for Summaries */
        .highlight-box {
            background-color: #161b22;
            border-left: 4px solid #58a6ff;
            padding: 1.5rem;
            border-radius: 0 8px 8px 0;
            margin: 1rem 0;
            font-size: 1.05rem;
            line-height: 1.6;
            color: #c9d1d9;
        }

        /* Alert Boxes */
        .red-flag {
            background-color: rgba(248, 81, 73, 0.1);
            border: 1px solid rgba(248, 81, 73, 0.4);
            border-left: 4px solid #f85149;
            padding: 1rem;
            border-radius: 6px;
            margin-bottom: 0.75rem;
            color: #ffdfdc;
            font-size: 0.95rem;
        }
        
        .alpha-driver {
            background-color: rgba(63, 185, 80, 0.1);
            border: 1px solid rgba(63, 185, 80, 0.4);
            border-left: 4px solid #3fb950;
            padding: 1rem;
            border-radius: 6px;
            margin-bottom: 0.75rem;
            color: #dcfce7;
            font-size: 0.95rem;
        }

        /* Verdict Badge */
        .verdict-container {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 2rem 0;
        }

        .verdict-badge {
            font-size: 3rem;
            font-weight: 800;
            letter-spacing: 0.1em;
            padding: 0.5rem 2rem;
            border-radius: 12px;
            text-transform: uppercase;
            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
            border: 2px solid currentColor;
        }

        .verdict-buy { 
            color: #3fb950; 
            background: rgba(63, 185, 80, 0.15);
            box-shadow: 0 0 20px rgba(63, 185, 80, 0.2);
        }
        
        .verdict-sell { 
            color: #f85149; 
            background: rgba(248, 81, 73, 0.15);
            box-shadow: 0 0 20px rgba(248, 81, 73, 0.2);
        }
        
        .verdict-watch { 
            color: #e3b341; 
            background: rgba(227, 179, 65, 0.15);
            box-shadow: 0 0 20px rgba(227, 179, 65, 0.2);
        }

        /* Tabs Styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2rem;
            border-bottom: 1px solid #30363d;
        }

        .stTabs [data-baseweb="tab"] {
            height: 3rem;
            white-space: pre-wrap;
            background-color: transparent;
            border-radius: 6px 6px 0 0;
            color: #8b949e;
            font-weight: 500;
            padding: 0 1rem;
        }

        .stTabs [data-baseweb="tab"]:hover {
            color: #58a6ff;
            background-color: rgba(255,255,255,0.02);
        }

        .stTabs [aria-selected="true"] {
            color: #58a6ff;
            border-bottom: 2px solid #58a6ff;
        }
        
        /* JSON Viewer */
        .stJson {
            background-color: #0d1117;
            border-radius: 8px;
            padding: 1rem;
            border: 1px solid #30363d;
        }

    </style>
    """, unsafe_allow_html=True)
