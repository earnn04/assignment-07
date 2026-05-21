import pandas as pd
import pathlib

def transform_data():
    in_path = "data/clean/events.csv"
    out_path = "data/transformed/events.csv"
    pathlib.Path("data/transformed").mkdir(parents=True, exist_ok=True)
    
    df = pd.read_csv(in_path)
    
    # Drop hours/minutes to parse explicit date string
    df['date'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d')
    
    df.to_csv(out_path, index=False)

if __name__ == "__main__":
    transform_data()
