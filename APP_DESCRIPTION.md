# News Analytics Platform

## Overview
The **News Analytics Platform** is a unified tool designed for humanitarian and food security analysts. It consists of multiple dashboards accessible via the sidebar on the **Home.py** landing page.

## Dashboards

### 1. General Dashboard (`1_General_Dashboard.py`)
- Broad overview of news volume and average sentiment.
- Regional and thematic breakdowns.

### 2. Crisis Monitoring Dashboard (`2_Crisis_Dashboard.py`)
- **Focus**: Early Warning, Regional Contextualization, and Sentiment Intensity.
- **Key Metric**: Negative Intensity (severity of badness).
- **Article Volume**: Track the frequency of news reporting over time.
- **Sentiment Score**: Monitor the average sentiment (Positive/Negative) of news coverage.
- **Negative Intensity**: A focused metric (0-1) where higher values indicate more severe negative reporting.
- **Anomaly Detection**: Automatic statistical flagging (Alerts/Alarms) when trends deviate significantly from the historical baseline (1 or 2 Standard Deviations).

### 2. 🌍 Geographic & Thematic Analysis
- **Regional Filter**: Drill down by ADM1 (State) and ADM2 (County).
- **Thematic Filter**: Analyze specific topics like "Conflict", "Food Security", "Health", etc.
- **Source Breakdown**: Compare reporting trends across different news outlets.

### 3. 🤖 AI Contextual Summary (RAG+LLM)
- **Generative Summaries**: Uses OpenAI's GPT models to read top relevant articles and generate a sharp, bulleted situation report.
- **Smart Filtering**: The AI summarizes only the articles matching your selected region, theme, and time window.

### 4. 📖 Article Browser
- **Detailed View**: Read the full text of individual articles.
- **Metadata**: View publication date, source, sentiment score, and classification labels.

## Data Source
The dashboard is powered by processed news data located in `data/processed/all_clean_df.csv`.
