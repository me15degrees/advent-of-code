def part_one(matriz):
    total = 0
    
    # horizontal (direita)
    for i in range(len(matriz)):
        for j in range(len(matriz[0]) - 3): 
            if matriz[i-1][j-1] == "S" and matriz[i][j] == "A" and matriz[i+1][j+1] == "M" and matriz[i-1][j+1] == "S" and matriz[i+1][j+1] == "M":
                total += 1
    
    # horizontal (esquerda)
    for i in range(len(matriz)):
        for j in range(len(matriz[0]) - 3): 
            if matriz[i][j] == "S" and matriz[i][j+1] == "A" and matriz[i][j+2] == "M" and matriz[i][j+3] == "X":
                total += 1

    # vertical (para baixo)
    for i in range(len(matriz) - 3): 
        for j in range(len(matriz[0])):
            if matriz[i][j] == "X" and matriz[i+1][j] == "M" and matriz[i+2][j] == "A" and matriz[i+3][j] == "S":
                total += 1
    
    # vertical invertida (para cima)
    for i in range(3, len(matriz)):  
        for j in range(len(matriz[0])):
            if matriz[i][j] == "X" and matriz[i-1][j] == "M" and matriz[i-2][j] == "A" and matriz[i-3][j] == "S":
                total += 1
    
    # diagonal (para baixo e para direita)
    for i in range(len(matriz) - 3):
        for j in range(len(matriz[0]) - 3):
            if matriz[i][j] == "X" and matriz[i+1][j+1] == "M" and matriz[i+2][j+2] == "A" and matriz[i+3][j+3] == "S":
                total += 1
    
    # diagonal (para cima e para a direita)
    for i in range(3, len(matriz)):
        for j in range(len(matriz[0]) - 3):
            if matriz[i][j] == "X" and matriz[i-1][j+1] == "M" and matriz[i-2][j+2] == "A" and matriz[i-3][j+3] == "S":
                total += 1

    # diagonal (para baixo e para a esquerda)
    for i in range(len(matriz) - 3):
        for j in range(3, len(matriz[0])):
            if matriz[i][j] == "X" and matriz[i+1][j-1] == "M" and matriz[i+2][j-2] == "A" and matriz[i+3][j-3] == "S":
                total += 1
    
    # diagonal (para cima e para a esquerda)
    for i in range(3, len(matriz)):
        for j in range(3, len(matriz[0])):
            if matriz[i][j] == "X" and matriz[i-1][j-1] == "M" and matriz[i-2][j-2] == "A" and matriz[i-3][j-3] == "S":
                total += 1
    return total

def part_two(matriz):
    total = 0
    
    for i in range(1, len(matriz) - 1):  # Garantir que o i não ultrapasse os limites
        for j in range(1, len(matriz[0]) - 1):  # Garantir que o j não ultrapasse os limites
            
            # Verificar as 4 disposições possíveis do "X" formado pelas palavras "MAS" ou "SAM"
            
            # Caso 1: "MAS" formando um X
            if matriz[i-1][j-1] == "M" and matriz[i][j] == "A" and matriz[i+1][j+1] == "S" and matriz[i+1][j-1] == "S" and matriz[i-1][j+1] == "M":
                total += 1
            
            # Caso 2: "SAM" formando um X
            if matriz[i-1][j-1] == "M" and matriz[i][j] == "A" and matriz[i+1][j+1] == "S" and matriz[i+1][j-1] == "M" and matriz[i-1][j+1] == "S":
                total += 1

            # Caso 3: "MAS" invertido formando um X
            if matriz[i-1][j-1] == "S" and matriz[i][j] == "A" and matriz[i+1][j+1] == "M" and matriz[i+1][j-1] == "M" and matriz[i-1][j+1] == "S":
                total += 1

            # Caso 4: "SAM" invertido formando um X
            if matriz[i-1][j-1] == "S" and matriz[i][j] == "A" and matriz[i+1][j+1] == "M" and matriz[i+1][j-1] == "S" and matriz[i-1][j+1] == "M":
                total += 1

    return total


def main():
    with open('input.in', 'r') as file:
        content = file.read().strip()
        matriz = [list(linha) for linha in content.split("\n")]
    #res_part_one = part_one(matriz)
    res_part_two = part_two(matriz)
    
    print(f"Total de ocorrências de 'XMAS': {res_part_two}")
main()
