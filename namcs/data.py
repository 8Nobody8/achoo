import pandas as pd
from namcs.index import NamcsIndex

def read_data(namcs_index, data_file):
    headers = namcs_index.dataframe.index.tolist()
    ranges = namcs_index.dataframe['file_location'].tolist()

    df = pd.read_fwf(
        data_file,
        colspecs=ranges,
        names=headers,
    )

    return NamcsData(namcs_index, df)

class NamcsData(object):
    
    def __init__(self, index, dataframe):
        self.index = index
        self.dataframe = dataframe