import pandas as pd
df = pd.DataFrame()
file = open("file.txt","r")
file.seek(0)
literals = []
lit_ltorg = []
lc_val = []
lc = 0
pool = [0]
for i in file:
    j=0
    data = i.strip()
    str = data.split(" ",1)
    x = data.find('=')
    if str[0] == 'START':
        lc = int(str[1])
        # print(lc)
    elif str[0] == 'LTORG':
        pool.append(len(literals))
        lit_ltorg = []
        for k in range(pool[-2],len(literals)):
            lc_val.append(lc)
            lc += 1
    else:
        lc = lc + 1
    if x != -1:
        res = ''.join(filter(lambda i: i.isdigit(), str[1]))
        lit = int(res)
        if lit not in lit_ltorg:
            literals.append(lit)
            lit_ltorg.append(lit)
for i in range(pool[-1],len(literals)):
    lc_val.append(lc)
    lc += 1
lit_vals = pd.Series(literals)
df.insert(loc=0, column='Literals', value = lit_vals)
df.insert(loc = 1, column = 'Address', value = lc_val)
df.to_csv('LT.csv')
print(df)
print("Pool Table:")
print(pool[0:len(pool)-1])
