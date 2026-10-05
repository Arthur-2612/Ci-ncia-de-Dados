import numpy as np

# Bloco 1: define uma entrada simples para um neurônio
x = np.array([0.8, 1.2, -0.4])
w = np.array([0.7, 1.1, -0.2])
b = -0.3

# Bloco 2: calcula a combinação linear antes da ativação
z = np.dot(x, w) + b

# Bloco 3: aplica a função ReLU para transformar o valor de saída
relu = max(0.0, z)

# Bloco 4: aplica a sigmoid para mostrar outra forma de ativação
sigmoid = 1 / (1 + np.exp(-z))

# Bloco 5: imprime os valores e explica o que cada um representa
print(f'Valor linear z: {z:.3f}')
print(f'ReLU(z): {relu:.3f}')
print(f'Sigmoid(z): {sigmoid:.3f}')
print('O neurônio combina entradas, aplica pesos e usa ativação para gerar uma resposta útil.')
print('Esse processo é a base da aprendizagem profunda e da modelagem de redes neurais.')
