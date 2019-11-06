import pandas as pd

from IPython import embed; embed()
df = pd.read_json("./data/results/result-battle-8812.json")

df.to_csv("results.csv")