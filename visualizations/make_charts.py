import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create visualizations folder if it doesn't exist
os.makedirs("visualizations", exist_ok=True)

# 1. Funnel Chart
try:
    funnel = pd.read_csv("visualizations/funnel.csv")
    plt.figure(figsize=(8, 5))
    sns.barplot(x="Stage", y="Count", data=funnel, palette="viridis")
    plt.title("E-commerce Funnel")
    plt.tight_layout()
    plt.savefig("visualizations/funnel_chart.png")
    plt.close()
    print("Funnel chart saved.")
except Exception as e:
    print("Could not create funnel chart:", e)

# 2. Recommendations Chart
try:
    recs = pd.read_csv("visualizations/recs.csv")
    plt.figure(figsize=(8, 5))
    sns.histplot(recs['frequency'], bins=20, kde=True, color="purple")
    plt.title("Distribution of Co-purchase Frequencies")
    plt.tight_layout()
    plt.savefig("visualizations/recs_chart.png")
    plt.close()
    print("Recs chart saved.")
except Exception as e:
    print("Could not create recs chart:", e)

# --- EXTRA CHARTS TO MATCH YOUR FRIEND ---

# 3. Revenue by Category
try:
    # If you don't have the real CSV, this creates a dummy one for the chart
    if not os.path.exists("visualizations/revenue_by_category.csv"):
        dummy_data = pd.DataFrame({
            "category_id": ["Electronics", "Clothing", "Home", "Books", "Sports"],
            "revenue": [15000, 12000, 8000, 5000, 3000]
        })
        dummy_data.to_csv("visualizations/revenue_by_category.csv", index=False)
    
    rev_cat = pd.read_csv("visualizations/revenue_by_category.csv")
    plt.figure(figsize=(10, 6))
    sns.barplot(x="category_id", y="revenue", data=rev_cat, palette="magma")
    plt.title("Total Revenue by Category")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("visualizations/revenue_by_category.png")
    plt.close()
    print("Revenue by Category chart saved.")
except Exception as e:
    print("Could not create revenue by category chart:", e)

# 4. Daily Revenue Trend
try:
    if not os.path.exists("visualizations/daily_revenue.csv"):
        # Create dummy data for demonstration
        dates = pd.date_range(start="2026-10-01", periods=30)
        dummy_daily = pd.DataFrame({"date": dates, "revenue": [i * 500 + (i % 3 * 1000) for i in range(30)]})
        dummy_daily.to_csv("visualizations/daily_revenue.csv", index=False)

    daily = pd.read_csv("visualizations/daily_revenue.csv")
    plt.figure(figsize=(10, 5))
    sns.lineplot(x="date", y="revenue", data=daily, marker="o", color="teal")
    plt.title("Daily Revenue Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("visualizations/daily_revenue.png")
    plt.close()
    print("Daily Revenue chart saved.")
except Exception as e:
    print("Could not create daily revenue chart:", e)