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

# if null, load into new dataframe 
HarmonyUPCNull = df_harmony[df_harmony['upc'].isnull()]

ManUPCNull = df_mansour[df_mansour['upc'].isnull()]

StoneUPCNull = df_stone[df_stone['UPC_Dell'].isnull()]

print(
    f"H:\n{HarmonyUPCNull}\n\n"
    f"M:\n{ManUPCNull}\n\n"
    f"S:\n{StoneUPCNull}"
)
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
#%%
# capture less than 6 digits into DF

df_UPCNullS
# %%
