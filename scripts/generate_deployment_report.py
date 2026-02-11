import pandas as pd
import numpy as np

def estimate_tokens(text):
    if pd.isna(text): return 0
    return len(str(text)) // 4

def generate_report():
    data_path = "data/processed/all_clean_df.csv"
    df = pd.read_csv(data_path, low_memory=False)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])
    df["quarter"] = df["date"].dt.to_period("Q").astype(str)
    
    # 1. Average tokens per article
    df["tokens"] = df["paragraphs_cleaned"].apply(estimate_tokens)
    avg_tokens = df["tokens"].mean()
    
    # 2. Counts for averages
    # Group by Quarter, Source, Label, ADM2
    # The 'grouped' variable is not used in the final report, so it can be removed or commented out if not needed.
    # grouped = df.groupby(["quarter", "retrieve_source", "Label", "adm2_name_final"]).size().reset_index(name="count")
    
    # Average articles per quarter? Or per quarter-source-label-adm2 combo?
    # Let's provide a breakdown of counts first.
    
    report = []
    report.append("# South Sudan News Analytics Platform - Data Distribution Report\n")
    report.append(f"## Global Statistics")
    report.append(f"- **Total Articles**: {len(df):,}")
    report.append(f"- **Average Tokens per Article**: {avg_tokens:.1f}\n")
    
    report.append(f"## Top 10 ADM2 Regions (Total Volume)")
    report.append(df["adm2_name_final"].value_counts().head(10).to_string())
    report.append("\n")
    
    report.append(f"## Article Counts by Source")
    report.append(df["retrieve_source"].value_counts().to_string())
    report.append("\n")
    
    report.append(f"## Average Articles by Quarter & Label (Top 5 Labels)")
    top_labels = df["Label"].value_counts().head(5).index.tolist()
    q_label_top = df[df["Label"].isin(top_labels)].groupby(["quarter", "Label"]).size().reset_index(name="count")
    pivot_ql = q_label_top.pivot(index="quarter", columns="Label", values="count").fillna(0)
    report.append(pivot_ql.to_string())
    report.append("\n")
    
    report.append(f"## Token Cost Estimation Example")
    sample_size = 15
    total_input_tokens = avg_tokens * sample_size
    # Pricing for gpt-4o-mini: 0.15 per 1M tokens
    cost = (total_input_tokens / 1_000_000) * 0.15
    report.append(f"Summarizing **{sample_size}** articles (avg {avg_tokens:.1f} tokens each):")
    report.append(f"- **Estimated Input Tokens**: {total_input_tokens:,.1f}")
    report.append(f"- **Estimated Cost (gpt-4o-mini)**: ${cost:.5f}")
    
    with open("deployment_report.md", "w", encoding="utf-8") as f:
        f.write("\n".join(report))
    
    print("Report generated: deployment_report.md")

if __name__ == "__main__":
    generate_report()
