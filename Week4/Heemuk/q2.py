import pandas as pd

data1 = {'Name':['cherry','mango','potato','onion'],
         'Type':['Fruit','Fruit','Vegetable','Vegetable'],
         'Price':[100,110,60,80]}
data2 = {'Name':['pepper','carrot','banana','kiwi'],
         'Type':['Vegetable','Vegetable','Fruit','Fruit'],
         'Price':[50,70,90,120]}

df1 = pd.DataFrame(data1, columns=['Name','Type','Price'])
df2 = pd.DataFrame(data2, columns=['Name','Type','Price'])
df3 = pd.concat([df1,df2])
df_fruit = df3[df3['Type']=='Fruit'].sort_values('Price', ascending=False)
df_veg = df3[df3['Type']=='Vegetable'].sort_values('Price', ascending=False)
#Type과 Price column 내림차순으로 정렬

df_fruit['Price'][:2].sum()
print("Sum of Top 2 Fruit Price : {}".format(df_fruit['Price'][:2].sum()))
print("Sum of Top 2 Vegetable Price : {}".format(df_veg['Price'][:2].sum()))
