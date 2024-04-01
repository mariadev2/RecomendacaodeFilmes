from sklearn.neighbors import NearestNeighbors

from Dadostratados import filmes_pivot, filmes_sparse,Base_dados_filmes


class Recomendacoes:
    def __init__(self):
        pass

    def selecionando_filme(self):
        filme_selecionado= input("Qual sua seleção:")
        return filme_selecionado

    def retornando_info(self):
        filme_selecionado = self.selecionando_filme()
        return print(Base_dados_filmes[Base_dados_filmes['TITULO'] == filme_selecionado])

    def retornando_recomendacao(self):
        modelo = NearestNeighbors(algorithm='brute')
        modelo.fit(filmes_sparse)
        filme_selecionado = self.selecionando_filme()
        distances, sugestions = modelo.kneighbors(
            filmes_pivot.filter(items=[filme_selecionado], axis=0).values.reshape(1, -1))

        for i in range(len(sugestions)):
            print(f"Filmes que voce pode gostar, porque assistiu -{filme_selecionado}-\n")
            print("-------SUGESTAO--------")
            print(filmes_pivot.index[sugestions[i]])

    def main(self):
        print("Escolha as opções:\n"
                            "[1] - Buscar recomendações\n"
                            "[2] - Buscar informações\n"
                            "[0] - Sair\n")
        menu = (input(int()))
        if menu == '1':
            self.retornando_recomendacao()
        elif menu == '2':
            self.retornando_info()
        elif menu == '0':
            mensagem = "fechando programa"
            return mensagem

# Verifica se o script está sendo executado como programa principal
if __name__ == "__main__":
    Recomendacoes().main()
