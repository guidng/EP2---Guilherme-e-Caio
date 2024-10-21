def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_posicoes=[]
    for i in range(tamanho):
        lista_posicoes.append(f'{linha},{coluna}')
        if orientacao=='vertical':
            linha+=1
        else:
            coluna+=1
    return lista_posicoes