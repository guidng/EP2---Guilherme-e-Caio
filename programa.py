import funcoes
# EX7
dic_embarcacoes={'porta-aviões':4,'navio-tanque':3,'contratorpedeiro':2,'submarino':1}

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

for navio,tamanho in dic_embarcacoes.items():
    for contador in range(5-tamanho):
        print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}')
        linha=int(input('Qual linha:'))
        coluna=int(input('Qual coluna:'))
        if navio!='submarino':
            orientacao=int(input('Qual orientação:'))
            if orientacao==1:orientacao='vertical'
            else:orientacao='horizontal'
        valid=funcoes.posicao_valida(frota,linha,coluna,orientacao,tamanho)
        while valid==False:
            print('Esta posição não está válida!')
            print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}')
            linha=int(input('Qual linha:'))
            coluna=int(input('Qual coluna:'))
            if navio!='submarino':
                orientacao=int(input('Qual orientação:'))
                if orientacao==1:orientacao='vertical'
                else:orientacao='horizontal'
            valid=funcoes.posicao_valida(frota,linha,coluna,orientacao,tamanho)
        else:
            lugares=funcoes.define_posicoes(linha,coluna,orientacao,tamanho)
            frota=funcoes.preenche_frota(frota, navio, linha, coluna, orientacao, tamanho)

#EX8
import random
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente=funcoes.posiciona_frota(frota_oponente)
tabuleiro_jogador=funcoes.posiciona_frota(frota)
jogando=True
lista_ineditas=[]
lista_ineditasop=[]
while jogando:
    print(funcoes.monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente))
    v=0
    while v==0:
        linha=int(input('Qual linha:'))
        while linha>9 or linha<0:
            print('Linha inválida!')
            linha=int(input('Qual linha:'))
        coluna=int(input('Qual coluna:'))
        while coluna>9 or coluna<0:
            print('Coluna inválida!')
            coluna=int(input('Qual coluna:'))
        if [linha,coluna] not in lista_ineditas:
            lista_ineditas.append([linha,coluna])
            v=1
        else:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
    tabuleiro_oponente=funcoes.faz_jogada(tabuleiro_oponente, linha, coluna)
    conf=funcoes.afundados(frota_oponente,tabuleiro_oponente)
    if conf==10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando=False
    else:
        v=0
        while v==0:
            linha_op=random.randint(0,9)
            coluna_op=random.randint(0,9)
            if [linha_op,coluna_op] not in lista_ineditasop:
                lista_ineditasop.append([linha_op,coluna_op])
                v=1
        print(f'Seu oponente está atacando na linha {linha_op} e coluna {coluna_op}')
        tabuleiro_jogador=funcoes.faz_jogada(tabuleiro_jogador,linha_op,coluna_op)
        conf_op=funcoes.afundados(frota,tabuleiro_jogador)
        if conf_op==10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando=False