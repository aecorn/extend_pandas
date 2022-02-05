# Extending Pandas
Trying out different ways of extending Pandas according to the documentation:\
https://pandas.pydata.org/docs/development/extending.html


### Simple functions that take and return dataframes, is not really "extending"
But its a very good place to start, and a good way of exploring what next step to take and organize by.

### Monkey-patching is not recommended
Placed under "pandas_object"-folder, this adds methods to all "pandas-objects", including Series... This can get messy fast, and is to be avoided.

### Subclassing introduces strong coupling?
If you have frequently repeated dataset-types with strongly coupled behaviour-needs, this might be a good option, but it might be unclear by name and type, that, really, this is only a slightly modified pandas-dataframe...

### Accessors are nice
With introducing your own namespace under DataFrames and Series, you can make them do new things. But this would probably be better with "bigger domains" than multiple Subclasses would? Or maybe having many isnt a problem?