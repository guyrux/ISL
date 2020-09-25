# Capítulo 07 - [Indo além da linearidade](../README.md)

## Assuntos tratados no capítulo

**1. Regressão polinomial:** é uma extensão da regressão linear. Consegue ajustar dados não lineares através da adição de fatores elevados até uma determinada potência.

**2. Funções escalonadas (ou *Step functions*):** "corta" o domínio da função em *K* partes. Esses cortes tem o objetivo de ajustar o modelos por partes dentro das regiôes definidas pelos "cortes".

**3. Regressões Splines:** essas funções são uma extensão das duas anteriores (**regressões polinomiais** e **funções escalonadas**). O domínio do modelo é segmentado em *K* partes e um polinômio diferente irá ajustar-se em cada região. Outra característica importante das regressões splines são as restrições nos nós (valor onde ocorrem os "cortes").

**4. *Smoothing Splines*** (eu traduziria como *Splines suavisadoras*)**:** similar às regressões Splines, porém contêm um fator que penalisa a variabilidade da função de custo e, assim, suavisa a função.

**5. Regressões locais:** Para cada ponto do domínio, ajusta-se um modelo aos dados levando-se em conta apenas os dados próximos de um determinado ponto e estes dados terão pesos atribuidos a sua distância em relação a ponto central.
- [Ótima explicação da Leslie Myint](https://www.youtube.com/watch?v=0PQKHlwh49A&ab_channel=LeslieMyint)

**6. Modelos generalizados aditivos (GAMs):** Esse tipo de modelo é um *framework* que permite que usemos funções não lineares para cada fator/variável de entrada.

--------------------

## [Notebook com mais detalhes](./ch7_01_anotacoes.ipynb)