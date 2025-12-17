import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = (df['weight'] / ((df['height']/100)**2)> 25).astype(int)

# 3
df['cholesterol'] =(df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc']> 1).astype(int)

