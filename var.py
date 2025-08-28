import pandas as pd
import numpy as np
file1 = pd.read_csv("eicher.csv")
df = pd.DataFrame(file1)
orig_cols=df.columns.to_list()
df.columns=[c.strip().lower() for c in df.columns]
for c in df.columns:
    if c== 'date' or c == 'series':
        pass 
    else :
        df[c]=df[c].replace(',', '', regex=True)

df['ltp']=pd.to_numeric(df['ltp'], errors="coerce")
    #log(pt/pt -1)
#print(df['ltp'][0])
#print(df['ltp'][1])
#print(df['ltp'][2])


df['rt']=np.log(df['ltp']/df['ltp'].shift(1))
#print(df['rt'][0])
#print(df['rt'][1])
#print(df['rt'][2])


n=len(df['rt'])
print(n)
df['computation'] = df['rt'][244:n]
#print(df["computation"][244])
df.sort_values(by="computation")
#print(df['computation'][244])
#print(df['computation'][1])
#df.sort_values(by=["computation"])
sorted_df = df.sort_values(by=['computation'], na_position="last").reset_index(drop=True)
print(sorted_df['computation'][13]*100000)

#print(df['computation'][1])
#print(df['computation'][239])

#sorted_df.to_csv("hello1.csv")


#r c in ['low','ltp','close','vwap', 'volume', 'value']:
#   df['c']=df['c'].replace(',', '', regex=True)
#   print(df['c'])


#print(df["OPEN"])
#print(file1)
#print(file1["OPEN"])