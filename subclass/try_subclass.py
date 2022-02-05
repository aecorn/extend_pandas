import subclass.subclass as subclass

# initialize like a pd.DataFrame
tab = subclass.DfSubclasss

# New methods
tab.title_set("05300")
tab.title_print()

print(type(tab))
print(tab['age'].value_counts())