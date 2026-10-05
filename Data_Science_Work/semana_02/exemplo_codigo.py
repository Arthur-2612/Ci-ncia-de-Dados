import numpy as np
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

# Bloco 1: define rótulos reais e previsões simuladas para demonstrar avaliação
v_real = np.array([0, 0, 0, 0, 1, 1, 1, 1])
v_pred = np.array([0, 1, 0, 0, 1, 1, 0, 1])

# Bloco 2: calcula a matriz de confusão, que organiza acertos e erros do modelo
matriz = confusion_matrix(v_real, v_pred)
print("Matriz de confusão:
", matriz)

# Bloco 3: mede precisão, recall e F1 para a classe positiva
precisao = precision_score(v_real, v_pred)
recall = recall_score(v_real, v_pred)
f1 = f1_score(v_real, v_pred)

# Bloco 4: imprime cada indicador separadamente para facilitar a leitura
print(f"Precisão: {precisao:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-score: {f1:.2f}")

# Bloco 5: explica por que a escolha da métrica impacta a decisão
print("Se o problema envolve risco, o recall costuma ser mais decisivo do que a acurácia simples.")
print("Isso mostra que não basta olhar um número isolado; é preciso saber qual evento importa.")
