import matplotlib.pyplot as plt
from  matplotlib.ticker import FuncFormatter
import pandas as pd
from pandas.api.types import CategoricalDtype
from preprocessData import load, changeDataType

path = './data/landslide_events.csv'
pd.set_option('display.max_columns', 13)
df = load(path)
df = changeDataType(df)

print(df['type_of_area'].value_counts())
print((df['type_of_area'].value_counts() / df['type_of_area'].value_counts().sum()) * 100, 2)

fig, ax = plt.subplots()

plt.scatter(df['distance'], df['type_of_area'], c = '#bf247a')
ax.set_xlabel('Frequency')
ax.set_ylabel('Type of area')
plt.title("Types of areas landslides have taken place", pad=20, weight='heavy')
plt.tight_layout()
plt.show()