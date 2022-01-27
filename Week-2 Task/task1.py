import pandas as pd
import os
df = pd.read_csv('emot.csv')
df_st = pd.DataFrame()
file = open("alp.txt","r")
file.seek(0)
emot_val = df['Mnemonic'].tolist()
first_str = ''
symbols = []
lc_val = []
size = []
lc = 0
for i in file:
    data = i.strip()
    str = data.split(" ")
    # print(str)
    first_str = str[0]
    x = data.find('DC')
    res = ''.join(filter(lambda i: i.isdigit(), data))
    if str[0] == 'START':
        lc = int(str[1])-1
        # print(lc)
    if first_str not in emot_val:
        symbols.append(first_str)
        lc_val.append(lc)
        size.append(1)
    if x!=-1:
        # print(res)
        lc=lc+int(res)
    else:
        lc = lc + 1

st_values = pd.Series(symbols)
lc_values = pd.Series(lc_val)
sizes = pd.Series(size)
df_st.insert(loc=0, column='Symbol', value = st_values)
df_st.insert(loc=1, column='Size', value = sizes)
df_st.insert(loc=2, column = 'LC', value = lc_values)
df_st.to_csv('ST.csv')
print(df_st)