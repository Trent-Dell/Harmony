#%%
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
a? = "data\parts_arev_na.txt"
b? = "data\parts_xrev_na.txt"
#%%
# load 3 sets rev into dataframe
df = pd.read_csv(arev_load, sep=',')
df_x = pd.read_csv(xrev_load, sep=",")