import pandas as pd
import matplotlib.pyplot as plt

#CAMINHO DO ARQUIVO CSV
df = pd.read_csv(
    r'coloque aqui o caminho para seu arquivo csv')

#PASSANDO OS NOMES DAS COLUNAS
numeros_sorteados = df[['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6',
                        'bola 7', 'bola 8', 'bola 9', 'bola 10', 'bola 11', 'bola 12', 'bola 13', 'bola 14', 'bola 15']]

frequencia = numeros_sorteados.apply(pd.Series.value_counts).sum(axis=1)

frequencia = frequencia.sort_values(ascending=False)

#MOSTRA A SEQUÊNCIA DOS NUMEROS SORTEADOS
print(frequencia)

#CRIAR O GRÁFICO
frequencia.plot(kind='bar', figsize=(10, 6))
plt.title('Frequência dos Numeros da Lotofácil')
plt.xlabel('numeros')
plt.ylabel('Frequência')
plt.show()
