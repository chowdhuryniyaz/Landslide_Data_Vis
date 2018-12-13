import matplotlib.pyplot as plt
from  matplotlib.ticker import FuncFormatter
import pandas as pd
from pandas.api.types import CategoricalDtype
from preprocessData import load, changeDataType

path = './data/landslide_events.csv'
pd.set_option('display.max_columns', 13)
df = load(path)
df = changeDataType(df)

count = df['date'].groupby(df.date.dt.year).agg('count')

fig, ax = plt.subplots()

count.plot(ax = ax, color = '#a532ba', rot = 0)
ax.set_xlabel('Year')
ax.set_ylabel('Frequency')
plt.title("Number of landslide events in a year", pad=20, weight='heavy')
plt.tight_layout()
plt.show()