---
title: South Sudan News Analytics Platform
emoji: 📰
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: "1.40.1"
app_file: Home.py
pinned: false
---

# South Sudan News Analytics Platform

A comprehensive dashboard for monitoring and analyzing news coverage in South Sudan, featuring:

- **Dataset Overview**: Article volume, labels, and regional distribution
- **ADM1 Insights**: State-level alert/alarm detection
- **ADM2 Insights**: County-level monitoring
- **Article Browser**: Search and read individual articles
- **RAG+LLM Summary**: AI-powered situation summaries

## Features

- 📊 Statistical anomaly detection for crisis monitoring
- 🗺️ Multi-level geographic analysis (ADM1/ADM2)
- 🔍 Advanced article search and filtering
- 🤖 GPT-powered summaries with RAG retrieval
- 📈 Interactive visualizations with Altair

## Data

The dashboard uses a 90 MB Parquet dataset hosted on GitHub Releases. Data is automatically downloaded on first run and cached for subsequent loads.

## Configuration

### Required Secrets

Set the following secret in your Hugging Face Space settings:

```
OPENAI_API_KEY = "sk-your-openai-api-key-here"
```

### Optional Configuration

- `DATA_URL`: URL to external data file (default: GitHub Releases)

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit secrets.toml with your API key

# Run the app
streamlit run Home.py
```

## Technical Details

- **Framework**: Streamlit 1.40.1
- **Data Format**: Parquet (optimized for performance)
- **External Storage**: GitHub Releases
- **AI Model**: OpenAI GPT-3.5-turbo (legacy API)
- **Visualization**: Altair charts

## License

Built for humanitarian and food security analysts.

## Contact

For questions or issues, please contact the repository maintainer.
