import pandas as pd
df = pd.DataFrame()
file = open("p5.txt","r")
file.seek(0)
literals = []
lc_val = []
lc = 0
for i in file:
    data = i.strip()
    str = data.split(" ",1)
    x = data.find('=')
    if str[0] == 'START':
        lc = int(str[1])-1
        # print(lc)
    else:
        lc = lc + 1
    if x != -1:
        res = ''.join(filter(lambda i: i.isdigit(), str[1]))
        lit = int(res)
        literals.append(lit)
lit_vals = pd.Series(literals)
df.insert(loc=0, column='Literals', value = lit_vals)
df.to_csv('LT.csv')
print(df)
