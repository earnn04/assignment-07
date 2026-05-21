import pandas as pd
import pathlib

def clean_data():
    raw_path = "data/raw/events.csv"
    out_path = "data/clean/events.csv"
    pathlib.Path("data/clean").mkdir(parents=True, exist_ok=True)
    
    df = pd.read_csv(raw_path)
    
    # 1. Drop rows with missing values
    df = df.dropna()
    
    # 2. Fix duration_seconds: convert to float first (to handle '.0'), then to integer
    df['duration_seconds'] = pd.to_numeric(df['duration_seconds'], errors='coerce')
    df = df.dropna()  # Drop rows that couldn't convert to numbers
    df['duration_seconds'] = df['duration_seconds'].astype(int)
    
    # 3. Filter for strictly positive duration values
    df = df[df['duration_seconds'] > 0]
    
    # 4. Enforce valid event types strictly
    valid_types = {'click', 'login', 'purchase', 'scroll', 'view'}
    df = df[df['event_type'].isin(valid_types)]
    
    # 5. Normalize timestamp to ISO 8601
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='mixed').dt.strftime('%Y-%m-%dT%H:%M:%S')
    
    df.to_csv(out_path, index=False)

if __name__ == "__main__":
    clean_data()
