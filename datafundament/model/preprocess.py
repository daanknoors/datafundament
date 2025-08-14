import pandas as pd
import janitor

def clean_data(df):
    # snakecase column names
    df = df.copy().clean_names()
    return df

def add_features(df):
    df = df.copy()
    df['winstmarge'] = (df['winst'] / df['verkoop'] * 100).round(2)
    df['aankoopprijs'] = df['verkoop'] - df['winst']
    return df
