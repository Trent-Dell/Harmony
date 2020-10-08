# this cleans Oracle DB data

#%%
import os
import csv
import matplotlib
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from config import db_password

#%%
# de-duplicate; primary key is DPN
# load data files
arev_load = "data\parts_arev_na.txt"
xrev_load = "data\parts_xrev_na.txt"

#%%
# load x/a-rev into dataframe
df_a = pd.read_csv(arev_load, sep=';')
df_x = pd.read_csv(xrev_load, sep=";")

#%%
# display data in DF
df_a
# df_x

#%%
# data types
df_x.dtypes
df_a.dtypes

#%%
# finding empty values
xNotNull = df_x.notnull().sum()
xIsNull = df_x.isnull().sum()
print(
    f"{xNotNull}\n\n"
    f"{xIsNull}"
    )
#%%
# finding nulls
aNotNull = df_a.notnull().sum()
aIsNull = df_a.isnull().sum()

print(
    f"{aNotNull}\n\n"
    f"{aIsNull}"
)

#%%
# if null, load into new dataframe and save to csv
xGCS_null = df_x[df_x['GCS'].isnull()]
xGCS_null

xCPC_null = df_x[df_x['COMBINED_PC'].isnull()]
xCPC_null

xCPT_null = df_x[df_x['COMBINED_PT'].isnull()]
xCPT_null

#%%
aGCS_null = df_a[df_a['GCS'].isnull()]
aGCS_null

aCPC_null = df_a[df_a['COMBINED_PC'].isnull()]
aCPC_null

aCPT_null = df_a[df_a['COMBINED_PT'].isnull()]
aCPT_null

print(aCPC_null,aCPT_null)

#%%
# aCPT_null
# aCPC_null
aGCS_null

aGCS_null.to_csv('data\aGCS_Nulls.csv')
#%%
# X-rev dupes
# df_x.duplicated(subset=['ITEM_NUMBER'])

# Select duplicate rows except first occurrence based on all columns
dup_xrevDF = df_x[df_x.duplicated(['ITEM_NUMBER'])]
dup_xrevDF

# duplicateRowsDFX = df_x[df_x.duplicated(['ITEM_NUMBER'])]
# duplicateRowsDFX.shape
# duplicateRowsDFX
dup_xrevDF.to_csv('data\Xrev_Dupes.csv')

#%%
# A-rev dupes
dup_arevDF = df_a[df_a.duplicated(['ITEM_NUMBER'])]
dup_arevDF

# duplicateRowsDFA = df_a[df_a.duplicated(['ITEM_NUMBER'])]
# duplicateRowsDFA.shape
dup_arevDF.to_csv('data\Arev_Dupes.csv')

#%%
# compare DFs
xDup_size = len(dup_xrevDF)
aDup_size= len(dup_arevDF)

uniqueDPN = (
    f"The X-rev data file has {len(df_x):,} rows.\n"
    f"Found this many X-rev duplicates: {xDup_size}\n"
    f"The A-rev data file has {len(df_a):,} rows.\n"
    f"Found this many A-rev duplicates: {aDup_size}\n"
    )
print(uniqueDPN)

# with open(file_to_save, "w") as textFile:
#     textFile.write(election_results)  #save the final vote count to the text file.

#%%
# drop
dedup_xRev = df_x[df_x.duplicated(subset=['ITEM_NUMBER'], keep='first')]
# len(dedup_xRev)
dedup_xRev

# future, build function to locate data sources
#%%
# Slicing
is_PT =  df_a[df_a['PART_TYPE']== "SI- Purchased RDR DBOX"]
print(is_PT.head())
#%%
# Slicing
is_PT1 =  df_a[df_a['PART_TYPE']== "Base,Installation (Buy Item)"]
print(is_PT.head())
#%%
len(is_PT1)
is_PT1.to_csv("data\\base_installBuyItem.csv")

#%%
# produce list of PT in both reports
# compare to GNS PT list

#%%
# find nulls; should be none in DPN, PC, PT, CPC, CPT & GCS

# drop nulls

# use this later for findind N/A in attribute fields
    ## get list of values in each column
#%%
# Load into SQL DB
db_string = f"postgres://postgres:{db_password}@127.0.0.1:51734/<-PATH->"
engine = create_engine(db_string)
parts_df.to_sql(name='part', con=engine)