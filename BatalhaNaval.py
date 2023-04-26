# Define Posição -

def define_posicoes(linha, coluna, orientacao, tamanho):
    
    grid = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
    ]

    posicao = []

    #Se orientação for 'vertical', coluna irá se manter constante
    #Se orientação for 'horizontal', linha irá se manter constante

    if orientacao == 'vertical':
        for L in range(linha,linha+tamanho):
            posicao.append([L,coluna])

    elif orientacao == 'horizontal':
        for c in range(coluna,coluna+tamanho):
            posicao.append([linha, c])

    return posicao

# Preenche Frota - 



# Faz Jogada - 

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro






























































































































































































