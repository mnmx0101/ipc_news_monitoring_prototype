# Data Directory

This directory contains all data files for the news analytics platform.

## Directory Structure

```
data/
├── raw/          # Original, immutable data dump
├── interim/      # Intermediate data that has been transformed
└── processed/    # Final, canonical datasets for analysis
```

## Subdirectories

### `raw/`
Contains the original, unprocessed data files. This data should be treated as **immutable** and never modified directly.

**Examples:**
- Scraped news articles
- Raw API responses
- Downloaded datasets

### `interim/`
Contains intermediate data that has been partially processed or transformed. This is useful for multi-stage processing pipelines.

**Examples:**
- Cleaned text data
- Partially aggregated datasets
- Data with initial feature extraction

### `processed/`
Contains the final, processed datasets ready for analysis, modeling, or visualization. **This is where your processed CSV files should go.**

**Examples:**
- `news_articles_processed.csv` - Fully processed news articles with features
- `sentiment_analysis_results.csv` - Sentiment scores and classifications
- `aggregated_metrics.csv` - Summary statistics and aggregated data

## Data Formats

- **CSV**: Primary format for tabular data
- **JSON**: For nested or hierarchical data structures
- **Parquet**: For large datasets requiring efficient storage and fast reads

## Best Practices

1. **Never commit large data files to git** - The .gitignore is configured to exclude data files
2. **Document your data** - Add metadata files or comments describing the data structure
3. **Use consistent naming** - Follow the pattern: `{source}_{description}_{date}.csv`
4. **Version your data** - Consider adding timestamps or version numbers to processed files
5. **Keep raw data immutable** - Always preserve the original data in `raw/`

## Example Workflow

```
raw/allafrica_articles_20260130.json
  ↓ (cleaning, parsing)
interim/articles_cleaned_20260130.csv
  ↓ (feature extraction, sentiment analysis)
processed/articles_with_features_20260130.csv
```
