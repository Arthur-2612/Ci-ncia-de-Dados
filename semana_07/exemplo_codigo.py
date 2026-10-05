import numpy as np
import pandas as pd

# Bloco 1: cria uma sequência de tempo mensal para simular uma série temporal
indice = pd.date_range('2024-01-01', periods=12, freq='MS')

# Bloco 2: define uma tendência linear e uma componente sazonal
base = np.linspace(100, 160, len(indice))
sazonal = np.array([5, 9, 12, 7, 5, 10, 14, 18, 13, 11, 8, 6])
serie = base + sazonal

# Bloco 3: organiza os dados em uma estrutura temporal
serie_temporal = pd.Series(serie, index=indice)
print(serie_temporal)

# Bloco 4: observa a estrutura da série e sua lógica de análise
print('A tendência mostra o movimento de longo prazo do conjunto.')
print('A sazonalidade mostra ciclos repetidos ao longo do tempo.')
print('O ruído corresponde a variações imprevisíveis que não seguem o padrão principal.')
