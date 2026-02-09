"""
Page 2: ADM1 Insights (Subnational Level 1)
Static + Dynamic alert/alarm heatmaps per Article Label.
"""

import streamlit as st
import pandas as pd
import altair as alt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.data_loader import load_data
from utils.filters import (
    render_source_filter, render_date_filter, render_sentiment_filter,
    apply_filters, render_summary_metrics
)
from utils.alert_helpers import make_heatmap_pair, render_alert_legend

st.set_page_config(page_title="ADM1 Insights", layout="wide")

st.title("ADM1 Insights (State Level)")
st.markdown("Alert/alarm detection at Admin Level 1, with **static** (full-span) and **dynamic** (12-month rolling) thresholds shown side by side for each Article Label.")

# Load data
df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
sources = render_source_filter(df, "p2", default=["radiotamazuj"])
sentiments = render_sentiment_filter(df, "p2", default=["Negative"])
date_range = render_date_filter(df, "p2")

# Apply filters (no label filter -- iterate over all labels)
filtered_df = apply_filters(
    df, sources=sources, date_range=date_range, sentiments=sentiments
)

# Summary metrics
render_summary_metrics(filtered_df)

st.markdown("---")
render_alert_legend()

# Top N regions
top_n = st.slider("Top N Regions to Display", 5, 20, 10, key="p2_topn")

if filtered_df.empty:
    st.warning("No articles match the current filters.")
else:
    all_labels = sorted([l for l in filtered_df["Label"].dropna().unique() if l != "Uncategorized"])
    
    region_totals = filtered_df["adm1_name_final"].value_counts()
    top_regions = region_totals.head(top_n).index.tolist()
    
    for label_name in all_labels:
        st.subheader(f"{label_name}")
        
        label_df = filtered_df[filtered_df["Label"] == label_name]
        
        if label_df.empty:
            st.info(f"No articles for label '{label_name}' with current filters.")
            continue
        
        ts_adm1 = label_df.groupby(["adm1_name_final", "yearmon"]).size().reset_index(name="article_count")
        ts_adm1["yearmon_date"] = pd.to_datetime(ts_adm1["yearmon"])
        ts_adm1 = ts_adm1[ts_adm1["adm1_name_final"].isin(top_regions)]
        
        if ts_adm1.empty:
            st.info(f"No data to display for '{label_name}' in top regions.")
            continue
        
        static_chart, dynamic_chart = make_heatmap_pair(
            ts_adm1, "adm1_name_final", "article_count", label_name, top_regions,
            height=max(250, top_n * 22)
        )
        
        col_left, col_right = st.columns(2)
        
        with col_left:
            st.altair_chart(static_chart, use_container_width=True)
        
        with col_right:
            st.altair_chart(dynamic_chart, use_container_width=True)
        
        st.markdown("---")

# Download button
if not filtered_df.empty:
    st.sidebar.markdown("---")
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
        "Download Filtered Data",
        csv,
        "adm1_filtered_articles.csv",
        "text/csv",
        key="p2_download"
    )
