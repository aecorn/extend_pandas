import pandas as pd

# Shared functionality under the namespace in 
class DfSMixin:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def title_print(self):
        print(self._obj.attrs['title'])

# Accessor under series
@pd.api.extensions.register_series_accessor("ext")
class ExtSeriesAccessor(DfSMixin):
    pass
    # Title_set() here might be confusing, because you would set the name of the column?
    # Attrs is also weird, documentation says it should be global on Series for the dataset
    # But testing shows that the Series has its own attrs?


# Accessor under dataframes, inherits from mixin 
@pd.api.extensions.register_dataframe_accessor("ext")
class ExtAccessor(DfSMixin):

    def title_set(self, title):
        self._obj.attrs['title'] = title


