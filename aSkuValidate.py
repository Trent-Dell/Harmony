#%%
# compare 3 Harmony DB
#%%
import os
import csv
import matplotlib
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from config import db_password
# %%
# load data files
fileMan = "data\mansourUPC.xlsx"
fileStone = "data\\UPCCodes1.xlsx"
fileHarmony = "data\\UPCcomplete.csv"
#%%
# load 3 sets rev into dataframe
df_mansour = pd.read_csv(fileMan, sep=',')
df_stone = pd.read_csv(fileStone, sep=",")
df_harmony = pd.read_csv(fileHarmony, sep=",")
# %%
