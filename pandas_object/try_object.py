import pandas_object
import pandas as pd

def main():
    df = pd.DataFrame({
        'age' : ["9-15", "16-24", "25-44"],
        'year' : ["2021", "2021", "2021"],
        'amount' : ["10,5", "15,1", "22,0"]
    })
    # Should be set just from the import alone
    print(df.ext_version)

    # Should be empty still
    print(df.attrs)

    # Call your own extended function
    df.set_title("Table 05300")
    # This should now contain stuff
    print(df.attrs)

    # Do we have access to the method under series as well?
    df['age'].set_title("Seriestitle")
    # Yes, but it adds a "attrs" attribute to the Series, not what we wanted...
    print(df['age'].attrs)
    # Make sure attrs of df is same, even with Series.attrs changed...
    print(df.attrs)
    # Attrs is currently weird?


if __name__ == "__main__":
    main()