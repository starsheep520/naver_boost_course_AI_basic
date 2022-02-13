import pandas as pd

idx = ["HDD","SDD","USB","CLOUD"]
data = [19,11,6,97]

series = pd.Series(data,index = idx)
series = series[series >= 10][series<=20]
print(series)