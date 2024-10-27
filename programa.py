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