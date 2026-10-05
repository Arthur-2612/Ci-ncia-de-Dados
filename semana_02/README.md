# Semana 02 — Métricas de Avaliação e Distribuições Estatísticas

## Visão geral do notebook
Esta semana foca em como avaliar se um modelo está funcionando bem. O notebook mostra que não basta dizer que o algoritmo “acertou muito”; é necessário entender que tipo de erro importa e qual métrica precisa ser usada para o problema real.

### Em poucas palavras
A aula explica:
- matriz de confusão;
- precisão, recall e F1-score;
- acurácia e seus limites;
- ROC e ROC-AUC;
- distribuições estatísticas e como elas afetam os dados.

## O que aparece no notebook
1. Verdadeiro positivo, falso positivo, falso negativo e verdadeiro negativo.
2. Situações em que acurácia pode esconder problemas.
3. Como interpretar aplicações com dados desbalanceados.
4. Como a curva ROC representa a separação entre classes.
5. Como diferentes distribuições influenciam o comportamento dos dados.

## Conceitos mais importantes
- Precisão: entre tudo o que o modelo previu como positivo, quantos realmente eram positivos.
- Recall: entre todos os casos positivos reais, quantos o modelo conseguiu capturar.
- F1-score: equilíbrio entre precisão e recall.
- ROC-AUC: capacidade geral do modelo em distinguir classes.

## Como ler esse notebook de forma simples
Os gráficos e as métricas devem ser lidos como indicadores de qualidade de decisão. Se o problema envolve risco, pode ser mais importante capturar o evento relevante do que ter um número de acerto bruto alto.

## Conclusão didática
A aula ensina que um modelo é bom quando serve ao objetivo do problema. A métrica certa é a que responde à pergunta correta, não a que parece mais bonita na tela.

### Arquivos da semana
- Notebook: [semana_02.ipynb](semana_02.ipynb)
- Exemplo prático: [exemplo_codigo.py](exemplo_codigo.py)
