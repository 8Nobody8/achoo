import pandas as pd
from namcs.exceptions import HeadersNotUniqueException

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

def read_headers(header_path):
    return pd.read_csv(
        header_path,
        sep='\t',
        header=0,
        converters={'file_location': range_to_tuple}
    )

def read_datafile(header_path, data_path):
    cols = read_headers(header_path)

    throw_if_col_has_duplicates(cols['item_no'])

    ranges = cols['file_location'].tolist()
    headers = cols['item_no'].tolist()

    return pd.read_fwf(
        data_path,
        colspecs=ranges,
        names=headers,
    )