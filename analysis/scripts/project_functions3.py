import pandas as pd

def load_and_process(path="../data/raw/insurance.csv"):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
        pd.read_csv("../data/raw/insurance.csv")
        .drop_duplicates()
    )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
        df1
        .rename(columns={"children":"number_of_children"})
        .assign(charge_per_child= (lambda x: x['charges'] / x['number_of_children'])).sort_values("charges",ascending=True).reset_index(drop=True)
        .reset_index(drop=True)
      )
    df3=(
        df2
        .drop(df2[df2["number_of_children"]<1].index)
        .dropna(subset = ["age","sex","bmi","number_of_children","smoker","region","charges"])
        .reset_index(drop=True)
    )
        
         

    # Make sure to return the latest dataframe

    return df3 

