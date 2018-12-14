import matplotlib.pyplot as plt
from  matplotlib.ticker import FuncFormatter
import pandas as pd
from pandas.api.types import CategoricalDtype
from preprocessData import load, changeDataType

path = './data/landslide_events.csv'
pd.set_option('display.max_columns', 13)
df = load(path)
df = changeDataType(df)

print(df['distance'].describe())

fig, ax = plt.subplots()
plt.boxplot(df['distance'], showfliers = False)
ax.set_ylabel('Distance')
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.title('Distance of landslide events')
plt.show()