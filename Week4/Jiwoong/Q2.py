import pandas as pd

col = ["Name","Type","Price"]

df1 = pd.DataFrame([["cherry","Fruit",100],
                    ["mango","Fruit",110],
                    ["potato","Vegetable",60],
                    ["onion","Vegetable",80]],columns = col)

df2 = pd.DataFrame([["pepper","Vegetable",50],
                    ["carrot","Vegetable",70],
                    ["banana","Fruit",90],
                    ["kiwi","Fruit",120]],columns = col)

df3 = df1.append(df2)

# def get_query(df,**conditions):
#     t = pd.DataFrame()
#     for con in conditions:
#         k,v = con
#         t = df[df[k] == v]
#     return t

def get_sum_in_columns(df,col,ascending,heads):
    return df.sort_values(col,axis = 0,ascending=ascending).head(heads).sum()[col]

df_fruit = df3[df3['Type'] == 'Fruit']
df_veg = df3[df3['Type'] == 'Vegetable']

print("Sum of Top 2 Fruit Price : ",get_sum_in_columns(df_fruit,'Price',False,2))
print("Sum of Top 2 Vegetable Price : ",get_sum_in_columns(df_veg,'Price',False,2))
