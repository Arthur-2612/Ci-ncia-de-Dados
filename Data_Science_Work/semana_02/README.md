# Semana 02 — Métricas de Avaliação e Distribuições Estatísticas

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
