import os, sys
import pandas as pd

def range_to_tuple(range):
    x = range.split('-', 1)
    if len(x) < 2:
        return (int(x[0])-1, int(x[0]))
    else:
        return (int(x[0])-1, int(x[1]))

cols = pd.read_csv(
    os.path.join('cols', 'namcs2016.tsv'),
    sep='\t',
    header=0,
    converters={'file_location': range_to_tuple}
)

ranges = cols['file_location'].tolist()

cols['item_headers'] = cols['item_no'].astype(str) + cols['item_description']
headers = cols['item_headers'].tolist()

df = pd.read_fwf(
    os.path.join('data', 'namcs2016.data'),
    colspecs=ranges,
    names=headers,
)

print(df)