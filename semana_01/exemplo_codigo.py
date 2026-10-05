import numpy as np

# Bloco 1: define os custos dos erros para mostrar por que a métrica importa
CUSTO_FALSO_NEGATIVO = 10000.0
CUSTO_FALSO_POSITIVO = 600.0

# Bloco 2: cenário sem apoio de modelo
fn_sem_modelo = 200
fp_sem_modelo = 0
custo_sem_modelo = fn_sem_modelo * CUSTO_FALSO_NEGATIVO + fp_sem_modelo * CUSTO_FALSO_POSITIVO

# Bloco 3: cenário com um modelo mais conservador
fn_com_modelo = 30
fp_com_modelo = 60
custo_com_modelo = fn_com_modelo * CUSTO_FALSO_NEGATIVO + fp_com_modelo * CUSTO_FALSO_POSITIVO

# Bloco 4: calcula a economia gerada pela decisão mais inteligente
reduzido = custo_sem_modelo - custo_com_modelo

# Bloco 5: imprime os números e reforça a ideia de que o contexto do problema define a métrica adequada
print(f"Custo sem modelo: R$ {custo_sem_modelo:,.2f}")
print(f"Custo com modelo: R$ {custo_com_modelo:,.2f}")
print(f"Economia gerada: R$ {reduzido:,.2f}")
print("A análise correta depende do problema e dos custos reais do erro.")

# Bloco 6: percebe-se que acurácia simples nem sempre indica melhor decisão
print("A métrica ideal depende da consequência operacional do erro.")
