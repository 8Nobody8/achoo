import os
import namcs

df = namcs.read_datafile(
    os.path.join('cols', 'namcs2016.tsv'),
    os.path.join('data', 'namcs2016.data'),
)

print(df)
print(df.describe())