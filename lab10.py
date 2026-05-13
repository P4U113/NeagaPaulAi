import pandas as pd
data=pd.read_csv('StudentsPerformance.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
primele5=data.head(5)
print(primele5)


print('\n Structura dataset-ului')
print(data.info())
print('\n Statistici descriptive (numerice)')
print(data.describe())
print('\n Valori lipsa pe fiecare coloană')
print(data.isna().sum())

import unicodedata

print('\n=== Identificarea tipurilor de variabile ===')
categorical_cols = data.select_dtypes(include=['object', 'category']).columns.tolist()
numeric_cols = data.select_dtypes(include=['number']).columns.tolist()
print('variabile categorice:', categorical_cols)
print('variabile numerice:', numeric_cols)

print('\n=== Categorii variabile categorice (fara diacritice) ===')
for col in categorical_cols:
    values = sorted(data[col].dropna().unique().tolist())
    values_no_diacritics = []
    for v in values:
        normalized = unicodedata.normalize('NFKD', str(v))
        normalized = ''.join(ch for ch in normalized if not unicodedata.combining(ch))
        values_no_diacritics.append(normalized)
    print(f'{col}:', values_no_diacritics)