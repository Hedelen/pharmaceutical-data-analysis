import pandas as pd

metadata_path = r'data\fields.xlsx'

metadata_df = pd.read_excel(metadata_path)
# print(metadata_df.head(10))
print(metadata_df.columns)
print(metadata_df.shape)
print(metadata_df[['Field Name', 'Description']].head(10))

# I feel like I get the gist of this metadata.
