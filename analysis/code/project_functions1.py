import pandas as pd
import numpy as np
def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .rename(columns={"sex": "gender"})
          .dropna(subset=['age', 'bmi', 'children', 'charges'])
          .reset_index(drop=True)
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .assign(bmi_category = lambda x: np.where(x['bmi'] < 18.5, 'Underweight', np.where(x['bmi'] < 25, 'Normal', np.where(x['bmi'] < 30, 'Overweight', 'Obese'))))
          .drop(columns=['region'])
          .reset_index(drop=True)
      )

    # Make sure to return the latest dataframe

    return df2
