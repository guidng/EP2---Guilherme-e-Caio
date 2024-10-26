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

# EX4
def posiciona_frota(frota):
    if len(frota.keys())>0:
        tab_defesa=[]
        for y in range(10):
            tab_defesa.append([0] *10)
        for barco,pos in frota.items():
            for posic in pos:
                for posi in posic:
                    tab_defesa[posi[0]][posi[1]]=1
        return tab_defesa

# EX5
def afundados(frota,tabuleiro):
    n=0
    for barco,pos in frota.items():
        for posic in pos:
            v=0
            for posi in posic:
                if tabuleiro[posi[0]][posi[1]]!='X':
                    v=1
            if v==0:
                n+=1
    return n

# EX6
def posicao_valida(frota,linha,coluna,orientacao,tamanho):
    resp=True
    posicoes=define_posicoes(linha,coluna,orientacao,tamanho)
    for posi in posicoes:
        if posi[0]>=10 or posi[0]<0 or posi[1]>=10 or posi[1]<0:
            resp=False
        for pos in frota.values():
            for posic in pos:
                for posicao in posic:
                    if posicao[0]==posi[0] and posicao[1]==posi[1]:
                        resp=False
    return resp