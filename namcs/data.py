import pandas as pd
from namcs.index import NamcsIndex

def read_data(namcs_index, data_file):
    colspecs, names = namcs_index._get_colspecs_and_names()

    df = pd.read_fwf(
        data_file,
        colspecs=colspecs,
        names=names,
    )

    return df