import pandas as pd

# "Loose" function
def set_title(df: pd.DataFrame, title: str) -> pd.DataFrame:
    if isinstance(df, pd.DataFrame) or issubclass(type(df), pd.DataFrame):
        df.attrs['title'] = title
        return
    raise KeyError(f"df: {df.name} doesnt look like a Dataframe, I'm scared of adding title.")


class DfSubclass(pd.DataFrame):
    
    def title_set(self, title):
        # "Registering" a loose function under a subclass?
        self = set_title(self, title)

    def title_print(self):
        print(self.attrs['title'])