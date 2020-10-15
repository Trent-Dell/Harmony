#%%
# compare 3 Harmony DB
#%%
import os
import csv
import xlrd
# import matplotlib
import numpy as np
import pandas as pd
# from sqlalchemy import create_engine
# from config import db_password
# %%
# load data files
fileMan = "data\mansourUPC.xlsx"
fileStone = "data\\UPCCodes1.xlsx"
fileHarmony = "data\\UPCcomplete.csv"
#%%
# load 3 sets rev into dataframe
df_mansour = pd.read_excel(fileMan, sep=',')
df_stone = pd.read_excel(fileStone, sep=",")
df_harmony = pd.read_csv(fileHarmony, sep=",")
# %%
df_harmony
# df_mansour
# %%
print(
    f'Main DB data types: {df_harmony.dtypes}\n\n'
    f'Mansour data types: {df_mansour.dtypes}\n\n'
    f'Stone data types: {df_stone.dtypes}\n\n'
)
# %%
# finding empty values
HarmonyNotNull = df_harmony.notnull().sum()
ManNotNull = df_mansour.notnull().sum()
StoneNotNull = df_stone.notnull().sum()

HarmonyIsNull = df_harmony.isnull().sum()
ManIsNull = df_mansour.isnull().sum()
StoneIsNull = df_stone.isnull().sum()

print(
    f"Harmony null values:\n{HarmonyIsNull}\n\n"
    f"Harmony filled in values:\n{HarmonyNotNull}"
    f"Mansour's nulls:\n{ManIsNull}\n\n"
    f"Mansour's filled in values:\n{ManNotNull}"
    f"Stone's nulls:\n{StoneIsNull}\n\n"
    f"Stone's filled in values:\n{StoneNotNull}"
    )
#%%
# zero in on UPC
HarmonyUPCNull = df_harmony[df_harmony['upc'].isnull()]

# if null, load into new dataframe 
# HarmonyUPCNull = df_harmony[df_harmony['upc'].isnull() or df_harmony['upc'].apply(lambda x: len(x)<6)]
# add rows where value is too short
# HarmonyUPCNull['upc'] = HarmonyUPCNull.append((df_harmony['upc'].str.len() < 6))
# HarmonyUPCNull['upc'] = HarmonyUPCNull[df_harmony['upc'].str.len() < 6)]
# df['column_name'] = df[df['column_name'].str.len()<6]
# df[~(df.A.str.len() < 6)]

# df[
# df['names'].apply(lambda x: len(x)>1) &
# df['cars'].apply(lambda x: "i" in x) &
# df['age'].apply(lambda x: int(x)<2)
#   ]

ManUPCNull = df_mansour[df_mansour['upc'].isnull()]

StoneUPCNull = df_stone[df_stone['UPC_Dell'].isnull()]

print(
    f"H:\n{HarmonyUPCNull}\n\n"
    f"M:\n{ManUPCNull}\n\n"
    f"S:\n{StoneUPCNull}"
)
#%%
h2 = df_harmony[df_harmony['upc'].str.len() < 111]

h2
# %%
df_harmony.dtypes
#%%
# load DF with UPC only
df_UPCNullH = HarmonyUPCNull[['dw_sku_num','upc']]
df_UPCNullM = ManUPCNull[['dw_sku_num','upc']]
df_UPCNullS = StoneUPCNull[['dw_sku_num','UPC_Dell']]

print(
    f'Harmony UPC null array size: {df_UPCNullH.shape}\n\n'
    f'Mansour UPC null array size: {df_UPCNullM.shape}\n\n'
    f'Stone UPC null array size: {df_UPCNullS.shape}\n\n'
)
# %%
def dataframe_difference(df1, df2, which=None):
    """Find rows which are different between two DataFrames."""
    comparison_df = df1.merge(df2,
                              indicator=True,
                              how='outer')
    if which is None:
        diff_df = comparison_df[comparison_df['_merge'] != 'both']
    else:
        diff_df = comparison_df[comparison_df['_merge'] == which]
    diff_df.to_csv('data/diff.csv')
    return diff_df

# %%
dataframe_difference(df_UPCNullH, df_UPCNullM)

# set which = both to see which ones are duplicated
# dataframe_difference(df_UPCNullH, df_UPCNullM, which='both')
# %%
# check for duplicates
diff_df = pd.read_csv('data\diff.csv')
duplicate = diff_df[diff_df.duplicated()]
print(
    f"Duplicate rows:\n{duplicate}\n\n"
    f"original dataframe:\n{diff_df}"
)
#%%
# capture less than 6 digits into DF

df_UPCNullS
# %%
