#%%
import pandas as pd 

col_nams = ['c{0:02d}'.format(i) for i in range(638)]
df = pd.read_csv('ikaWidgetCSV_20191109183857.tcsv', names=col_nams)
print(df)