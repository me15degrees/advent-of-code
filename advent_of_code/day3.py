padrao = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


linhas = padrao.strip().split("\n")
matriz = [[int(caractere) if caractere.isdigit() else caractere for caractere in linha] for linha in linhas]
for linha in matriz:
 linhas, colunas = len(matriz), len(matriz[0])

def verifica_caracteres_especiais(i, j):
    caracteres_especiais = set('*#$+.')

    # Verifica na linha acima
    if i > 0 and isinstance(matriz[i - 1][j], int):
        for k in range(colunas):
            if matriz[i - 1][k] in caracteres_especiais:
                return True
    
  
    if isinstance(matriz[i][j], int):
        for k in range(linhas):
            if matriz[k][j] in caracteres_especiais:
                return True
    

    if j > 0 and isinstance(matriz[i][j - 1], int):
        for k in range(linhas):
            if matriz[k][j - 1] in caracteres_especiais:
                return True
    

    if j < colunas - 1 and isinstance(matriz[i][j + 1], int):
        for k in range(linhas):
            if matriz[k][j + 1] in caracteres_especiais:
                return True
    
    return False


for i in range(linhas):
    for j in range(colunas):
        if isinstance(matriz[i][j], int) and verifica_caracteres_especiais(i, j):
            print(f"Caractere especial adjacente ao número em ({i}, {j}): {matriz[i][j]}")
