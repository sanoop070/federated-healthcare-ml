import pandas as pd
from pathlib import Path

# Project root
ROOT = Path(__file__).resolve().parent.parent

# Input files
heart_file = ROOT / "data" / "raw" / "disease_prediction.csv"
diabetes_file = ROOT / "data" / "raw" / "diabetes_prediction_dataset.csv"

# Output folders
heart_output = ROOT / "data" / "heart"
diabetes_output = ROOT / "data" / "diabetes"

# Load datasets
heart_df = pd.read_csv(heart_file)
diabetes_df = pd.read_csv(diabetes_file)

# Shuffle data
heart_df = heart_df.sample(frac=1, random_state=42).reset_index(drop=True)
diabetes_df = diabetes_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Split heart dataset
hospital_1 = heart_df.iloc[:500]
hospital_2 = heart_df.iloc[500:1000]

# Split diabetes dataset
hospital_3 = diabetes_df.iloc[:500]
hospital_4 = diabetes_df.iloc[500:1000]

# Save files
hospital_1.to_csv(heart_output / "hospital_1.csv", index=False)
hospital_2.to_csv(heart_output / "hospital_2.csv", index=False)

hospital_3.to_csv(diabetes_output / "hospital_3.csv", index=False)
hospital_4.to_csv(diabetes_output / "hospital_4.csv", index=False)

print("Hospital datasets created successfully!")
print(f"Hospital 1: {len(hospital_1)} records")
print(f"Hospital 2: {len(hospital_2)} records")
print(f"Hospital 3: {len(hospital_3)} records")
print(f"Hospital 4: {len(hospital_4)} records")