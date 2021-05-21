import pandas as pd
import numpy as np

df = pd.read_pickle('2021-02-07_to_2021-02-21.pickle')
df[df['League'] == 'English Premier League'].Profit.sum()
print('moot')
