import matplotlib.pyplot as plt
from  matplotlib.ticker import FuncFormatter
import pandas as pd
from pandas.api.types import CategoricalDtype
from preprocessData import load, changeDataType

path = './data/landslide_events.csv'
pd.set_option('display.max_columns', 13)
df = load(path)
df = changeDataType(df)

#df.cause_of_landslide.cat.remove_categories(['Flooding', 'Earthquake', 'Mining digging', 'Freeze thaw', 'Construction', 'Other', 'Volcano', 'Dam embankment collapse'], inplace = True)

count = df['size_of_landslide'].value_counts(sort = True)
percent = round((count / count.sum()) * 100, 2)

colours = [plt.cm.PuRd(x)
            for x in
                (0.27 + i * 0.6/count.nunique()
                for i in range(count.nunique()))]

explode = []
for i in percent:
    if i <= 10:
        explode.append(0.3)
    else:
        explode.append(0.0)

fig, ax = plt.subplots()

plt.pie(count, colors = colours, startangle = 90, explode = explode, autopct = '%.0f%%', labels = df['size_of_landslide'].cat.categories)
plt.legend(df['size_of_landslide'].cat.categories, bbox_to_anchor=(1.15, 0.8), loc="center left", frameon=False)
plt.text(-2, 1.08, "Different sizes of landslides")
plt.tight_layout()

#   Found code from: https://python-graph-gallery.com/160-basic-donut-plot/
hole=plt.Circle((0, 0), 0.5, color='white')
p=plt.gcf()
p.gca().add_artist(hole)
plt.show()