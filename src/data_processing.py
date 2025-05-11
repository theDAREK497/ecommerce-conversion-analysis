import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    df = df.dropna()
    df['device_type'] = df['device_type'].astype('category')
    return df

def calculate_metrics(df):
    metrics = {
        'avg_page_load': df['page_load_time_seconds'].mean(),
        'conversion_rate': df['conversion'].mean() * 100,
        'bounce_rate': df['bounce_rate'].mean() * 100
    }
    return metrics