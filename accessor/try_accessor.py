import namespace
import pandas as pd

df = pd.DataFrame({
    'age' : ["9-15", "16-24", "25-44"],
    'year' : ["2021", "2021", "2021"],
    'amount' : ["10,5", "15,1", "22,0"]
})

# new methods under constructed dataframe-namespace
df.ext.title_set('testname')
df.ext.title_print()

# Same method, but under Series-accessor
df['age'].ext.title_print()