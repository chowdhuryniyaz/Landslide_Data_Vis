import matplotlib.pyplot as plt
from  matplotlib.ticker import FuncFormatter
import pandas as pd
from pandas.api.types import CategoricalDtype
from preprocessData import load, changeDataType

path = './data/landslide_events.csv'
pd.set_option('display.max_columns', 13)
df = load(path)
df = changeDataType(df)

print(df['injuries'].describe())

fig, ax = plt.subplots()
plt.boxplot(df['injuries'])
ax.set_ylabel('Injuries')
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.title('Injuries from landslide events')
plt.show()