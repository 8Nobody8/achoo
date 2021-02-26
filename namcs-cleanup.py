import os, sys
import pandas as pd
from HeadersNotUniqueException import HeadersNotUniqueException

def throw_if_col_has_duplicates(df_col):
    dupes = df_col.loc[df_col.duplicated() == True]
    if not dupes.empty:
        raise HeadersNotUniqueException('The following indices are not unique: {}.'.format(dupes.index.values.tolist()))

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

throw_if_col_has_duplicates(cols['item_no'])

ranges = cols['file_location'].tolist()
headers = cols['item_no'].tolist()

df = pd.read_fwf(
    os.path.join('data', 'namcs2016.data'),
    colspecs=ranges,
    names=headers,
)

print(df)

print(df.describe())