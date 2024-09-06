import pandas as pd

#CONVERTENDO O AQUIVO EXCEL PARA CSV

df = pd.read_excel(r'coloque aqui o caminho para seu arquivo excel.xlsx')

#CAMINHO DO NOVO ARQUIVO GERADO COMO CVS - ESSE CAMINHO AQUI VOCE COPIA E COLA NO OUTRO CÓDIGO
df.to_csv(r'coloque aqui o caminho gerado para seu arquivo csv', index=False)