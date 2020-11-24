## Agrupamento

**Positivo:**

- Como o k-means funciona?
> k-means é um algoritmo de aprendizado não-supervisionado e é usado para *encontrar observações que sejam próximas* e, com isso, inferir a existência de grupos com atributos mais similares entre seus elementos.
> Para iniciar o algoritmo k-means, é necessário indicar a quantidade de grupos ou *cluters* que são esperados, essa quantidade é indicada pela letra *k* de k-means.
> Os centróides, como são chamados os pontos centrais de cada agrupamentos, são dispostos aleatoriamente no espaço n-dimensional formado pelos atributos/fatores das observações.
> E seguida, são medidas as distâncias entre todos os pontos e os *k* centróides. As observações são associadas ao centróide mais próximo. Por fim, é calculado o baricentro de cada agrupamento e o centróide é movido para esse novo ponto. Esse último passo deve ser executado até que não haja mais alteração na localização dos centróides.

- Qual o algoritmo sofreria mais com outliers: k-means ou hierárquico?
> Acredito que o **k-means** sofra mais com outliers devido a natureza da determinação do centro de cada agrupamento que é localizado na distância média de todas as observações e a média é sensível a *outliers*.

**Negativo:**

- Qual a distância é otimizada no k-means, intra-cluster ou inter-cluster?
- Qual é a diferença entre a abordagem single linkage, complete e average linkage?
- Quais são as vantagens e desvantagens de um algoritmo hierárquico como a single linkage quando comparado com o algoritmo k-means?
- Como definir o número de k no k-means?
- Comparar elbow, silhueta e silhueta simplificada.
- Qual dos hierárquicos sofre menos com outliers?

## Classificação:

**Positivo:**

- Como funciona uma árvore de decisão?
- Para que serve a poda na altura da árvore?
- Explicar a diferença entre acurácia e precisão.
- Explique como os métodos de bagging funcionam.

**Negativo:**

- Qual é a importância de fazer a seleção de variáveis? Dê um exemplo de como fazer.
- Por que nem sempre é bom utilizarmos a acurácia?
- Quando utilizamos a F1?
- Explique como os métodos de boosting funcionam.

## Regressão

**Positivo:**

- Como calcular o MSE?
- Explicar como o ElasticNet funciona.
- Explicar a diferença entre regularização L1 e L2?

**Negativo:**

- Explicar técnicas de validação cruzada.
- Como deve ser feito a escolha da função de ativação de uma rede neural?
- Explicar como o modelo SVM funciona.

## Estatística

**Positivo:**

- Como calcular média, mediana e moda?

> **Média:** somatório dos elementos de uma amostra divididos pela quantidade de elementos dessa amostra.
>
> $$ Média = \frac{1}{n}\sum_{i=1}^nx_{i} $$
>
>---
>
> **Mediana:** elemento central de uma amostra. Quando os elementos são colocados em ordem crescente ou decrescente, a mediana é o elemento central, no caso de uma quantidade ímpar de amostras e é a média dos dois elementos centrais se a amostra tiver uma quantidade de elementos par.
> **Importante:** A mediana é mais robusta que a média quanto a presença de outliers.
>
>---
>
> **Moda:** simplesmente o elemento com maior de ocorrência na amostra.
>
>---

**Negativo:**

- Qual é a diferença entre a amostragem por conglomerado e a estratificada? Nesse tipo de amostragem, os conglomerados devem ser homogêneos ou heterogêneos?
- Como calcular o desvio padrão?

> O desvio padrão é uma medida de dispersão que mostra quanto os elementos estão distantes da média da amostra. Quanto mais próximo de 0, menos disperso é a amostra.
> $$ \sigma = \sqrt{\frac{\sum_{i=1}^n(x_{i}-\bar{x})}{n}} $$
> Importante que a variâcia é o quadrado do desvio padrão.

## SQL

**Positivo:**

- Qual é a diferença entre inner join e left join?
- Dê um exemplo de uma situação na qual podemos usar a cláusula *group by*.

**Negativo:**

- Suponha que precisamos fazer uma junção (JOIN) de duas tabelas muito grandes. Como podemos acelerar o processo?