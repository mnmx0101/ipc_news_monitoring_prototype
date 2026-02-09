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

DATA_PATH = os.getenv("DATA_PATH", "data/processed/all_clean_df.csv")

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
    """Load and preprocess the news dataset."""
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        st.error(f"❌ Data file not found at: `{data_path}`")
        return pd.DataFrame(columns=CORE_COLUMNS)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame(columns=CORE_COLUMNS)

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
