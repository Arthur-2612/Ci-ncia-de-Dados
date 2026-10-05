import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Bloco 1: carrega a base de dados para começar a análise exploratória
base = pd.read_csv('semana_03/materiais/CRISP_DM_Random_Forest_Credito.csv')

# Bloco 2: observa a estrutura básica do conjunto para confirmar colunas e tipos
print(base.head())
print(base.dtypes)

# Bloco 3: cria um boxplot para encontrar valores extremos na variável idade
sns.boxplot(data=base, x='idade')
plt.title('Boxplot da variável idade')
plt.show()

# Bloco 4: calcula estatísticas descritivas para ver tendência central e dispersão
resumo = base[['idade', 'renda_mensal', 'score_serasa']].describe()
print(resumo)

# Bloco 5: analisa a presença de valores inconsistentes na base
print('Quantidade de valores nulos:', base.isnull().sum().sum())
print('Se houver outliers ou inconsistências, a preparação deve tratá-los antes do treino.')
print('A qualidade da base define a qualidade da resposta do modelo.')
