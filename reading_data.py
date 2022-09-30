from avaliador_api import define_sentimento


def gerando_df(coluna, df):

    # dropando colunas vazias
    series = df[coluna]
    series.dropna(inplace=True)
    df = series.to_frame()

    # removendo colunas com uma string vazia
    df[coluna] = df[coluna].apply(lambda x: x.strip() if type(x) == str else x)
    df_remover = df.loc[df[coluna] == '']
    df.drop(df_remover.index, inplace=True)
    
    # corrigindo index
    df.reset_index(drop=True, inplace=True)

    # passando valores para a API
    df['resultado_api'] = df[coluna].apply(lambda x: define_sentimento(x))
    
    # separando emoção e sentimento em colunas diferentes
    df['emotions'] = df['resultado_api'].apply(lambda x: x['emotions'])
    df['sentiment'] = df['resultado_api'].apply(lambda x: x['sentiment'])
    
    # seperando as informações de sentimento em colunas
    df['sentiment_score'] = df['sentiment'].apply(lambda x: x['score'])
    df['felling'] = df['sentiment'].apply(lambda x: x['label'])
    
    # seperando as emoções
    df['sadness'] = df['emotions'].apply(lambda x: x['sadness'])
    df['joy'] = df['emotions'].apply(lambda x: x['joy'])
    df['fear'] = df['emotions'].apply(lambda x: x['fear'])
    df['disgust'] = df['emotions'].apply(lambda x: x['disgust'])
    df['anger'] = df['emotions'].apply(lambda x: x['anger'])

    # dropando que contem os dicionarios 
    df.drop(['emotions', 'sentiment', 'resultado_api'], inplace=True, axis=1)
    
    return df
