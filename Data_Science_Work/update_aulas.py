from pathlib import Path

root = Path(__file__).resolve().parent

weeks = {
    "semana_01": {
        "readme": """# Semana 01 — Fundamentos de Estatística e a Metodologia CRISP-DM

## Objetivo da aula

A primeira aula estabelece a base teórica da disciplina. O foco não é apenas memorizar fórmulas, mas entender como a estatística, a qualidade dos dados e a estrutura do problema influenciam a análise e a tomada de decisão em Ciência de Dados.

## Resumo completo

A semana começa com conceitos fundamentais de estatística descritiva: população, amostra, média, mediana, moda, variância, desvio padrão, quartis e percentis. Esses conceitos ajudam a descrever padrões, dispersão e centralidade dos dados. Em seguida, a aula introduz escalas de medida — nominal, ordinal, intervalar e de razão — para mostrar que o tipo de variável define o tipo de análise que será possível fazer.

Também foi apresentado o ciclo CRISP-DM, que organiza o projeto em seis fases: entendimento do negócio, entendimento dos dados, preparação dos dados, modelagem, avaliação e implementação. Esse framework é importante porque mostra que Ciência de Dados não é só modelar; é resolver um problema real com rigor técnico e alinhamento estratégico.

A aula reforça ainda a ideia de que decisões de negócio envolvem custos e riscos. Em cenários de crédito, por exemplo, um falso negativo pode custar muito mais que um falso positivo. Isso mostra por que a escolha de métricas no problema correto é tão importante.

## Tópicos principais

- Estatística descritiva
- População, amostra e representatividade
- Média, mediana, moda e dispersão
- Escalas de medida
- CRISP-DM e fases do projeto
- Custos e riscos em decisões analíticas

## O que um aluno deve levar

- Entender que dados sem contexto podem levar a conclusões falsas.
- Reconhecer que cada tipo de variável exige uma forma diferente de análise.
- Compreender que projeto de dados deve ser lido como um ciclo e não como uma tarefa isolada.

## Material

- Notebook: [semana_01.ipynb](semana_01.ipynb)
- Exemplo prático: [exemplo_codigo.py](exemplo_codigo.py)
""",
        "code": """import numpy as np

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
"""
    },
    "semana_02": {
        "readme": """# Semana 02 — Métricas de Avaliação e Distribuições Estatísticas

## Objetivo da aula

A segunda aula conecta teoria estatística e avaliação de modelos. O ponto principal é entender como mensurar o desempenho de um classificador e como interpretar a distribuição dos dados antes de tomar decisão.

## Resumo completo

A aula introduz a matriz de confusão e mostra como ela organiza os erros e acertos de um modelo. São apresentados os termos verdadeiro positivo, falso positivo, verdadeiro negativo e falso negativo. A partir disso, surgem indicadores fundamentais: acurácia, precisão, recall e F1-score. O professor costuma enfatizar que a acurácia pode ser enganosa em um problema desbalanceado, porque um modelo que sempre prevê a classe majoritária pode parecer ótimo sem realmente resolver o problema.

Em seguida, a aula apresenta a curva ROC e a área sob essa curva, conhecida como ROC-AUC. Essa métrica ajuda a avaliar a capacidade do modelo de separar corretamente as classes. A discussão de distribuições estatísticas também entra em cena: normal, uniforme e Poisson. A ideia é perceber que os dados não têm a mesma estrutura e que isso influencia a forma como o problema deve ser tratado.

A prática com simulações em NumPy reforça a ideia de que a variabilidade é natural e precisa ser interpretada, não ignorada. Em projetos reais, uma distribuição diferente pode sugerir comportamento distinto de clientes, eventos, erros ou comportamentos de mercado.

## Tópicos principais

- Matriz de confusão
- Precisão, recall e F1-score
- ROC e ROC-AUC
- Dados desbalanceados
- Distribuição normal e outras distribuições
- Simulação estatística

## O que um aluno deve levar

- Entender que não existe uma métrica universal.
- Reconhecer que a classe relevante pode exigir foco em recall ou precisão.
- Perceber que a distribuição dos dados é parte do desenho do modelo.

## Material

- Notebook: [semana_02.ipynb](semana_02.ipynb)
- Exemplo prático: [exemplo_codigo.py](exemplo_codigo.py)
""",
        "code": """import numpy as np
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

# Bloco 1: define rótulos reais e previsões simuladas para demonstrar avaliação
v_real = np.array([0, 0, 0, 0, 1, 1, 1, 1])
v_pred = np.array([0, 1, 0, 0, 1, 1, 0, 1])

# Bloco 2: calcula a matriz de confusão, que organiza acertos e erros do modelo
matriz = confusion_matrix(v_real, v_pred)
print("Matriz de confusão:\n", matriz)

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
"""
    },
    "semana_03": {
        "readme": """# Semana 03 — EDA Avançada e Preparação dos Dados

## Objetivo da aula

A terceira aula enfatiza a análise exploratória de dados e a preparação da base. Antes de qualquer modelagem, é essencial entender o conjunto, detectar inconsistências e decidir como tratar ruídos e colunas problemáticas.

## Resumo completo

A análise exploratória (EDA) é o momento em que o analista pergunta: o que os dados estão dizendo? Quais valores parecem inconsistentes? O que precisa ser corrigido antes de treinar um modelo? A aula mostra como estatísticas descritivas e gráficos ajudam a identificar outliers, distribuições incomuns e padrões relevantes.

São discutidos boxplots, quartis, correlação e comportamento geral das variáveis. Essa etapa não é só visual; ela define a qualidade da base. Um valor extremo, uma coluna com muitos dados faltantes ou uma entrada inválida pode afetar completamente a modelagem.

Em seguida, a aula trata da preparação dos dados: imputação, normalização, codificação, seleção de atributos e descarte de informações inconsistentes. Essa etapa é crítica, porque um modelo não é melhor apenas por ter mais dados; ele é melhor quando os dados têm consistência e contexto adequados.

## Tópicos principais

- EDA e análise exploratória
- Outliers e valores anômalos
- Correlação entre variáveis
- Tratamento de dados faltantes
- Preparação e limpeza de dados
- Impacto da qualidade de dados no modelo

## O que um aluno deve levar

- Entender que não há modelagem eficiente sem boa preparação dos dados.
- Reconhecer padrões suspeitos antes de qualquer treino.
- Reconhecer que EDA é etapa analítica e não uma etapa opcional.

## Material

- Notebook: [semana_03.ipynb](semana_03.ipynb)
- Exemplo prático: [exemplo_codigo.py](exemplo_codigo.py)
""",
        "code": """import pandas as pd
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
"""
    },
    "semana_04": {
        "readme": """# Semana 04 — CRISP-DM: Modelagem e Avaliação Financeira

## Objetivo da aula

A quarta aula entra na fase de modelagem do CRISP-DM. Agora, os dados deixam de ser apenas observados e passam a ser convertidos em previsões e decisões orientadas por valor.

## Resumo completo

A fase de modelagem é a etapa em que se escolhe um algoritmo para aprender padrões a partir dos dados. A aula apresenta a Random Forest, um modelo de ensemble que combina várias árvores de decisão. Essa estratégia reduz a variância de previsões individuais e geralmente oferece maior robustez.

Além disso, a Random Forest permite interpretar a importância das variáveis. Isso é importante porque a análise não é apenas prever um resultado; é entender o que mais influenciou a decisão. Em problemas de crédito, por exemplo, a renda, o histórico de atraso e o score podem variar em importância dependendo do conjunto e da regra de negócio.

A aula também conecta a avaliação técnica com a dimensão financeira. Um modelo bom não é apenas aquele que acerta mais; é aquele que reduz perdas, melhora decisões e gera valor. Isso mostra que as métricas precisam estar alinhadas ao objetivo do negócio.

## Tópicos principais

- Random Forest
- Ensemble learning
- Importância de variáveis
- Treinamento e validação
- Avaliação financeira e técnica
- Valor gerado pelo modelo

## O que um aluno deve levar

- Entender que a modelagem é uma etapa do processo e não o fim dele.
- Perceber que a variável importante é a que tem maior valor para o problema.
- Relacionar desempenho técnico com retorno financeiro ou redução de risco.

## Material

- Notebook: [semana_04.ipynb](semana_04.ipynb)
- Exemplo prático: [exemplo_codigo.py](exemplo_codigo.py)
""",
        "code": """from sklearn.ensemble import RandomForestClassifier
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
"""
    },
    "semana_05": {
        "readme": """# Semana 05 — Inferência Estatística e Testes de Hipóteses

## Objetivo da aula

A quinta aula introduz a inferência estatística, permitindo que o aluno vá além de descrever dados e passe a testar se uma observação é realmente relevante ou se pode ter acontecido por acaso.

## Resumo completo

A inferência estatística usa amostras para dizer algo sobre a população. A aula explica a diferença entre hipótese nula e hipótese alternativa, além de introduzir o p-valor. Essa medida indica a probabilidade de observar um resultado tão extremo quanto o observado, assumindo que a hipótese nula é verdadeira.

O conceito de erro tipo I e erro tipo II também é apresentado. O primeiro é rejeitar a hipótese nula quando ela era verdadeira; o segundo é não rejeitar quando deveria rejeitar. Essa discussão é importante porque estatística não é certeza absoluta, mas um processo de tomada de decisão sob incerteza.

Além disso, a aula revisita a distribuição normal e mostra como ela serve como referência para testes de normalidade e comparações entre grupos. Esse raciocínio prepara o aluno para interpretar estudos, experimentos e relatórios de dados de forma mais crítica.

## Tópicos principais

- Inferência estatística
- Hipótese nula e alternativa
- p-valor
- Erros tipo I e II
- Distribuição normal
- Testes de hipóteses

## O que um aluno deve levar

- Entender que estatística leva em conta incerteza, não certeza absoluta.
- Saber que significância e efeito prático não são a mesma coisa.
- Reconhecer que conclusão estatística deve ser interpretada com cautela e contexto.

## Material

- Notebook: [semana_05.ipynb](semana_05.ipynb)
- Exemplo prático: [exemplo_codigo.py](exemplo_codigo.py)
""",
        "code": """import numpy as np
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
"""
    },
    "semana_06": {
        "readme": """# Semana 06 — Acompanhamento do Projeto Integrador e Revisão

## Objetivo da aula

A sexta semana funciona como base de revisão e acompanhamento do projeto integrador. A ideia é consolidar praticamente todos os conceitos aprendidos e verificar se o aluno consegue conectar o método com a prática.

## Resumo completo

Ao longo da disciplina, o aluno já teve contato com estatística, EDA, métricas, modelos e inferência. Agora, a aula organiza esse conhecimento em um fluxo mais completo. O projeto integrador é usado como eixo para aplicar a lógica do CRISP-DM em um cenário real ou semireal.

A revisão enfatiza que os projetos de dados são iterativos. É comum precisar voltar para limpeza, ajustar variáveis, trocar métricas ou reformular a abordagem. Isso mostra que análise de dados não é um processo linear e perfeito, mas um ciclo de refinamento orientado por evidência.

## Tópicos principais

- Revisão do CRISP-DM
- Projeto integrador
- Organização do fluxo do projeto
- Ajuste iterativo
- Interpretação dos resultados

## O que um aluno deve levar

- Entender que projetos reais exigem refinamento constante.
- Apreciar a importância da organização e da documentação.
- Reconhecer que análise e decisão são etapas integradas, não sequências artificiais.

## Material

- Notebook: [semana_06.ipynb](semana_06.ipynb)
- Exemplo prático: [exemplo_codigo.py](exemplo_codigo.py)
""",
        "code": """# Bloco 1: descreve a sequência lógica do trabalho de análise
passos = [
    'entender o problema de negócio',
    'coletar e organizar os dados',
    'explorar a base e identificar inconsistências',
    'preparar as variáveis',
    'treinar e avaliar o modelo',
    'comunicar os resultados com contexto'
]

# Bloco 2: percorre a lista para reforçar a ordem do fluxo analítico
for passo in passos:
    print(f'- {passo}')

# Bloco 3: reforça a ideia de que o trabalho é iterativo
print('Em projetos reais, a primeira hipótese pode estar incorreta; ajuste e validação são parte do processo.')
print('O ciclo da análise é uma ferramenta de aprendizado e melhoria contínua.')
"""
    },
    "semana_07": {
        "readme": """# Semana 07 — Análise de Séries Temporais

## Objetivo da aula

A sétima aula introduz um tipo de dado em que a ordem temporal é essencial. Séries temporais exigem atenção à evolução no tempo e não podem ser tratadas como uma coleção de registros independentes.

## Resumo completo

A análise de séries temporais trabalha com observações indexadas no tempo, como vendas mensais, temperatura diária, demanda de energia ou preços de ativos. A aula mostra que o valor presente depende em parte do passado e que padrões podem se repetir ao longo do tempo.

Os principais componentes de uma série temporal são tendência, sazonalidade e ruído. A tendência representa o movimento de longo prazo; a sazonalidade representa ciclos recorrentes; o ruído representa flutuações aleatórias e imprevisíveis. Essa decomposição ajuda a interpretar melhor o comportamento do dado e a construir previsões mais coerentes.

Também são discutidos métodos de suavização, como média móvel e suavização exponencial. Esses recursos ajudam a diminuir ruído e identificar padrões mais estáveis. Essa é uma etapa importante para monitoramento, previsão e tomada de decisão em contextos dinâmicos.

## Tópicos principais

- Séries temporais
- Tendência e sazonalidade
- Ruído e decomposição
- Média móvel
- Suavização exponencial
- Tomada de decisão com dados temporais

## O que um aluno deve levar

- Entender que tempo é informação, não apenas contexto.
- Identificar padrões temporais ao invés de tratar dados como independentes.
- Reconhecer a importância da ordenação e da decomposição temporal.

## Material

- Notebook: [semana_07.ipynb](semana_07.ipynb)
- Exemplo prático: [exemplo_codigo.py](exemplo_codigo.py)
""",
        "code": """import numpy as np
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
"""
    },
    "semana_08": {
        "readme": """# Semana 08 — Revisão e Prova 1

## Objetivo da aula

A semana 08 tem caráter de revisão geral, reunindo os principais conteúdos do primeiro bloco da disciplina e preparando o aluno para a primeira avaliação formal.

## Resumo completo

A revisão abrange estatística descritiva, amostragem, CRISP-DM, EDA, medidas de avaliação e séries temporais. O objetivo é consolidar o raciocínio e reforçar o entendimento de que os conceitos se conectam, e não aparecem isoladamente.

A prova exige mais do que memorização: a estudante precisa saber interpretar, explicar e justificar escolhas. Isso inclui reconhecer as métricas corretas para cada problema e compreender por que a etapa de análise exploratória é essencial antes do treinamento.

## Tópicos principais

- Revisão de estatística
- CRISP-DM
- EDA
- Métricas e avaliação
- Séries temporais
- Estratégia de estudos

## O que um aluno deve levar

- Entender a lógica global da disciplina.
- Relacionar cada etapa da análise com o objetivo do problema.
- Desenvolver capacidade de explicação e justificativa analítica.

## Material

- Notebook: [semana_08.ipynb](semana_08.ipynb)
- Exemplo prático: [exemplo_codigo.py](exemplo_codigo.py)
""",
        "code": """# Bloco 1: revisa os principais temas da etapa inicial da disciplina
conteudos = [
    'estatística descritiva',
    'amostragem e escalas',
    'CRISP-DM',
    'EDA',
    'métricas de avaliação',
    'séries temporais'
]

# Bloco 2: percorre a lista para reforçar cada tópico revisado
for tema in conteudos:
    print(f'- {tema}')

# Bloco 3: reforça que a revisão precisa conectar teoria e prática
print('A prova não testa apenas memorização; testa capacidade de raciocinar sobre dados e decisões.')
print('A clareza de interpretação é tão importante quanto a técnica aplicada.')
"""
    },
    "semana_09": {
        "readme": """# Semana 09 — Consolidação do Projeto Integrador

## Objetivo da aula

A nona semana é dedicada à consolidação do projeto integrador, reunindo os conhecimentos aplicados em análise, limpeza, interpretação e apresentação dos resultados.

## Resumo completo

A consolidação do projeto exige uma revisão crítica da base de dados, do problema de negócio, das decisões de limpeza e da metodologia aplicada. Nessa etapa, o aluno precisa verificar se a análise está alinhada ao objetivo enunciado e se as conclusões têm sustentação trazida pela evidência dos dados.

A aula reforça a ideia de que o valor de um projeto não está apenas na execução do código, mas também na capacidade de conectar os resultados à pergunta correta. O analista precisa saber o que quer responder, como chegou a essa resposta e como comunicar isso de forma clara para quem vai decidir.

## Tópicos principais

- Projeto integrador
- Revisão da base
- Qualidade dos dados
- Preparação e validação
- Interpretação de conclusões
- Comunicação analítica

## O que um aluno deve levar

- Entender que um projeto é medido pela qualidade da resposta ao problema.
- Reconhecer que cada etapa da pipeline deve ter justificativa técnica e de negócio.
- Perceber que comunicação clara é parte essencial da análise.

## Material

- Notebook: [semana_09.ipynb](semana_09.ipynb)
- Exemplo prático: [exemplo_codigo.py](exemplo_codigo.py)
""",
        "code": """# Bloco 1: lista os principais passos da revisão de um projeto
etapas = [
    'validar a qualidade dos dados',
    'revisar a variável alvo',
    'identificar outliers e inconsistências',
    'aplicar limpeza e preparação',
    'treinar e avaliar modelos',
    'apresentar resultados com contexto'
]

# Bloco 2: imprime a sequência para reforçar a lógica do projeto
for etapa in etapas:
    print(f'- {etapa}')

# Bloco 3: conclui com a mensagem central da semana
print('O projeto ganha valor quando a análise é coerente, bem explicada e orientada por um objetivo real.')
print('O resultado técnico precisa ser entendido como decisão de negócio, não como métrica isolada.')
"""
    },
    "semana_10": {
        "readme": """# Semana 10 — Da Random Forest às Redes Neurais

## Objetivo da aula

A décima semana introduz a ideia de redes neurais e mostra como elas se relacionam com os modelos que já foram vistos, como a Random Forest. O objetivo é compreender a lógica matemática por trás do aprendizado e a importância da preparação do dado.

## Resumo completo

A aula inicia comparando árvores de decisão com redes neurais. Enquanto a Random Forest combina decisões de várias árvores, a rede neural realiza transformações matemáticas em sequência, combinando entradas ponderadas, bias e funções de ativação. O neurônio é a unidade básica do aprendizado, operando como um processador que recebe sinais, combina valores e produz uma saída.

São introduzidos os conceitos de pesos, bias, camadas, ativação e treinamento. A função de ativação, como ReLU e sigmoid, permite que a rede introduza não-linearidade no processo, capturando relações mais complexas entre as variáveis. A aula também ressalta que dados com escalas muito diferentes podem prejudicar o aprendizado e que normalização costuma ser uma etapa necessária.

A comparação com modelos clássicos reforça a ideia de que cada abordagem tem uma lógica própria. A importância do ajuste de pesos e da otimização continua é central para a compreensão de redes neurais e de aprendizagem profunda.

## Tópicos principais

- Redes neurais
- Neurônios, pesos e bias
- Funções de ativação
- Camadas e arquitetura
- Normalização e escala
- Comparação com Random Forest

## O que um aluno deve levar

- Entender que redes neurais são sequências de transformações matemáticas e não “caixas pretas” incompreensíveis.
- Reconhecer a importância de normalização e preparação dos dados.
- Saber que o treinamento é um processo de ajustes sucessivos ao erro do modelo.

## Material

- Notebook: [semana_10.ipynb](semana_10.ipynb)
- Exemplo prático: [exemplo_codigo.py](exemplo_codigo.py)
""",
        "code": """import numpy as np

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
"""
    }
}

for name, data in weeks.items():
    folder = root / name
    folder.mkdir(exist_ok=True)
    (folder / 'README.md').write_text(data['readme'], encoding='utf-8')
    (folder / 'exemplo_codigo.py').write_text(data['code'], encoding='utf-8')
    print(f'Atualizado: {folder}')

print('Processo concluído: resumos completos e exemplos comentados foram registrados em todas as semanas.')
