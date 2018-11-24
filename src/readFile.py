import matplotlib.pyplot as plt
from  matplotlib.ticker import FuncFormatter
import pandas as pd
from preprocessData import load, changeDataType

path = './data/landslide_events.csv'

df = load(path)
df = changeDataType(df)

print(df.head())
print(df.dtypes)