import pandas as pd
import os


def to_dataframe(data):
    return pd.DataFrame(data)


def save_csv(df, path):
    # bikin folder kalau belum ada
    os.makedirs(os.path.dirname(path), exist_ok=True)

    df.to_csv(path, index=False)
    print(f"Saved to {path}")