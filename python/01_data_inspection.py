
from pathlib import Path
import pandas as pd

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Locate the dataset
csv_files = list(DATA_DIR.glob("*.csv"))

if not csv_files:
    raise FileNotFoundError(
        "No CSV file found inside the data folder."
    )

file_path = csv_files[0]
df = pd.read_csv(file_path)

print("\n--- DATASET DETAILS ---")
print("File:", file_path.name)
print("Rows and columns:", df.shape)

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- FIRST 5 ROWS ---")
print(df.head().to_string())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print("Exact duplicate rows:", df.duplicated().sum())

print("\n--- UNIQUE CUSTOMERS ---")
if "customerID" in df.columns:
    print("Unique customer IDs:", df["customerID"].nunique())

print("\n--- CHURN DISTRIBUTION ---")
if "Churn" in df.columns:
    print(df["Churn"].value_counts(dropna=False))
    print("\nChurn percentage:")
    print(
        (df["Churn"].value_counts(normalize=True, dropna=False) * 100)
        .round(2)
    )

print("\nInspection completed.")
