<<<<<<< HEAD
import pandas as pd

df1 = pd.DataFrame([["cherry", "fruit", 100], ["mango", "fruit", 110], ["potato", "vegetable", 60], ["onion", "vegetable", 80]], columns = ["Name", "Type", "Price"])
df2 = pd.DataFrame([["pepper", "vegetable", 50], ["carrot", "vegetable", 70], ["banana", "fruit", 90], ["kiwi", "fruit", 120]], columns = ["Name", "Type", "Price"])

df3 = pd.concat([df1, df2])
print(df3)

df_fruit = df3.loc[df3["Type"] == "fruit"]
df_fruit = df_fruit.sort_values(by="Price", ascending=False)
print(df_fruit)

df_veg = df3.loc[df3["Type"] == "vegetable"]
df_veg = df_veg.sort_values(by="Price", ascending=False)
print(df_veg)

print("sum of top 2 fruit price :", sum(df_fruit[:2]["Price"]))
=======
import pandas as pd

df1 = pd.DataFrame([["cherry", "fruit", 100], ["mango", "fruit", 110], ["potato", "vegetable", 60], ["onion", "vegetable", 80]], columns = ["Name", "Type", "Price"])
df2 = pd.DataFrame([["pepper", "vegetable", 50], ["carrot", "vegetable", 70], ["banana", "fruit", 90], ["kiwi", "fruit", 120]], columns = ["Name", "Type", "Price"])

df3 = pd.concat([df1, df2])
print(df3)

df_fruit = df3.loc[df3["Type"] == "fruit"]
df_fruit = df_fruit.sort_values(by="Price", ascending=False)
print(df_fruit)

df_veg = df3.loc[df3["Type"] == "vegetable"]
df_veg = df_veg.sort_values(by="Price", ascending=False)
print(df_veg)

print("sum of top 2 fruit price :", sum(df_fruit[:2]["Price"]))
>>>>>>> 1cd0b0ddf18224d14fbbee1430d43df0883cff73
print("sum of top 2 fruit price :", sum(df_veg[:2]["Price"]))