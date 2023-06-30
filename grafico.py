import numpy as np
import matplotlib.pyplot as plt

# Obter os valores de a, b e c
a = 3
b = 9
c = 2

# Criar vetor aleatório de tamanho 10 para x
x = np.random.rand(10)

# Calcular os valores de y
y = a * x + b * x - c

# Gerar uma sequência de cores para cada ponto
cores = np.arange(len(x))

# Plotar os pontos no gráfico com cores diferentes
plt.scatter(x, y, c=cores, cmap='rainbow', label='Pontos')

# Configurar o gráfico
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Exibir o gráfico
plt.show()
