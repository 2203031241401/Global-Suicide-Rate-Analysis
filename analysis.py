import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def basic_stats(df):
    return df.describe()

def suicides_by_country(df):
    return df.groupby("country")["suicides_no"].sum().sort_values(ascending=False)