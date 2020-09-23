# Capítulo 07 - [Indo além da linearidade](../README.md)

## Assuntos tratados no capítulo

**1. Regressão polinomial:** é uma extensão da regressão linear. Consegue ajustar dados não lineares através da adição de fatores elevados até uma determinada potência.

**2. Funções escalonadas (ou *Step functions*):** "corta" o domínio da função em *K* partes. Esses cortes tem o objetivo de ajustar o modelos por partes dentro das regiôes definidas pelos "cortes".

**3. Regressões Splines:** essas funções são uma extensão das duas anteriores (**regressões polinomiais** e **funções escalonadas**). O domínio do modelo é segmentado em *K* partes e um polinômio diferente irá ajustar-se em cada região. Outra característica importante das regressões splines são as restrições nos nós (valor onde ocorrem os "cortes").

**4. *Smoothing Splines*** (eu traduziria como *Splines suavisadoras*)**:** similar às regressões Splines, porém contêm um fator que penalisa a variabilidade da função de custo e, assim, suavisa a função.

**5. Regressões locais:** Para cada ponto do domínio, ajusta-se um modelo aos dados levando-se em conta apenas os dados próximos de um determinado ponto e estes dados terão pesos atribuidos a sua distância em relação a ponto central.

**6. Modelos generalizados aditivos (GAMs):** Esse tipo de modelo é um *framework* que permite que usemos funções não lineares para cada fator/variável de entrada.

--------------------
## Regressão polinomial
Como podemos ver na equação abaixo, a equação generalizada da regressão polinomial é só uma extensão da regressão linear simples.

$$
y_{i} = \beta_{0} + \beta_{1}x_{i}^1 + \beta_{2}x_{i}^2 + ... + \beta_{d}x_{i}^d + \epsilon_{i}
\tag{1}
$$

O mesmo pode ser estendido para problemas de classificação. No livro (p.268), temos como exemplo a **regressão logística**:

$$
Pr(y_{i}>250|x_{i}) = \frac{exp(\beta_{0} + \beta_{1}x_{i}^1 + \beta_{2}x_{i}^2 + ... + \beta_{d}x_{i}^d)}{1+exp(\beta_{0} + \beta_{1}x_{i}^1 + \beta_{2}x_{i}^2 + ... + \beta_{d}x_{i}^d)}
\tag{2}
$$

Um ponto que não encontrei no texto ou nas aulas, mas acredito que devemos levar em conta para alguns problemas é quando o modelo leva em conta mais de um fator/variável de entrada e há gostaríamos de verificar se a interação entre os fatores é impactante ou não.

--------------------
## Funções escalonadas (ou *Step functions*)



--------------------
## Regressões Splines



--------------------
## *Smoothing Splines*** (eu traduziria como *Splines suavisadoras*)



--------------------
## Regressões locais

[Ótima explicação da Leslie Myint](https://www.youtube.com/watch?v=0PQKHlwh49A&ab_channel=LeslieMyint).

--------------------
## Modelos generalizados aditivos (GAMs)

