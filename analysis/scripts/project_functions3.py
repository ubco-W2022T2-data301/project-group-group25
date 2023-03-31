import pandas as pd
import numpy as np
def load_and_process(path="../data/raw/insurance.csv"):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
        pd.read_csv("../data/raw/insurance.csv")
        .drop_duplicates()
        .dropna(subset = ["age","sex","bmi","children","smoker","region","charges"])
        .reset_index(drop=True)
        .drop(df[df["children"]<1].index)
    )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
        df1
        .assign(charge_per_child= (lambda x: x['charges'] / x['children'])).sort_values("charges",ascending=True).reset_index(drop=True)
        .rename(columns={"children":"number_of_children"})
        .reset_index(drop=True)
        
      )

    # Make sure to return the latest dataframe

    return df2 
