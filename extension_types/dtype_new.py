import pandas as pd
import numpy as np


@pd.api.extensions.register_extension_dtype
class CustomDtype(pd.api.extensions.ExtensionDtype):
    
    name = "custom"
    #type: type[CategoricalDtypeType] = CategoricalDtypeType
    #kind: str_type = "O"
    str = "|O08"
    base = np.dtype("O")
    _metadata = ("categories", "ordered")
    #_cache_dtypes: dict[str_type, PandasExtensionDtype] = {}

    def type():
        pass

    def name():
        pass

    def construct_array_type():
        pass