import pandas as pd
import pathlib

def generate_features():
    in_path = "data/transformed/events.csv"
    out_path = "data/features/events.csv"
    pathlib.Path("data/features").mkdir(parents=True, exist_ok=True)
    
    df = pd.read_csv(in_path)
    
    # Create required engineered variables
    df['duration_minutes'] = df['duration_seconds'] / 60.0
    df['weekday'] = pd.to_datetime(df['date']).dt.day_name()
    
    df.to_csv(out_path, index=False)

if __name__ == "__main__":
    generate_features()
