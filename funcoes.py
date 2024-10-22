#EX1
def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_posicoes=[]
    for i in range(tamanho):
        lista_posicoes.append([linha,coluna])
        if orientacao=='vertical':
            linha+=1
        else:
            coluna+=1
    return lista_posicoes

#EX2
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    if nome_navio not in frota.keys():
        frota[nome_navio] =  [define_posicoes(linha,coluna,orientacao,tamanho)]
    else:
        frota[nome_navio].append(define_posicoes(linha,coluna,orientacao,tamanho))
    return frota

#EX3
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"

    return tabuleiro

