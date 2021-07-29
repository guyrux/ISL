# -*- coding: utf-8 -*-
class DataDescribe:
    """
    Created on Sun Jun 16 22:36:39 2019

    @author: Gustavo Suto 
    """
    import pandas as pd

    def __init__(self):
        pass


    def breve_descricao(df):
        """
        Função breve_descricao
        
        Objetivo: Exclui atributos que estejam com colunas com todos os valores
        'NaN'. Imprime na tela a quantidade de atributos/campos e a quantidade
        de registros.
        
        Args:
            df ([pandas.DataFrame]): [Dataframe que queremos analisar.]
        """
        
        df.dropna(axis=1, how="all", inplace=True)
    
        print("O data set possui: \n- {} atributos/campos; e \n- {} registros.\n".
          format(df.shape[1], df.shape[0]))
        df.info()
    
    
        
    def serie_nulos(df, corte = 0.5):
        """
        Função serie_nulos

        Responsável: Suto
        Data: 04/05/19
        
        Objetivo: essa função retorna uma tupla com:
            (1) contendo uma pd.series com os atributos com maior proporção de nulos; e
            (2) uma string indicando quantos atributos estão com uma proporção de nulos acima do corte dado.
        
        Args:
            df ([pandas.DataFrame]): [Dataframe que queremos analisar.]
            corte (int, optional): [Limite mínimo de nulos presentes em um atributo para destacar]. Default = 50.

        Returns:
            [pandas.DataFrame]: [DataFrame contendo os atributos que possuem uma proporção de nulos acima ]
        """
        
        serie = (df.isnull().sum().sort_values(ascending=False)/len(df))
        
        serie_cortada = serie[serie > corte]

        print(f"{len(serie_cortada)} atributos/features/campos possuem mais de {corte} de valores nulos.")
        
        return serie_cortada
    


    def cardinalidade(df):
        """
        responsável: suto
        data: 27/10/19
        objetivo:   essa função retorna um dataframe com os atributos não
                    numéricos e sua respectiva cardinalidade em ordem crescente. 
        Argumentos: somente 01 (um) argumento, o DataFrame que se deseja
                    analisar.
        """

        import pandas as pd
        
        df_temporario = df.select_dtypes(exclude=["float64"])

        matriz_cardialidade = []

        for i, coluna in enumerate(df_temporario.columns):
            matriz_cardialidade.append([coluna, len(df_temporario[coluna].unique()), sorted(df_temporario[coluna].unique())])

        matriz_cardialidade = pd.DataFrame(matriz_cardialidade, columns=["Atributo", "Cardinalidade", "Valores"])
        matriz_cardialidade.sort_values(by=["Cardinalidade", "Atributo"], inplace=True, ascending=True)
        
        return matriz_cardialidade



    def cardinalidade_com_descricao(df):
        """
        responsável: suto
        data: 27/10/19
        objetivo: essa função retorna dois dataframes.
            (1) O primeiro com a descrição dos atributos numéricos (int ou
            float); e
            (2) O segundo com os atributos não numéricos e sua respectiva
            cardinalidade em ordem crescente. 
        argumentos: somente 01 (um) argumento, o DataFrame que se deseja analisar.
        """

        import pandas as pd
        
        df_temporario = df.select_dtypes(exclude=["int64", "float64"])
        
        matriz_cardialidade = []

        for i, coluna in df_temporario.items():
            matriz_cardialidade.append([i, len(df_temporario[i].unique())])
            
        matriz_cardialidade = pd.DataFrame(matriz_cardialidade, columns=["Atributo", "Cardinalidade"])
        matriz_cardialidade.sort_values(by="Cardinalidade", inplace=True, ascending=True)
        
        return matriz_cardialidade.T, df.describe()
    
    
    # TODO: remover essa função e colocar isolada numa outra classe.
    def r2_ajustado(x, y, y_pred):
        """
        responsável: Suto
        data: 23/11/19
        
        r2_ajustado retorna o R² Ajustado e recebe como argumento as séries com
        o valor alvo teste e o predito.
        """

        from sklearn.metrics import r2_score
        
        n = x.shape[0]
        k = x.shape[1]
        return (1-((n-1)/(n-(k+1)))*(1-r2_score(y, y_pred)))