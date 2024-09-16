import pandas as pd

df = pd.read_csv('./dados/tel_e_codigos.csv',delimiter=';')

duplicados = df[df.duplicated()]

print(duplicados)





