import pandas as pd
from scipy.stats import pearsonr


df=pd.read_excel("newdf.xlsx")
df.dropna(inplace=True)

pccs=pearsonr(df["color"], df["reprate"])
print(pccs)


