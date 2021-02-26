import pandas as pd
from namcs.exceptions import HeadersNotUniqueException

def read_index(index_file):
    cols = pd.read_csv(
        index_file,
        sep='\t',
        header=0,
        converters={'file_location': range_to_tuple}
    )

    throw_if_col_has_duplicates(cols['item_no'])

    cols.set_index('item_no', inplace=True)

    return NamcsIndex(cols)

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

class NamcsIndex(object):

    def __init__(self, dataframe):
        self.dataframe = dataframe