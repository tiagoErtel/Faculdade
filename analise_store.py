# RU: 3922907

import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('Stores.csv')

# Renomear as colunas
df = df.rename(columns={
    'Daily_Customer_Count': 'Visitantes',
    'Items_Available': 'Itens Disponíveis',
    'Store_Sales': 'Vendas da Loja'
})

# Calcular os valores estatísticos
items_min  = df['Itens Disponíveis'].min()
items_max  = df['Itens Disponíveis'].max()
items_mean = df['Itens Disponíveis'].mean()
items_std  = df['Itens Disponíveis'].std()

customers_min  = df['Visitantes'].min()
customers_max  = df['Visitantes'].max()
customers_mean = df['Visitantes'].mean()
customers_std  = df['Visitantes'].std()

sales_min  = df['Vendas da Loja'].min()
sales_max  = df['Vendas da Loja'].max()
sales_mean = df['Vendas da Loja'].mean()
sales_std  = df['Vendas da Loja'].std()

# Criar os gráficos
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.scatter(df.index, df['Itens Disponíveis'], color='blue')
plt.xlabel('Loja')
plt.ylabel('Itens Disponíveis')
plt.title('Itens Disponíveis')

plt.subplot(1, 3, 2)
plt.scatter(df.index, df['Visitantes'], color='green')
plt.xlabel('Loja')
plt.ylabel('Visitantes')
plt.title('Visitantes Diários')

plt.subplot(1, 3, 3)
plt.scatter(df.index, df['Vendas da Loja'], color='red')
plt.xlabel('Loja')
plt.ylabel('Vendas da Loja')
plt.title('Vendas da Loja')

plt.tight_layout()
plt.show()
