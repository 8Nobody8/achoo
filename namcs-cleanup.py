import os, sys
import pandas as pd

df = pd.read_fwf(
    os.path.join('data', 'namcs2016.data'), 
    [
        (0, 2),
        (2, 3),
        (3, 6),
        (6, 7),
        (7, 10),
        ()
    ])

print(df)