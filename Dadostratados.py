import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

#importando base de daos
Base_dados_filmes = pd.read_csv(r"C:\Users\pmari\PycharmProjects\RecomendacaodeFilmes\sistema_recomendacao/movies_metadata.csv",
                                low_memory=False)
pd.set_option('display.max_columns', None)
avaliacoes = pd.read_csv(r"C:\Users\pmari\PycharmProjects\RecomendacaodeFilmes\sistema_recomendacao/ratings.csv")

#Tratando dados da base dos filmes
Base_dados_filmes = Base_dados_filmes[['id','original_title','original_language','vote_count']]

Base_dados_filmes.rename(columns={'id':'ID_FILME','original_title':'TITULO','original_language':'LINGUAGEM','vote_count':'QT_AVALIACOES'},inplace=True)
Base_dados_filmes.dropna(inplace=True)

#Tratando dados da base doas avaliacoes

avaliacoes = avaliacoes [['userId','movieId','rating']]
avaliacoes.rename(columns={'userId':'ID_USUARIO','movieId':'ID_FILME','rating':'AVALIACAO'},inplace=True)
avaliacoes.dropna(inplace=True)

#Filtrando apenas os usuarios com mais de 999 avaliacoes
qt_avaliacoes = avaliacoes['ID_USUARIO'].value_counts() > 999
y = qt_avaliacoes[qt_avaliacoes].index

#Atualizando base 'avaliacoes' com apenas os uduarios que tiveram mais de 999 avaliacoes
avaliacoes = avaliacoes[avaliacoes['ID_USUARIO'].isin(y)]

#Atualizando base 'Base_dados_filmes' com apenas AS AVAOLIACOES Mais de 999
Base_dados_filmes = Base_dados_filmes[Base_dados_filmes['QT_AVALIACOES'] > 999]

#Entendendo quantos filmes tem em cada lingua
filmes_linguagem = Base_dados_filmes['LINGUAGEM'].value_counts()

#atualizando a abse apenas com filmes em ingles
Base_dados_filmes = Base_dados_filmes[Base_dados_filmes['LINGUAGEM'] == 'en']

#Mudando a coluna ID_FILME para int
#print(Base_dados_filmes.info())
Base_dados_filmes['ID_FILME'] = Base_dados_filmes['ID_FILME'].astype(int)
#print(avaliacoes.info())

# Concatenando os dataframes
avaliacoes_e_filmes = avaliacoes.merge(Base_dados_filmes, on = 'ID_FILME')
#print(avaliacoes_e_filmes.isna().sum())

#apagando duplicatas
avaliacoes_e_filmes.drop_duplicates(['ID_FILME','ID_USUARIO'],inplace=True)

#Deletando a variavel ID_FILME
del avaliacoes_e_filmes['ID_FILME']

# Agora precisamos fazer um PIVOT. O que queremos é que cada ID_USUARIO seja uma variavel com o respectivo valor de nota para cada filme avaliado
filmes_pivot = avaliacoes_e_filmes.pivot_table(columns = 'ID_USUARIO', index = 'TITULO', values = 'AVALIACAO')
filmes_pivot.fillna(0, inplace = True)

#print(filmes_pivot.head(4))

#TRABALHANCO COM SCIPY

filmes_sparse = csr_matrix(filmes_pivot)



#print(type(filmes_sparse))
# Criando e treinando o modelo preditivo
















#print(avaliacoes.isna().sum())
#print(pd.DataFrame(Base_dados_filmes.head(3)))
#print(pd.DataFrame(avaliacoes.head(3)))


