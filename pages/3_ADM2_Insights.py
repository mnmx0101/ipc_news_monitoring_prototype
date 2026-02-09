"""
Page 3: ADM2 Insights (Subnational Level 2)
Static + Dynamic alert/alarm heatmaps per Article Label at county level.
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
    render_adm1_filter, apply_filters, render_summary_metrics
)
from utils.alert_helpers import make_heatmap_pair, add_sd_flags_static, render_alert_legend

st.set_page_config(page_title="ADM2 Insights", layout="wide")

st.title("ADM2 Insights (County Level)")
st.markdown("Alert/alarm detection at Admin Level 2 (County), with **static** and **dynamic** (12-month rolling) thresholds per Article Label.")

# Load data
df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
sources = render_source_filter(df, "p3", default=["radiotamazuj"])
sentiments = render_sentiment_filter(df, "p3", default=["Negative"])
date_range = render_date_filter(df, "p3")

st.sidebar.markdown("---")
st.sidebar.subheader("Geographic Scope")
adm1_regions = render_adm1_filter(df, "p3", default=["Central Equatoria"])

# Apply filters
filtered_df = apply_filters(
    df, sources=sources, date_range=date_range,
    sentiments=sentiments, adm1=adm1_regions
)

# Exclude Unknown County
filtered_df = filtered_df[filtered_df["adm2_name_final"] != "Unknown County"]

# Summary metrics
render_summary_metrics(filtered_df)

st.markdown("---")
render_alert_legend()

# Top N counties
top_n = st.slider("Top N Counties to Display", 10, 50, 30, key="p3_topn")

if filtered_df.empty:
    st.warning("No articles match the current filters.")
else:
    all_labels = sorted([l for l in filtered_df["Label"].dropna().unique() if l != "Uncategorized"])
    
    county_totals = filtered_df["adm2_name_final"].value_counts()
    top_counties = county_totals.head(top_n).index.tolist()
    
    for label_name in all_labels:
        st.subheader(f"{label_name}")
        
        label_df = filtered_df[filtered_df["Label"] == label_name]
        
        if label_df.empty:
            st.info(f"No articles for label '{label_name}' with current filters.")
            continue
        
        ts_adm2 = label_df.groupby(["adm2_name_final", "yearmon"]).size().reset_index(name="article_count")
        ts_adm2["yearmon_date"] = pd.to_datetime(ts_adm2["yearmon"])
        ts_adm2 = ts_adm2[ts_adm2["adm2_name_final"].isin(top_counties)]
        
        if ts_adm2.empty:
            st.info(f"No data to display for '{label_name}' in top counties.")
            continue
        
        static_chart, dynamic_chart = make_heatmap_pair(
            ts_adm2, "adm2_name_final", "article_count", label_name, top_counties,
            height=max(300, min(len(top_counties), top_n) * 20)
        )
        
        col_left, col_right = st.columns(2)
        
        with col_left:
            st.altair_chart(static_chart, use_container_width=True)
        
        with col_right:
            st.altair_chart(dynamic_chart, use_container_width=True)
        
        st.markdown("---")
    
    # Alert Summary Table
    st.subheader("Alert Summary by County (Static Threshold)")
    
    ts_all = filtered_df.groupby(["adm2_name_final", "yearmon"]).size().reset_index(name="article_count")
    ts_all["yearmon_date"] = pd.to_datetime(ts_all["yearmon"])
    ts_all = ts_all[ts_all["adm2_name_final"].isin(top_counties)]
    
    if not ts_all.empty:
        ts_flagged = add_sd_flags_static(ts_all, "adm2_name_final", "article_count")
        
        alert_summary = ts_flagged.groupby("adm2_name_final")["status"].value_counts().unstack(fill_value=0)
        alert_summary["Total Months"] = alert_summary.sum(axis=1)
        if "Alarm-high" in alert_summary.columns:
            alert_summary = alert_summary.sort_values("Alarm-high", ascending=False)
        
        st.dataframe(alert_summary.head(20), use_container_width=True)

# Download button
if not filtered_df.empty:
    st.sidebar.markdown("---")
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
        "Download Filtered Data",
        csv,
        "adm2_filtered_articles.csv",
        "text/csv",
        key="p3_download"
    )
