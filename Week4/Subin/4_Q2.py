import pandas as pd

df1 = pd.DataFrame(
    data ={'Name': ['cherry', 'mango', 'potato', 'onion'],
           'Type': ['Fruit', 'Fruit', 'Vegetable', 'Vegetable'],
           'Price': ['100', '110', '60', '80']},
    columns= ['Name', 'Type', 'Price'])

df2 = pd.DataFrame(
data ={'Name': ['pepper', 'carrot', 'banana', 'kiwi'],
        'Type': ['Vegetable', 'Vegetable', 'Fruit', 'Fruit'],
        'Price': ['50', '70', '90', '120']},
columns= ['Name', 'Type', 'Price'])


df3 = df1.append(df2)

df_fruit = df3.loc[df3['Type'] == 'Fruit'].sort_values(by='Price', ascending=False)
df_veg = df3.loc[df3['Type'] == 'Vegetable'].sort_values(by='Price', ascending=False)

#상위 2개 합산 과정은 예시 코드를 참조했으나 계속 int와 object를 더할 수 없다고 뜨는 오류 발생
print("Sum of Top 2 Fruit Price: ", sum(df_fruit[:1]['Price']))
print("Sum of Top 2 Vegetable Price: ", sum(df_veg[:1]['Price']))