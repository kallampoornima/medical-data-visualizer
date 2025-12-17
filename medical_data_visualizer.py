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

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )






    # 16
    fig.savefig('heatmap.png')
    return fig

