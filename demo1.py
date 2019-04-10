from __future__ import print_function
import pandas as pd
import numpy as np
df = pd.read_excel("Financial Sample.xlsx")
f=df.head()
s=pd.pivot_table(df,index=["Segment","Country","Product"],values=["Month Name","Year"])
h=s.head()
pd.DataFrame.from_dict(h)
writer = pd.ExcelWriter('simple-report.xlsx', engine='xlsxwriter')
df.to_excel(writer, index=False)
writer.save()