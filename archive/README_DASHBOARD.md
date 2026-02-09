# News Analytics Platform - Streamlit Dashboard

A comprehensive Streamlit dashboard for analyzing South Sudan news articles with sentiment analysis, geographic filtering, alert/alarm detection, and RAG+LLM capabilities.

## Features

- **📊 Sentiment Analysis**: Track sentiment scores over time with statistical alerts and alarms
- **🗺️ Geographic Filtering**: Filter by ADM1 regions and ADM2 counties
- **🔍 Keyword Search**: Search articles by keywords with OR logic support
- **📈 Visualizations**: Interactive time series, heatmaps, and bar charts
- **🚨 Alert System**: Automatic detection of anomalies using standard deviation thresholds
- **🤖 RAG+LLM**: Generate AI-powered situation summaries using OpenAI

## Quick Start

### 1. Prerequisites

- Python 3.8 or higher
- OpenAI API key (for RAG+LLM features)
- Processed news data CSV file

### 2. Installation

```bash
# Install dashboard dependencies
pip install -r requirements-dashboard.txt

# Download NLTK data (required for text processing)
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('punkt_tab')"
```

### 3. Configuration

Create a `.env` file in the project root:

```bash
# Copy the example file
copy .env.example .env
```

Edit `.env` and add your configuration:

```env
# Required: Your OpenAI API key
OPENAI_API_KEY=sk-your-actual-openai-api-key-here

# Required: Path to your processed CSV file
DATA_PATH=data/processed/all_clean_df.csv
```

### 4. Data Preparation

Place your processed news data CSV file at the path specified in `DATA_PATH`. The CSV should contain these columns:

**Required columns:**
- `date` - Article publication date
- `title` - Article title
- `paragraphs` - Original article text
- `paragraphs_cleaned` - Cleaned article text
- `sentiment_score` - Sentiment score (0-1)
- `sentiment_label` - Sentiment category
- `adm1_name_final` - ADM1 region name
- `adm2_name_final` - ADM2 county name
- `Label` - Article category label

**Optional columns:**
- `url` - Article URL
- `retrieve_source` - Data source
- `summary_text` - Article summary (for RAG)

### 5. Run the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your default browser at `http://localhost:8501`

## Dashboard Sections

### 1. **Filters (Sidebar)**
- Date range selection
- Keyword search (supports OR logic: `keyword1 OR keyword2`)
- Source filtering
- Geographic filters (ADM1 regions, ADM2 counties)
- Content filters (article labels, sentiment types)
- Heatmap controls

### 2. **Time Series Charts**
- **Sentiment Score Over Time**: Track average sentiment with alert/alarm detection
- **Article Count Over Time**: Monitor article volume with anomaly detection
- **Heatmap**: Regional alerts and alarms by month

**Alert System:**
- 🟢 **Normal**: Within 1 standard deviation
- 🟠 **Alert**: Beyond 1 SD (high or low)
- 🔴 **Alarm**: Beyond 2 SD (high or low)

### 3. **Geographic Analysis**
- Average sentiment by ADM1 region
- Article count by ADM2 county

### 4. **Article Browser**
- Browse individual articles
- View original and cleaned text
- See metadata (date, source, location, sentiment)

### 5. **RAG+LLM Situation Summary**
Generate AI-powered summaries of filtered articles:
- Select location level (ADM1 or ADM2)
- Choose retrieval method (keyword or TF-IDF)
- Set time range and focus location
- Enter focus keyword/topic
- Generate summary with source citations

## Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `OPENAI_API_KEY` | OpenAI API key for LLM features | Yes (for RAG) | - |
| `DATA_PATH` | Path to processed CSV file | Yes | `data/processed/all_clean_df.csv` |

## Troubleshooting

### Data File Not Found

**Error:** `❌ Data file not found at: data/processed/all_clean_df.csv`

**Solution:**
1. Ensure your CSV file is placed at the correct path
2. Update `DATA_PATH` in `.env` if using a different location
3. Check file permissions

### OpenAI API Error

**Error:** `Missing OPENAI_API_KEY`

**Solution:**
1. Create a `.env` file in the project root
2. Add your OpenAI API key: `OPENAI_API_KEY=sk-...`
3. Restart the Streamlit app

### NLTK Data Missing

**Error:** `Resource punkt not found`

**Solution:**
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
```

### TF-IDF Retrieval Not Working

**Error:** Falls back to keyword retrieval

**Solution:**
```bash
pip install scikit-learn
```

## Data Directory Structure

```
news-analytics-platform/
├── data/
│   ├── raw/              # Original data
│   ├── interim/          # Intermediate processing
│   └── processed/        # Final processed CSV (place your file here)
│       └── all_clean_df.csv
├── app.py                # Streamlit dashboard
├── .env                  # Your configuration (not in git)
├── .env.example          # Configuration template
└── requirements-dashboard.txt
```

## Tips for Best Results

1. **Data Quality**: Ensure your CSV has clean date formats and valid sentiment scores
2. **API Costs**: RAG+LLM features use OpenAI API (costs apply per request)
3. **Performance**: For large datasets (>100k articles), consider filtering by date first
4. **Retrieval Method**: TF-IDF is more accurate but requires scikit-learn; keyword is faster
5. **Top K Articles**: Start with 10-15 articles for summaries to balance quality and cost

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify your `.env` configuration
3. Ensure all dependencies are installed
4. Check that your CSV file has the required columns

## License

This dashboard is part of the News Analytics Platform project.
