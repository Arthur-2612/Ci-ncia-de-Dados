from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Bloco 1: gera um conjunto sintético para simular um problema de classificação
X, y = make_classification(
    n_samples=200,
    n_features=10,
    n_informative=5,
    n_redundant=2,
    random_state=42,
)

# Bloco 2: define o modelo com árvores e balanceamento de classe
modelo = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight='balanced'
)

# Bloco 3: treina o classificador usando os dados simulados
modelo.fit(X, y)
acuracia = modelo.score(X, y)

# Bloco 4: observa o nível de acerto do modelo na base de treino
print(f'Acurácia no treino: {acuracia:.3f}')

# Bloco 5: extrai as importâncias das variáveis para interpretar a decisão
importancia = modelo.feature_importances_
print('Importância das primeiras variáveis:', importancia[:5])

# Bloco 6: reforça a ideia de que a variável mais importante depende do contexto do problema
print('A importância das variáveis mostra quais atributos mais influenciaram a decisão do modelo.')
print('Isso ajuda a explicar o resultado e a gerar confiança na análise.')
