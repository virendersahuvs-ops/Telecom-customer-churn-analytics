
from pathlib import Path
import pandas as pd

project_dir = Path(__file__).resolve().parent.parent
data_dir = project_dir / "data"
csv_files = list(data_dir.glob("*.csv"))

if not csv_files:
    raise FileNotFoundError("CSV file not found in data folder.")

df = pd.read_csv(csv_files[0])

# Inspect the original text values
raw_charges = df["TotalCharges"].astype(str).str.strip()
invalid_mask = pd.to_numeric(raw_charges, errors="coerce").isna()

print("Invalid TotalCharges rows:", invalid_mask.sum())
print("\nOriginal values using repr():")
print([repr(value) for value in raw_charges[invalid_mask].tolist()])

print("\nTenure of affected customers:")
print(df.loc[invalid_mask, "tenure"].value_counts(dropna=False))

print("\nCustomer records affected:")
print(df.loc[invalid_mask, ["customerID", "tenure", "TotalCharges"]])

print("\nVerification complete.")
