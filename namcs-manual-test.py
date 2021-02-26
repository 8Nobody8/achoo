import os
import namcs

index = namcs.read_index(
    os.path.join('cols', 'namcs2016.tsv')
)

data = namcs.read_data(
    index,
    os.path.join('data', 'namcs2016.data')
)

print(data.dataframe)
print(data.dataframe.describe())