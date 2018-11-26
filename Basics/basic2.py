import numpy as np
import pandas as pd
import plotly.offline as pyo 

df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
pyo.plot([
    {
        'x' : df.index,
        'y' : df[col],
        'name' : col
    }
    for col in df.columns])
