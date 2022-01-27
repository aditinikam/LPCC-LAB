import pandas as pd
import os
df = pd.read_csv('emot.csv')
df_st = pd.DataFrame()
df_lt = pd.DataFrame()
file = open("f2.txt","r")
file.seek(0)
emot_val = df['Mnemonic'].tolist()
first_str = ''
symbols = []
lc_smb_val = []
size = []
lc_smb = 0
literals = []
lc_val = []
lc = 0
pool = [0]
file.seek(0)
for i in file:
    data = i.strip()
    str = data.split(" ",1)
    # print(str)
    first_str = str[0]
    x = data.find('DC')
    res = ''.join(filter(lambda i: i.isdigit(), data))
    # str = data.split(" ")
    y = data.find('=')
    if str[0] == 'START':
        lc = int(str[1])
        # print(lc)
    elif str[0] == 'LTORG':
        pool.append(len(literals))
        for k in range(pool[-2],len(literals)):
            lc_val.append(lc)
            lc += 1
    elif str[0] == 'ORIGIN':
        data_res = str[1].split('+')
        if data_res[0] in symbols:
            ind = symbols.index(data_res[0])
            lc = lc_smb_val[ind] + int(data_res[1])
    # elif 
    #     data_res = 
    else:
        lc = lc + 1
    if first_str not in emot_val:
        symbols.append(first_str)
        # print(str[1])
        data_res = str[1].split(' ')
        if data_res[0] == 'EQU':
            print(data_res)
            lc_smb_val.append(lc_smb_val[symbols.index(data_res[1])])
        else: 
            lc_smb_val.append(lc-1)
        size.append(1)
    if x!=-1:
        # print(res)
        lc=lc+int(res)
    if y != -1:
        res = ''.join(filter(lambda i: i.isdigit(), str[1]))
        lit = int(res)
        literals.append(lit)
for i in range(pool[-1],len(literals)):
    lc_val.append(lc)
    lc += 1
st_values = pd.Series(symbols)
lc_values = pd.Series(lc_smb_val)
sizes = pd.Series(size)
df_st.insert(loc=0, column='Symbol', value = st_values)
df_st.insert(loc=1, column='Size', value = sizes)
df_st.insert(loc=2, column = 'LC', value = lc_values)
df_st.to_csv('ST.csv')
print(df_st)
lit_vals = pd.Series(literals)
df_lt.insert(loc=0, column='Literals', value = lit_vals)
df_lt.insert(loc = 1, column = 'Address', value = lc_val)
df.to_csv('LT.csv')
print(df_lt)
print("Pool Table:")
print(pool[0:len(pool)-1])