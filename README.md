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
- **[Ollama](https://ollama.com/)** installed and running.
- A model pulled (e.g., `ollama pull llama3`).

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

1. **Start Ollama**:
   Ensure your local LLM server is running:
   ```bash
   ollama serve
   ```
   *Make sure you have pulled a model like `ollama pull llama3`.*

2. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
3. **Analyze**:
   - Select your local model in the sidebar.
   - Upload a PDF.
   - Sentinel will analyze it completely offline.

## 📂 Project Structure
```
sentinel_analyst/
├── app.py              # Main Dashboard UI & Styling
├── analysis.py         # AI Logic (Ollama Integration)
├── utils.py            # PDF Processing Utilities
├── requirements.txt    # Python Dependencies
├── sample_data/        # Place your test PDFs here
└── README.md           # This file
```

## 🛡️ Technical Details
- **Frontend**: Streamlit with custom CSS.
- **Backend (AI)**: **Ollama** (Local Inference) - No API keys required.
- **Parsing**: `pypdf` for robust text extraction.
- **Privacy**: Zero data leaves your machine.

---
*Created by Antigravity.*
