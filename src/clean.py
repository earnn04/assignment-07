import pandas as pd
import pathlib

def clean_data():
    raw_path = "data/raw/events.csv"
    out_path = "data/clean/events.csv"
    pathlib.Path("data/clean").mkdir(parents=True, exist_ok=True)
    
    df = pd.read_csv(raw_path)
    
    # Remove null evaluations
    df = df.dropna()
    
    # Enforce positive durations and non-empty event profiles
    df = df[df['duration_seconds'] > 0]
    df = df[df['event_type'].astype(str).str.strip() != ""]
    
    # Standardize string timestamp to ISO 8601 (YYYY-MM-DDTHH:MM:SS)
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='mixed').dt.strftime('%Y-%m-%dT%H:%M:%S')
    
    df.to_csv(out_path, index=False)

if __name__ == "__main__":
    clean_data()
