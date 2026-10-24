
import pandas as pd
from pathlib import Path

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "telco_churn_cleaned.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

print("=" * 50)
print("TELECOM CUSTOMER CHURN - PYTHON EDA")
print("=" * 50)

# 1. Dataset dimensions
print("\n1. DATASET DIMENSIONS")
print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])

# 2. Column information
print("\n2. COLUMN INFORMATION")
df.info()

# 3. Duplicate records
print("\n3. DUPLICATE RECORDS")
print("Duplicates:", df.duplicated().sum())
print("Unique customers:", df["customerID"].nunique())

# 4. Missing values
print("\n4. MISSING VALUES")
print(df.isnull().sum()[df.isnull().sum() > 0])

# 5. Churn distribution
print("\n5. CHURN DISTRIBUTION")
print(df["Churn"].value_counts())

print("\n6. CHURN PERCENTAGE")
print(
    (df["Churn"].value_counts(normalize=True) * 100).round(2)
)

# 7. Numerical summary
print("\n7. NUMERICAL SUMMARY")
print(df[["tenure", "MonthlyCharges", "TotalCharges"]].describe())

print("\nEDA inspection completed.")
