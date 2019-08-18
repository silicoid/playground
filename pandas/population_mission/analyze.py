#!/usr/bin/python3

import pandas as pd

df = pd.read_csv("Population_Estimates.csv")
df.set_index("Year",inplace=True)
df.sort_index(inplace=True)

df_clean = pd.DataFrame()

for gender in df["Gender"].unique():
    print(gender)

    gender_df = df.copy()[df["Gender"]==gender]
    gender_df[f'{gender}_Total'] = gender_df["Total"]

    if df_clean.empty:
        df_clean = gender_df[[f'{gender}_Total']]

    else:
        df_clean = df_clean.join(gender_df[f'{gender}_Total'])

graph = df_clean.plot().get_figure()
graph.savefig("test.pdf")
