import matplotlib.pyplot as plt
from  matplotlib.ticker import FuncFormatter
import pandas as pd
from pandas.api.types import CategoricalDtype
from preprocessData import load, changeDataType

path = './data/landslide_events.csv'
pd.set_option('display.max_columns', 13)
df = load(path)
df = changeDataType(df)

df = df[df['country_name'] == 'United States']
count = df['state_or_province'].value_counts(ascending  = True, sort = True)
percent = round((count / count.sum()) * 100, 2)
print(percent)

fig, ax = plt.subplots()

percent.plot(kind = 'barh', ax = ax, color = [plt.cm.PuRd(x)
                                            for x in
                                                (0.27 + i * 1/count.nunique()
                                                for i in range(count.nunique()))], rot = 0)
ax.set_xlabel('Percent')
ax.set_ylabel('State')
plt.title("Percentage of landslide events per state in the US", pad=20, weight='heavy')
plt.tight_layout()
plt.show()