import pandas as pd
from namcs.index import NamcsIndex

def read_data(namcs_index, data_file):
    headers = namcs_index._dataframe.index.tolist()
    ranges = namcs_index._dataframe['file_location'].tolist()

    df = pd.read_fwf(
        data_file,
        colspecs=ranges,
        names=headers,
    )

    return df