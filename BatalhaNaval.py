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

def preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho):
    posicao = []
    i = 0
    if frota == {} or nome_navio not in frota:
        if orientacao == 'horizontal':
            while i < tamanho:
                posicao.append([linha,coluna+i])
                i += 1
        elif orientacao == 'vertical':
            while i < tamanho:
                posicao.append([linha+i,coluna])
                i += 1
        frota[nome_navio] = ([posicao])
    else:
        if orientacao == 'horizontal':
            while i < tamanho:
                posicao.append([linha,coluna+i])
                i += 1
        elif orientacao == 'vertical':
            while i < tamanho:
                posicao.append([linha+i,coluna])
                i += 1
        frota[nome_navio].append(posicao)
    return frota
    


# Faz Jogada - 

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

# Posiciona Frota 

def posiciona_frota(frota):
    tabuleiro = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    for chave in frota:
        for valor in frota[chave]:
            for posicao in valor:
                tabuleiro[posicao[0]][posicao[1]] = 1
    return tabuleiro

# Quantas embarcações afundadas?

def afundados(frota, tabuleiro):

  N_Afundados = 0
  for navio in frota:
    for tamanho in frota[navio]:
      y = 0
      for cords in tamanho:
        x = tabuleiro[cords[0]][cords[1]]
        if x != 'X':
          y = 1
      if y == 0:
        N_Afundados += 1
  
  return N_Afundados

# Posição Válida

def posicao_valida(frota,linha,coluna,orientacao,tamanho):
    posicoes_preenchidas = []
    position = define_posicoes(linha, coluna, orientacao, tamanho)
    for w in position:
        x = w[0]
        y = w[1]
        if x < 0 or x > 9 or y < 0 or y > 9:
            return False
        for navio, lista in frota.items():
            for pos in lista:
                for n in pos:
                    posicoes_preenchidas.append(n)
                    if n[0] == x and  n[1] == y:
                        return False
    return True



# Posicionando Frota

# Jogadas do jogador

# Jogadas do Oponente





























































































































































































