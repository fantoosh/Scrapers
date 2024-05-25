import pandas as pd

df1 = pd.read_csv('PropertySearchResults.csv', low_memory=False, on_bad_lines='skip', dtype=str)
df2 = pd.read_csv('polkcadproperties.csv', low_memory=False, dtype=str)
df3 = pd.read_csv('polkcad-property-data.csv', low_memory=False)

print(f'df1{df1.columns}')
print(f'df2{df2.columns}')
print(f'df3{df3.columns}')

print(df1.info())
print(df3.info())

df1_df3 = df1.merge(df3, on=['Property ID', 'Owner Name'])
print(df1_df3.info())
# pd.concat([df1, df3], )

final_df = df1_df3.merge(df2, on=['url', 'Owner Name'])
print(final_df.info())

final_df.to_csv('polkcad-property-data-final.csv', index=False)

