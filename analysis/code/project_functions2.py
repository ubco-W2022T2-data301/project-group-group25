import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def load_and_process(r"C:\Users\somes\Downloads\project-group-group25\data\raw\insurance.csv"):
    df= (
        pd.read_csv(r"C:\Users\somes\Downloads\project-group-group25\data\raw\insurance.csv")
        .dropna()
        .reset_index()
        .rename(columns={"sex": "Sex"})
        .rename(columns={"index": "Index"})
        .rename(columns={"bmi": "BMI"})
        .rename(columns={"children": "Number of Children"})
        .rename(columns={"smoker": "Smoker?"})
        .rename(columns={"region": "Area of Residence"})
        .rename(columns={"charges": "Life Insurance Cost"})
        .rename(columns={"age": "Age"})
    )
    
