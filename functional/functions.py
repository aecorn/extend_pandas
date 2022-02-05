import pandas as pd

def set_title(df: pd.DataFrame, title: str) -> pd.DataFrame:
    if isinstance(df, pd.DataFrame) or issubclass(type(df), pd.DataFrame):
        df.attrs['title'] = title
        return df
    raise KeyError(f"df: {df.name} doesnt look like a Dataframe, I'm scared of adding title.")