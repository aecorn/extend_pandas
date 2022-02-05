import subclass

def main():
    # initialize like a pd.DataFrame
    tab = subclass.DfSubclass({
        'age' : ["9-15", "16-24", "25-44"],
        'year' : ["2021", "2021", "2021"],
        'amount' : ["10,5", "15,1", "22,0"]
    })

    # New methods
    tab.title_set("05300")
    tab.title_print()

    print(type(tab))
    print(tab['age'].value_counts())

if __name__ == "__main__":
    main()