# 🦅 Sentinel Analyst
> **Financial Superintelligence Platform**

Sentinel is a production-grade Streamlit prototype designed to function as an autonomous financial analyst. It ingests complex financial documents (SEC filings, earnings transcripts) and uses large language models (LLMs) to extract proprietary insights, risk factors, and investment verdicts.

![Interface Preview](https://via.placeholder.com/800x400?text=Sentinel+Analyst+Interface)

## ✨ Features
- **Instant Strategic Summaries**: Cuts through the noise to find the core business narrative.
- **Red Flag Detection**: Identifies subtle risks, management obfuscation, and liability concerns.
- **Alpha Extraction**: Pinpoints unique growth drivers and competitive moats.
- **Analyst Verdict**: Generates a strictly data-driven BUY/WATCH/SELL rating.
- **Modern Fintech UI**: Dark-themed, distraction-free interface built for professionals.

## 🚀 Installation

### Prerequisites
- Python 3.9 or higher
- An OpenAI API Key (Optional, for live data. Demo mode included.)

### Setup
1. **Clone the repository** (if applicable) or download the source.
2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Usage

1. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
2. **Access the Dashboard**:
   The app will open in your browser at `http://localhost:8501`.
3. **Analyze**:
   - Enter your OpenAI API Key in the sidebar (or leave blank to try the **Demo Mode** with mock data).
   - Upload a PDF (e.g., Apple's 10-K).
   - Watch Sentinel parse and analyze the document in real-time.

## 📂 Project Structure
```
sentinel_analyst/
├── app.py              # Main Dashboard UI & Styling
├── analysis.py         # AI Logic & Prompt Engineering
├── utils.py            # PDF Processing Utilities
├── requirements.txt    # Python Dependencies
├── sample_data/        # Place your test PDFs here
└── README.md           # This file
```

## 🛡️ Technical Details
- **Frontend**: Streamlit with custom CSS injection for the "Fintech Terminal" aesthetic.
- **Parsing**: `pypdf` for robust text extraction.
- **Caching**: `@st.cache_data` ensures instant reloading of analyzed files.
- **Architecture**: Modular separation of concerns (UI vs. Logic vs. Utils).

---
*Created by Antigravity.*
