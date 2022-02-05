import pandas as pd

# Shared functionality under the namespace in 
class AvailableBoth:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def title_print(self):
        print(self._obj.attrs['title'])


@pd.api.extensions.register_series_accessor("ext")
class ExtSeriesAccessor(AvailableBoth):
    pass
    # Title_set() here might be confusing, because you would set the name of the column?


# Accessor under dataframes, inherit from Series is possible?
# To avoid 
@pd.api.extensions.register_dataframe_accessor("ext")
class ExtAccessor(AvailableBoth):

    def title_set(self, title):
        self._obj.attrs['title'] = title


