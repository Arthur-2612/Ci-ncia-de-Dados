import numpy as np
from scipy.stats import shapiro

# Bloco 1: gera uma amostra seguindo distribuição normal
np.random.seed(42)
amostra = np.random.normal(loc=10, scale=2, size=500)

# Bloco 2: aplica o teste de Shapiro para verificar normalidade da amostra
estatistica, p_valor = shapiro(amostra)

# Bloco 3: imprime o valor do teste e do p-valor
print(f'Estatística do teste: {estatistica:.4f}')
print(f'p-valor: {p_valor:.4f}')

# Bloco 4: define a regra de decisão estatística
if p_valor > 0.05:
    print('Não rejeitamos a hipótese de normalidade.')
else:
    print('Rejeitamos a hipótese de normalidade.')

# Bloco 5: reforça a interpretação dos resultados
print('Um p-valor baixo indica evidência contra a hipótese nula.')
print('Mas a decisão também depende do contexto e da qualidade da amostra.')
