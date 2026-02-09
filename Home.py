"""
News Analytics Platform - Home Page
Entry point with 5 specialized dashboard pages.
"""

import streamlit as st

st.set_page_config(
    page_title="News Analytics Platform",
    page_icon="NA",
    layout="wide"
)

st.title("South Sudan News Analytics Platform")

st.markdown("""
Welcome to the unified News Analytics Platform for monitoring and analyzing news coverage in South Sudan.

---

### Dashboard Pages

Use the **sidebar** to navigate between the following views:

| Page | Description |
|------|-------------|
| **Dataset Overview** | High-level view of article volume, labels, and regional distribution |
| **ADM1 Insights** | State-level alert/alarm detection based on article volume anomalies |
| **ADM2 Insights** | County-level alert/alarm detection for granular monitoring |
| **Article Browser** | Search and read individual articles with full metadata |
| **RAG+LLM Summary** | AI-powered situation summaries using GPT models |

---

### Alert/Alarm System

The platform uses statistical anomaly detection to flag unusual patterns:

| Status | Meaning | Visual |
|--------|---------|--------|
| **Normal** | Within 1 standard deviation of historical mean | Gray |
| **Alert-high** | 1-2 standard deviations above mean | Orange |
| **Alarm-high** | More than 2 standard deviations above mean | Red |

---

### Configuration

- **Data Source**: `data/processed/all_clean_df.csv`
- **API Key**: Set `OPENAI_API_KEY` in `.env` for RAG+LLM features

---
*Built for humanitarian and food security analysts.*
""")
