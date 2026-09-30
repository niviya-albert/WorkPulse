"""
WorkPulse – Unemployment Trends & Economic Insights
Module: src/analysis.py
Description: Exploratory Data Analysis (EDA), Statistical Aggregations, and Visualizations.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set publication style
sns.set_theme(style="whitegrid", font_scale=1.1)
plt.rcParams["font.sans-serif"] = "DejaVu Sans"
plt.rcParams["figure.dpi"] = 300


def create_visualizations(df_primary: pd.DataFrame, df_regional: pd.DataFrame, output_dir: str):
    """
    Generates core visual analytics for WorkPulse and saves high-resolution charts.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # -------------------------------------------------------------
    # 1. OVERALL NATIONAL UNEMPLOYMENT TREND OVER TIME (RURAL vs URBAN)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # National overall mean per month
    national_monthly = df_primary.groupby("Date")["Unemployment_Rate_Pct"].mean().reset_index()
    rural_monthly = df_primary[df_primary["Area_Type"] == "Rural"].groupby("Date")["Unemployment_Rate_Pct"].mean().reset_index()
    urban_monthly = df_primary[df_primary["Area_Type"] == "Urban"].groupby("Date")["Unemployment_Rate_Pct"].mean().reset_index()
    
    ax.plot(national_monthly["Date"], national_monthly["Unemployment_Rate_Pct"], 
            marker="o", color="#1E293B", linewidth=3, label="National Average")
    ax.plot(urban_monthly["Date"], urban_monthly["Unemployment_Rate_Pct"], 
            marker="s", linestyle="--", color="#DC2626", linewidth=2, label="Urban Average")
    ax.plot(rural_monthly["Date"], rural_monthly["Unemployment_Rate_Pct"], 
            marker="^", linestyle="--", color="#16A34A", linewidth=2, label="Rural Average")
    
    # Highlight COVID lockdown spike
    ax.axvspan(pd.Timestamp("2020-03-24"), pd.Timestamp("2020-05-31"), 
               color="#FEE2E2", alpha=0.6, label="National Lockdown Peak")
    
    ax.set_title("WorkPulse: Unemployment Rate Trajectory Over Time (May 2019 – June 2020)", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Timeline (Month-Year)", fontweight="bold")
    ax.set_ylabel("Unemployment Rate (%)", fontweight="bold")
    ax.legend(frameon=True, facecolor="white", edgecolor="#CBD5E1")
    plt.xticks(national_monthly["Date"], [d.strftime("%b %Y") for d in national_monthly["Date"]], rotation=45)
    plt.tight_layout()
    
    chart1_path = os.path.join(output_dir, "1_national_trend_rural_vs_urban.png")
    fig.savefig(chart1_path)
    plt.close(fig)
    print(f"[Saved] {chart1_path}")
    
    # -------------------------------------------------------------
    # 2. STATE RANKINGS: TOP 10 HIGHEST & TOP 10 LOWEST UNEMPLOYMENT
    # -------------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    state_rankings = df_primary.groupby("State")["Unemployment_Rate_Pct"].mean().sort_values(ascending=False)
    top_10 = state_rankings.head(10)
    bottom_10 = state_rankings.tail(10).sort_values(ascending=True)
    
    sns.barplot(x=top_10.values, y=top_10.index, ax=ax1, hue=top_10.index, palette="Reds_r", legend=False)
    ax1.set_title("Top 10 States with Highest Avg Unemployment (%)", fontweight="bold")
    ax1.set_xlabel("Average Unemployment Rate (%)")
    for p in ax1.patches:
        ax1.annotate(f"{p.get_width():.1f}%", (p.get_width() + 0.5, p.get_y() + p.get_height() / 2),
                     ha="left", va="center", fontsize=9, fontweight="bold")
                     
    sns.barplot(x=bottom_10.values, y=bottom_10.index, ax=ax2, hue=bottom_10.index, palette="Greens_d", legend=False)
    ax2.set_title("Top 10 States with Lowest Avg Unemployment (%)", fontweight="bold")
    ax2.set_xlabel("Average Unemployment Rate (%)")
    for p in ax2.patches:
        ax2.annotate(f"{p.get_width():.1f}%", (p.get_width() + 0.3, p.get_y() + p.get_height() / 2),
                     ha="left", va="center", fontsize=9, fontweight="bold")
                     
    plt.tight_layout()
    chart2_path = os.path.join(output_dir, "2_state_highest_vs_lowest.png")
    fig.savefig(chart2_path)
    plt.close(fig)
    print(f"[Saved] {chart2_path}")
    
    # -------------------------------------------------------------
    # 3. STATE vs MONTH UNEMPLOYMENT HEATMAP
    # -------------------------------------------------------------
    pivot_df = df_primary.pivot_table(index="State", columns="Year_Month", values="Unemployment_Rate_Pct", aggfunc="mean")
    # Sort states by highest average for clean visual sorting
    pivot_df = pivot_df.loc[state_rankings.index]
    
    fig, ax = plt.subplots(figsize=(14, 10))
    sns.heatmap(pivot_df, cmap="YlOrRd", annot=True, fmt=".1f", linewidths=0.5, ax=ax, cbar_kws={"label": "Unemployment Rate (%)"})
    ax.set_title("State-Wise Monthly Unemployment Rate Heatmap (2019 - 2020)", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Year-Month", fontweight="bold")
    ax.set_ylabel("State", fontweight="bold")
    plt.tight_layout()
    
    chart3_path = os.path.join(output_dir, "3_state_monthly_heatmap.png")
    fig.savefig(chart3_path)
    plt.close(fig)
    print(f"[Saved] {chart3_path}")
    
    # -------------------------------------------------------------
    # 4. ZONAL COMPARISON & RECOVERY DYNAMICS (REGIONAL DATASET)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(12, 6))
    zone_monthly = df_regional.groupby(["Year_Month", "Zone"])["Unemployment_Rate_Pct"].mean().unstack()
    
    for zone in zone_monthly.columns:
        ax.plot(zone_monthly.index, zone_monthly[zone], marker="o", linewidth=2.5, label=zone)
        
    ax.set_title("Zonal Trajectory & Extended Recovery (Jan 2020 – Oct 2020)", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Year-Month", fontweight="bold")
    ax.set_ylabel("Unemployment Rate (%)", fontweight="bold")
    ax.legend(title="Macro-Zone", frameon=True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    chart4_path = os.path.join(output_dir, "4_zonal_recovery_trajectory.png")
    fig.savefig(chart4_path)
    plt.close(fig)
    print(f"[Saved] {chart4_path}")


if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    data_dir = os.path.join(base_dir, "data")
    output_dir = os.path.join(base_dir, "reports", "figures")
    
    df_p = pd.read_csv(os.path.join(data_dir, "cleaned_unemployment_data.csv"))
    df_p["Date"] = pd.to_datetime(df_p["Date"])
    
    df_r = pd.read_csv(os.path.join(data_dir, "cleaned_unemployment_regional.csv"))
    df_r["Date"] = pd.to_datetime(df_r["Date"])
    
    print("Generating EDA Visualizations...")
    create_visualizations(df_p, df_r, output_dir)
    print("All visualizations generated successfully.")
