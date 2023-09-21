import  pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

df = pd.DataFrame(
    np.random.rand(100, 5),
    columns=['a', 'b', 'c', 'd', 'e'])
profile = ProfileReport(df, title="pandas profile report", html={'style':{'full_width': True}})
profile