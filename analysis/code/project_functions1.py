import pandas as pd
import numpy as np
def load_and_process(path="../data/raw/insurance.csv"):
    
    # Method Chain 1 (Load data and deal with missing data)
    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .dropna()
        .reset_index(drop=True)
    )

    # Method Chain 2 (Create new columns and do processing)
    df2 = (
        df1
        .assign(bmi_group = lambda x: pd.cut(x['bmi'], 
                                             bins=[0,18.5,25,30,35,100], 
                                             labels=['Underweight','Normal','Overweight','Obese Class I','Obese Class II/III']))
        .drop(columns=['region'])
        .sort_values('charges', ascending=False)
        .reset_index(drop=True)
    )

    # Return the latest dataframe
    return df2

