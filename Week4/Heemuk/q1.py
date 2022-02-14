import pandas as pd

idx = ['HDD','SSD','USB','CLOUD']
data = [19, 11, 5, 97]
series = pd.Series(data=data, index=idx)
series = series[(series >= 10) & (series <=20)]
# 10 이상, 20 이하를 가지는 series data만 저장

print(series)
