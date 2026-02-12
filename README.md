---
title: South Sudan News Analytics
emoji: 📰
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: "1.40.1"
app_file: Home.py
pinned: false
---

# South Sudan News Analytics Platform

An interactive dashboard for analyzing news coverage of South Sudan, featuring:

- **Dataset Overview**: Comprehensive statistics and visualizations
- **Regional Insights**: ADM1 and ADM2 level analysis
- **Article Browser**: Search and explore individual articles
- **RAG+LLM Summary**: AI-powered situation summaries using OpenAI

## Features

- Real-time data loading from GitHub
- Interactive filters by source, date, region, and topic
- Anomaly detection for crisis monitoring
- OpenAI-powered summarization with strict region/topic filtering

## Configuration

Add your OpenAI API key in the Space settings under "Variables and secrets":
- Variable name: `OPENAI_API_KEY`
- Value: Your OpenAI API key

## Data Source

Data is automatically loaded from the GitHub repository - no manual data upload required.
