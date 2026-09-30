"""
WorkPulse – Unemployment Trends & Economic Insights
Module: src/data_cleaning.py
Description: Data loading, cleaning, validation, and preprocessing pipeline.
"""

import pandas as pd
import numpy as np
import os


def load_and_clean_primary_data(filepath: str) -> pd.DataFrame:
    """
    Loads and cleans the primary dataset ('Unemployment in India.csv').
    
    Steps:
    1. Strip leading and trailing whitespace from column names.
    2. Remove fully empty (NaN) trailing rows.
    3. Strip whitespace from string columns (State, Frequency, Area_Type).
    4. Parse 'Date' column into proper datetime objects (format: DD-MM-YYYY).
    5. Convert 'Employed_Count' to integer.
    6. Rename columns to standardized, clean Pythonic names.
    7. Sort chronologically by Date, State, and Area_Type.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at {filepath}")
        
    df = pd.read_csv(filepath)
    
    # 1. Strip whitespace from column headers
    df.columns = df.columns.str.strip()
    
    # 2. Drop completely blank rows (trailing 28 rows in raw dataset)
    df = df.dropna(how="all").copy()
    
    # 3. Clean whitespace in text columns
    text_cols = ["Region", "Frequency", "Area"]
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
            
    # 4. Standardize column names
    rename_dict = {
        "Region": "State",
        "Estimated Unemployment Rate (%)": "Unemployment_Rate_Pct",
        "Estimated Employed": "Employed_Count",
        "Estimated Labour Participation Rate (%)": "Labour_Participation_Rate_Pct",
        "Area": "Area_Type"
    }
    df = df.rename(columns=rename_dict)
    
    # 5. Convert Date to datetime format
    df["Date"] = pd.to_datetime(df["Date"].astype(str).str.strip(), format="%d-%m-%Y")
    
    # 6. Convert Employed count to integer
    df["Employed_Count"] = df["Employed_Count"].astype(np.int64)
    
    # 7. Extract helper time features (Year, Month, Month_Name, Year_Month)
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Month_Name"] = df["Date"].dt.strftime("%B")
    df["Year_Month"] = df["Date"].dt.strftime("%Y-%m")
    
    # 8. Sort chronologically
    df = df.sort_values(by=["Date", "State", "Area_Type"]).reset_index(drop=True)
    
    return df


def load_and_clean_regional_data(filepath: str) -> pd.DataFrame:
    """
    Loads and cleans the regional dataset ('Unemployment_Rate_upto_11_2020.csv').
    
    Includes Macro-Zones (South, North, East, West, Northeast) and Geospatial coordinates.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at {filepath}")
        
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip()
    
    # Clean text columns
    df["Region"] = df["Region"].astype(str).str.strip()
    df["Frequency"] = df["Frequency"].astype(str).str.strip()
    df["Region.1"] = df["Region.1"].astype(str).str.strip()
    
    # Correct coordinates: In raw Kaggle dataset, 'longitude' holds lat values (~10-33) and 'latitude' holds long values (~71-92)
    rename_dict = {
        "Region": "State",
        "Region.1": "Zone",
        "Estimated Unemployment Rate (%)": "Unemployment_Rate_Pct",
        "Estimated Employed": "Employed_Count",
        "Estimated Labour Participation Rate (%)": "Labour_Participation_Rate_Pct",
        "longitude": "Latitude",
        "latitude": "Longitude"
    }
    df = df.rename(columns=rename_dict)
    
    # Convert Date
    df["Date"] = pd.to_datetime(df["Date"].astype(str).str.strip(), format="%d-%m-%Y")
    df["Employed_Count"] = df["Employed_Count"].astype(np.int64)
    
    # Add helper time features
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Month_Name"] = df["Date"].dt.strftime("%B")
    df["Year_Month"] = df["Date"].dt.strftime("%Y-%m")
    
    # Sort chronologically
    df = df.sort_values(by=["Date", "Zone", "State"]).reset_index(drop=True)
    
    return df


if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    data_dir = os.path.join(base_dir, "data")
    
    file1 = os.path.join(data_dir, "Unemployment in India.csv")
    file2 = os.path.join(data_dir, "Unemployment_Rate_upto_11_2020.csv")
    
    print("--- Cleaning Primary Dataset ---")
    df_primary = load_and_clean_primary_data(file1)
    out1 = os.path.join(data_dir, "cleaned_unemployment_data.csv")
    df_primary.to_csv(out1, index=False)
    print(f"Saved clean primary dataset to: {out1}")
    print(f"Shape: {df_primary.shape} | Nulls: {df_primary.isnull().sum().sum()}")
    
    print("\n--- Cleaning Regional / Zonal Dataset ---")
    df_regional = load_and_clean_regional_data(file2)
    out2 = os.path.join(data_dir, "cleaned_unemployment_regional.csv")
    df_regional.to_csv(out2, index=False)
    print(f"Saved clean regional dataset to: {out2}")
    print(f"Shape: {df_regional.shape} | Nulls: {df_regional.isnull().sum().sum()}")
