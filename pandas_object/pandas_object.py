from pandas.core.base import PandasObject

PandasObject.ext_version = 'v1.0.0'

def set_title(df, name: str):
    df.attrs['title'] =  name
PandasObject.set_title = set_title