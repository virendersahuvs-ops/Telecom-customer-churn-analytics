
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "telco_churn_cleaned.csv"
OUTPUT_DIR = PROJECT_DIR / "reports" / "python_charts"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH)

# Clean churn labels for analysis
df["Churn"] = df["Churn"].astype(str).str.strip()

# 1. Churn distribution
churn_counts = df["Churn"].value_counts()

churn_counts.plot(kind="bar")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "01_churn_distribution.png", dpi=150)
plt.show()
plt.close()

# 2. Churn rate by contract
contract_churn = df.groupby("Contract")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
).sort_values(ascending=False)

contract_churn.plot(kind="bar")
plt.title("Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "02_contract_churn_rate.png", dpi=150)
plt.show()
plt.close()

# 3. Monthly charges by churn status
df.boxplot(column="MonthlyCharges", by="Churn")
plt.title("Monthly Charges by Churn Status")
plt.suptitle("")
plt.xlabel("Churn Status")
plt.ylabel("Monthly Charges")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "03_monthly_charges_boxplot.png", dpi=150)
plt.show()
plt.close()

# 4. Churn rate by tenure group
df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, 72],
    labels=["0-12 Months", "13-24 Months", "25-48 Months", "49-72 Months"]
)

tenure_churn = df.groupby(
    "TenureGroup", observed=False
)["Churn"].apply(lambda x: (x == "Yes").mean() * 100)

tenure_churn.plot(kind="bar")
plt.title("Churn Rate by Customer Tenure")
plt.xlabel("Tenure Group")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "04_tenure_churn_rate.png", dpi=150)
plt.show()
plt.close()

print(f"Charts saved to: {OUTPUT_DIR}")
