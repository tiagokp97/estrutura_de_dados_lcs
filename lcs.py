import time

def lcs_recursive(X, Y, m, n):
    start_time = time.time()
    result = lcs(X, Y, m, n)
    end_time = time.time()
    execution_time = end_time - start_time
    return {"result": result, "size": str(result), "time": f"{execution_time:.6f} seconds"}

def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))


def longest_common_subsequence(X, Y):
    start_time = time.time()
    # Obter o comprimento das duas sequências
    len_X = len(X)
    len_Y = len(Y)

    # Inicializar a matriz de programação dinâmica (dp) com zeros
    dp_matrix = [[0] * (len_Y + 1) for _ in range(len_X + 1)]

    # Preencher a matriz dp
    for i in range(1, len_X + 1):
        for j in range(1, len_Y + 1):
            # Quando os caracteres correspondentes nas duas sequências são iguais
            if X[i - 1] == Y[j - 1]:
                dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1
            else:
                # Escolher o maior valor entre a célula acima e a célula à esquerda
                dp_matrix[i][j] = max(dp_matrix[i - 1][j], dp_matrix[i][j - 1])

    # Reconstruir a subsequência comum mais longa a partir da matriz dp
    lcs_result = []
    i, j = len_X, len_Y
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_result.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp_matrix[i - 1][j] > dp_matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1


    # Converter a lista resultante em uma string e inverter para obter a LCS correta
    lcs_string = ''.join(reversed(lcs_result))
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000 


    return {"execution time": f"{execution_time:.6f} ms", "size": str(len(lcs_string)), "result": lcs_string}

# Exemplo de uso:
pairs = [
    ("ABCDEFGHIJKLMNOP", "PONMLKJIHGFEDCBA"),
    ("ABCDXYZLMNOPQR", "RQPONMLKJIHGFED"),
    ("ABRACADABRAALAK", "KALAABARACADABR"),
    ("JHONDOESAMMYJAN", "NAYJMMASEODNHOJ"),
    ("FIREWATERWINDH", "HNIDWRETAWEFIR"),
]

for i, (X, Y) in enumerate(pairs):
    print(f"Par {i+1}:")
    print("Versão com Programação Dinâmica:", longest_common_subsequence(X, Y))
    print("Versão Recursiva:", lcs_recursive(X, Y, len(X), len(Y)))

# Testando
# Recursiva 
# A função recursiva tem dois casos principais:

# As duas strings terminam no mesmo caractere, então temos que resolver o problema para as strings sem seus últimos caracteres.
# As duas strings têm diferentes caracteres finais, então temos dois subproblemas para resolver: um sem o último caractere da primeira string e outro sem o último caractere da segunda string.
# Isso nos dá uma árvore de recursão binária - cada nó tem até 2 filhos. Em uma árvore binária completa, o número total de nós é O(2^h), onde h é a altura da árvore. No nosso caso, a altura máxima da árvore é m + n, o que leva a uma complexidade de tempo de O(2^(m+n)).


# Dynamic programming
# Tempo: O(m*n)

# Usamos uma matriz 2D, "matriz", para armazenar os resultados intermediários. Para cada célula [i][j] dessa matriz, verificamos:

# Se X[i-1] == Y[j-1], então pegamos o valor de [i-1][j-1] e adicionamos 1.
# Caso contrário, pegamos o máximo entre [i-1][j] e [i][j-1].
# Como temos que calcular o valor para cada combinação de i (de 1 a m) e j (de 1 a n), o tempo total é O(m*n).