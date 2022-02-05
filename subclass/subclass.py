import pandas as pd

class DfSubclass(pd.DataFrame):
    
    def title_set(self, title):
        self.attrs['title'] = title

    def title_print(self):
        print(self.attrs['title'])