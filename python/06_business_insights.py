
import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "telco_churn_cleaned.csv"

df = pd.read_csv(DATA_PATH)
df["Churn"] = df["Churn"].astype(str).str.strip()

print("=" * 55)
print("TELECOM CUSTOMER CHURN - BUSINESS INSIGHTS")
print("=" * 55)

# Overall churn
churn_rate = (df["Churn"].eq("Yes").mean() * 100)
print(f"\n1. Overall churn rate: {churn_rate:.2f}%")

# Contract-wise churn
contract_rates = (
    df.groupby("Contract")["Churn"]
    .apply(lambda x: x.eq("Yes").mean() * 100)
    .sort_values(ascending=False)
)
print("\n2. Churn rate by contract type:")
print(contract_rates.round(2))

# Tenure-wise churn
df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, 72],
    labels=["0-12 Months", "13-24 Months", "25-48 Months", "49-72 Months"]
)

tenure_rates = (
    df.groupby("TenureGroup", observed=False)["Churn"]
    .apply(lambda x: x.eq("Yes").mean() * 100)
)
print("\n3. Churn rate by tenure:")
print(tenure_rates.round(2))

# Average monthly charges
charges = df.groupby("Churn")["MonthlyCharges"].mean()
print("\n4. Average monthly charges by churn status:")
print(charges.round(2))

# Internet service
internet_rates = (
    df.groupby("InternetService")["Churn"]
    .apply(lambda x: x.eq("Yes").mean() * 100)
    .sort_values(ascending=False)
)
print("\n5. Churn rate by internet service:")
print(internet_rates.round(2))

print("\nAnalysis completed.")
