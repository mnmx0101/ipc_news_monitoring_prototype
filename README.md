# News Analytics Platform - Deployment Guide

## Quick Start (Local Development)

### Prerequisites
- Anaconda/Miniconda installed
- OpenAI API key

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/news-analytics-platform.git
   cd news-analytics-platform
   ```

2. **Create conda environment**
   ```bash
   conda create -n crisis-dashboard python=3.9 -y
   conda activate crisis-dashboard
   pip install -r requirements.txt
   ```

3. **Configure secrets**
   ```bash
   # Copy the example secrets file
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml
   
   # Edit .streamlit/secrets.toml and add your OpenAI API key
   ```

4. **Run the dashboard**
   ```bash
   streamlit run Home.py
   ```

   The app will open at http://localhost:8501

---

## Deployment to Streamlit Cloud

### Step 1: Prepare Repository

✅ **Already done!** This repository is configured for deployment:
- Data optimized (Parquet format: 90 MB instead of 1.8 GB CSV)
- Sensitive files excluded (`.env`, secrets)
- Requirements specified

### Step 2: Deploy

1. **Push to GitHub** (if not already done)
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Go to Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub account

3. **Configure deployment**
   - **Repository**: `YOUR-USERNAME/news-analytics-platform`
   - **Branch**: `main`
   - **Main file**: `Home.py`

4. **Add secrets**
   - Click "Advanced settings"
   - In "Secrets" section, add:
     ```toml
     OPENAI_API_KEY = "sk-your-actual-key-here"
     ```

5. **Deploy!**
   - Click "Deploy"
   - Wait 2-5 minutes
   - Your app will be live at `https://your-app-name.streamlit.app`

---

## Features

- **Dataset Overview**: High-level statistics and trends
- **ADM1 Insights**: State-level anomaly detection
- **ADM2 Insights**: County-level monitoring
- **Article Browser**: Search and read articles
- **RAG+LLM Summary**: AI-powered situation reports

---

## Data

The dashboard uses `data/processed/all_clean_df.parquet` (90 MB):
- **Format**: Parquet (optimized for deployment)
- **Size**: 95% smaller than original CSV
- **Performance**: 5.8x faster loading
- **Records**: 167,588 articles

---

## Configuration

### Environment Variables

Create `.streamlit/secrets.toml` for local development:

```toml
OPENAI_API_KEY = "sk-your-key-here"
```

For Streamlit Cloud, add secrets in the app settings.

---

## Troubleshooting

### "OpenAI API key missing"
- Check `.streamlit/secrets.toml` exists locally
- For Streamlit Cloud, verify secrets are configured in app settings

### "Data file not found"
- Ensure `data/processed/all_clean_df.parquet` exists
- If you only have CSV, run: `python scripts/convert_to_parquet.py`

### App is slow
- Verify you're using Parquet format (not CSV)
- Check Streamlit Cloud resource limits
- Consider upgrading to paid tier for better performance

---

## Project Structure

```
news-analytics-platform/
├── Home.py                 # Main entry point
├── pages/                  # Dashboard pages
│   ├── 1_Dataset_Overview.py
│   ├── 2_ADM1_Insights.py
│   ├── 3_ADM2_Insights.py
│   ├── 4_Article_Browser.py
│   └── 5_RAG_LLM_Summary.py
├── utils/                  # Shared utilities
│   ├── data_loader.py
│   ├── filters.py
│   └── alert_helpers.py
├── data/
│   └── processed/
│       └── all_clean_df.parquet  # Optimized data
├── scripts/
│   └── convert_to_parquet.py     # CSV to Parquet converter
├── requirements.txt        # Python dependencies
└── .streamlit/
    └── secrets.toml.example      # Secrets template
```

---

## Support

For issues or questions:
- Check the [deployment checklist](deployment_checklist.md)
- Review [Streamlit documentation](https://docs.streamlit.io)
- See [USER_GUIDE.md](USER_GUIDE.md) for feature details

---

## License

[Add your license here]

---

**Built for humanitarian and food security analysts**
