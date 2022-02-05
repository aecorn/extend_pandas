import functions
import pandas as pd

def main():
    df = pd.DataFrame({
        'age' : ["9-15", "16-24", "25-44"],
        'year' : ["2021", "2021", "2021"],
        'amount' : ["10,5", "15,1", "22,0"]
    })

    # Function on the loose
    functions.set_title(df, "Functional title")
    print(df.attrs)

    # Function can be type specific, try using on Series, we want error here
    #functions.set_title(df['age'], 'Age column')

if __name__ == "__main__":
    main()