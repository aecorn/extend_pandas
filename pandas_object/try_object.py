import pandas_object
import pandas as pd

def main():
    df = pd.DataFrame()
    # Should be set just from the import alone
    print(df.ext_version)

    # Should be empty still
    print(df.attrs)

    # Call your own extended function
    df.set_title("Table 05300")
    # This should now contain stuff
    print(df.attrs)


if __name__ == "__main__":
    main()