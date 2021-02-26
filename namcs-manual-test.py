import os
import namcs

index = namcs.read_index(
    os.path.join('cols', 'namcs2016.tsv')
)

df = namcs.read_data(
    index,
    os.path.join('data', 'namcs2016.data')
)

print(df)
print(df.describe())