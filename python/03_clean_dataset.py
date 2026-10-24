
from pathlib import Path
import pandas as pd

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Find original CSV
csv_files = list(DATA_DIR.glob("*.csv"))

if not csv_files:
    raise FileNotFoundError("Original CSV not found in data folder.")

input_file = csv_files[0]

# Load original dataset
df = pd.read_csv(input_file)

print("Original dataset shape:", df.shape)

# Clean TotalCharges
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"].astype(str).str.strip(),
    errors="coerce"
)

# Validate customer records
print("\nMissing TotalCharges after conversion:")
print(df["TotalCharges"].isna().sum())

print("\nCustomers with zero tenure:")
print((df["tenure"] == 0).sum())

# Save a separate cleaned copy
output_file = DATA_DIR / "telco_churn_cleaned.csv"
df.to_csv(output_file, index=False)

print("\nCleaned dataset saved to:", output_file.name)
print("Cleaned dataset shape:", df.shape)
print("\nFinal data types:")
print(df.dtypes)

print("\nCleaning completed successfully.")
