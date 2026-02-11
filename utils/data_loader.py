"""
Shared data loading utilities for the News Analytics Platform.
"""

import os
import streamlit as st
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

CORE_COLUMNS = [
    "date", "title", "paragraphs", "paragraphs_cleaned", "url",
    "retrieve_source", "yearmon", "year_quarter",
    "adm1_name_final", "adm2_name_final", "Label",
    "sentiment_label", "sentiment_score"
]

# Auto-detect data format (prefer Parquet for deployment)
DEFAULT_CSV_PATH = "data/processed/all_clean_df.csv"
DEFAULT_PARQUET_PATH = "data/processed/all_clean_df.parquet"

# External data URL (GitHub Releases)
DATA_URL = "https://github.com/mnmx0101/ipc_news_monitoring_prototype/releases/download/v1.0-data/all_clean_df.parquet"

# Check which file exists (prefer Parquet)
if Path(DEFAULT_PARQUET_PATH).exists():
    DATA_PATH = os.getenv("DATA_PATH", DEFAULT_PARQUET_PATH)
else:
    DATA_PATH = os.getenv("DATA_PATH", DEFAULT_CSV_PATH)

# Keyword taxonomy for article labeling
CATEGORIES = {
    "Conflict and Violence": [
        "conflict","war","fighting","battle","violence","clash","attack","military","armed","rebel","soldier","security",
        "bomb","shell","shooting","insurgent","terror","terrorism","casualty","hostage","airstrike"
    ],
    "Political Instability": [
        "political","government","protest","demonstration","election","coup","instability","corruption","parliament",
        "opposition","governance","policy","minister","president","cabinet","regime","referendum"
    ],
    "Economic Issues": [
        "price","inflation","economy","economic","market","trade","currency","poverty","unemployment","growth","debt",
        "finance","livelihood","wage","budget","gdp","cost","commodity","imports","exports"
    ],
    "Weather Conditions": [
        "drought","rain","rainfall","storm","cyclone","hurricane","typhoon","flood","flooding","weather","climate",
        "temperature","heatwave","monsoon"
    ],
    "Production Shortage": [
        "harvest","production","yield","crop","crops","planting","farming","agriculture","livestock","pasture","supply",
        "shortage","output","seed","fertilizer"
    ],
    "Humanitarian Aid": [
        "aid","relief","assistance","humanitarian","donor","funding","wfp","unhcr","unicef","ngo","distribution","support",
        "msf","red cross","icrc"
    ],
    "Food Crisis": [
        "food","famine","hunger","nutrition","malnutrition","insecurity","ipc","starvation","hungry"
    ],
    "Land-related issues": [
        "land","tenure","dispute","boundary","eviction","pastoralist","grazing","farmland","property","encroachment"
    ],
    "Forced Displacements": [
        "displacement","displaced","refugee","refugees","idp","idps","migrant","migration","camp","camps","asylum",
        "relocation","returnee","returnees"
    ],
    "Pests and Diseases": [
        "locust","pest","pests","disease","diseases","outbreak","cholera","malaria","ebola","measles","covid","virus",
        "infection","armyworm","pandemic"
    ],
    "Environment Issues": [
        "environment","environmental","deforestation","erosion","pollution","biodiversity","conservation","desertification",
        "degradation","wildfire","climate","greenhouse"
    ]
}


@st.cache_data
def load_data(data_path=DATA_PATH):
    """Load and preprocess the news dataset.
    
    Supports both CSV and Parquet formats. Parquet is preferred for deployment
    due to smaller file size and faster loading.
    """
    
    try:
        # Auto-detect format based on file extension
        data_path_str = str(data_path)
        if data_path_str.endswith('.parquet'):
            df = pd.read_parquet(data_path)
        elif data_path_str.endswith('.csv'):
            df = pd.read_csv(data_path, low_memory=False)
        else:
            # Try Parquet first, then CSV
            try:
                df = pd.read_parquet(data_path)
            except:
                df = pd.read_csv(data_path, low_memory=False)
    except FileNotFoundError:
        st.error(f"❌ Data file not found at: `{data_path}`")
        st.info("💡 Tip: If deploying, convert CSV to Parquet using `python scripts/convert_to_parquet.py`")
        st.stop()  # Stop execution to show error clearly
    except Exception as e:
        st.error(f"❌ Error loading data from `{data_path}`")
        st.error(f"**Error type**: {type(e).__name__}")
        st.error(f"**Error message**: {str(e)}")
        import traceback
        st.code(traceback.format_exc())
        st.stop()  # Stop execution to show error clearly

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["adm1_name_final"] = df["adm1_name_final"].fillna("Unknown Region")
    df["adm2_name_final"] = df["adm2_name_final"].fillna("Unknown County")
    df["Label"] = df["Label"].fillna("Uncategorized")
    df["yearmon"] = df["date"].dt.to_period("M").astype(str)
    df["sentiment_score"] = pd.to_numeric(df["sentiment_score"], errors="coerce")
    df = df.dropna(subset=["date", "sentiment_score"])
    
    return df


def get_taxonomy_table():
    """Return taxonomy as a DataFrame for display."""
    rows = []
    for cat, kws in CATEGORIES.items():
        rows.append({"Category": cat, "Keywords": ", ".join(kws)})
    return pd.DataFrame(rows)
