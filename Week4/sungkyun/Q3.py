<<<<<<< HEAD
import pandas as pd

idx = ["sue", "ryan", "jay", "jane", "anna"]
col = ["round_1", "round_2", "round_3", "round_4", "round_5"]
data = [[55, 65, 60, 66, 57], [64, 77, 71, 79, 67], [88, 81, 79, 89, 77], [45 , 35, 30, 46, 47], [91, 96, 90, 97, 99]]

df = pd.DataFrame(data, index=idx, columns=col)

col_round6 = pd.DataFrame([11, 15, 13, 17, 19], index=idx)

df["round6"] = col_round6
print(df)

=======
import pandas as pd

idx = ["sue", "ryan", "jay", "jane", "anna"]
col = ["round_1", "round_2", "round_3", "round_4", "round_5"]
data = [[55, 65, 60, 66, 57], [64, 77, 71, 79, 67], [88, 81, 79, 89, 77], [45 , 35, 30, 46, 47], [91, 96, 90, 97, 99]]

df = pd.DataFrame(data, index=idx, columns=col)

col_round6 = pd.DataFrame([11, 15, 13, 17, 19], index=idx)

df["round6"] = col_round6
print(df)

>>>>>>> 1cd0b0ddf18224d14fbbee1430d43df0883cff73
print(df.describe().loc[["mean", "max", "min"]])