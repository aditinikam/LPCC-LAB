import pandas as pd
import os

IC_output = open('IC_Code.txt','w+')
emot = pd.read_csv('emot.csv')
cls_field = pd.read_csv('class_field.csv')
st = pd.DataFrame()
lt = pd.DataFrame()
file = open("file.txt","r")
file.seek(0)
emot_val = emot['Mnemonic'].tolist()
emot_cls_val = emot['Class'].tolist()
emot_op = emot['Opcode'].tolist()
value_cls_field = cls_field['VAL. OF CLASS FIELD'].tolist()
sym_cls_field = cls_field['SYMBOL'].tolist()
LC = 0
literal_values = []
LC_literal = []
symbol_values = []
symbol_size = []
LC_symbol = []
pool_table = [0]
lit_ltorg = []
for line in file:
    line = line.replace('\n',' ')
    line = line.replace(',',' ')
    words = line.split(' ')
    IC_line = ''
    if words[0] == 'START':
        LC = int(words[1])-1

    if words[0] == 'ORIGIN':
        data = words[1].split('+')
        if data[0] in symbol_values:
            ind = symbol_values.index(data[0])
            LC = LC_symbol[ind] + int(data[1])
        IC_line = "(AD,3)(C," + str(LC) + ")"
        IC_output.write(IC_line+"\n")
        continue
    if len(words) > 1 and words[1] == "EQU":
        if words[0] not in symbol_values:
            symbol_values.append(words[0])
            LC_symbol.append(LC)
        LC_symbol[symbol_values.index(words[0])] = LC_symbol[symbol_values.index(words[2])]
        IC_line = "(S," + str(symbol_values.index(words[0])) + ")(AD,4)(C," + str(LC_symbol[symbol_values.index(words[2])]) + ")"
        IC_output.write(IC_line+"\n")
        continue
    if len(words) > 1 and words[1] == "DS":
        if words[0] in symbol_values:
            LC_symbol[symbol_values.index(words[0])] = LC
            symbol_size[symbol_values.index(words[0])] = words[2]
        LC = LC + int(words[2])
        continue

    for word in words:
        if word.startswith('='):
            literal = int(word[2:int(len(word)-1)])
            if literal not in lit_ltorg:
                lit_ltorg.append(literal)
                literal_values.append(literal)
            rev_lit = literal_values[::-1]
            IC_line += "(L," + str(len(literal_values) - rev_lit.index(literal)-1) + ")"
            continue
        if word == 'LTORG':
            pool_table.append(len(literal_values))
            for k in range(pool_table[-2],len(literal_values)):
                LC_literal.append(LC)
                LC += 1
                if k < len(literal_values)-1:
                    IC_line += "(DL,2)(C," + str(literal_values[k]) + ")\n"
                else:
                    IC_line += "(DL,2)(C," + str(literal_values[k]) + ")"
            lit_ltorg = []
            # IC_line += "(DL,02) (C," + literal_values[k] + ")"
            LC -= 1
            continue
        
        
        if word.isdigit():
            IC_line += "(C," + word + ")"
        if word not in emot_val and word != '' and not word.isdigit():
            if word not in symbol_values:
                symbol_values.append(word)
                LC_symbol.append(LC)
                symbol_size.append(1)
            else:
                LC_symbol[symbol_values.index(word)] = LC
            IC_line += "(S," + str(symbol_values.index(word)) + ")"
            
        # if word in symbol_values:
        #     IC_line += "(S," + str(symbol_values.index(word)) + ")"
        if word in emot_val:
            class_val = emot_cls_val[emot_val.index(word)]
            symbol = sym_cls_field[value_cls_field.index(class_val)]
            op_code = str(emot_op[emot_val.index(word)])
            IC_line += "(" + symbol + "," + op_code + ")"
    LC += 1 
            
    IC_output.write(IC_line+"\n")

for i in range(pool_table[-1],len(literal_values)):
    LC_literal.append(LC)
    LC += 1
    IC_line = "(DL,2)(C," + str(literal_values[i]) + ")"
    IC_output.write(IC_line+"\n")

df_st = pd.DataFrame()
df_lt = pd.DataFrame()
df_pt = pd.DataFrame()

st_values = pd.Series(symbol_values)
lc_symbol = pd.Series(LC_symbol)
sizes = pd.Series(symbol_size)
df_st.insert(loc=0, column='Symbol', value = st_values)
df_st.insert(loc=1, column='Size', value = sizes)
df_st.insert(loc=1, column = 'Address', value = lc_symbol)
df_st.to_csv('Symbol Table.csv')
print("\nSymbol Table\n")
print(df_st)

lit_vals = pd.Series(literal_values)
lc_literal = pd.Series(LC_literal)
df_lt.insert(loc=0, column='Literals', value = lit_vals)
df_lt.insert(loc = 1, column = 'Address', value = lc_literal)
df_lt.to_csv('Literal Table.csv')
print('\nLiteral Table\n')
print(df_lt)

pool = pd.Series(pool_table)
df_pt.insert(loc = 0, column = 'Pool', value = pool)
df_pt.to_csv('Pool Table.csv')
print('\nPool Table\n')
print(df_pt)

