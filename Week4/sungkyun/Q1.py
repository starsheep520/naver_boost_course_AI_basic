<<<<<<< HEAD
import pandas as pd

idx = ["HDD", "SDD", "USB", "CLOUD"]
data = [19, 11, 5, 97]

series = pd.Series(data, index = idx)
series = series[series>=10][series<=20]

print(series)
=======
import pandas as pd

idx = ["HDD", "SDD", "USB", "CLOUD"]
data = [19, 11, 5, 97]

series = pd.Series(data, index = idx)
series = series[series>=10][series<=20]

print(series)
>>>>>>> 1cd0b0ddf18224d14fbbee1430d43df0883cff73
