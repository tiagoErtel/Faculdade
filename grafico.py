# RU: 3922907

import numpy as np
import plotly.graph_objects as go

a = 3
b = 9
c = 2

# Gerar vetor aleatório de tamanho 10
x = np.random.rand(10)

# Calcular os valores de y
y = a*x + b*x - c

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y,mode='lines', name='função linear'))
fig.update_layout(title = "função linear",
                  xaxis_title = "x",
                  yaxis_title = "y")
fig.show()
