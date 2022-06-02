n = int(input("Informe o quadrado da Matriz >> "))
print(f"Voce informou uma Matriz {n} x {n}")
matriz= (n+n**3)/2

A = []
for i in range(n):
    l = []
    for j in range(n):
        l.append(int(input('Digite o valor de [' + str(i) + ',' + str(j) + ']:')))
    A.append(l)

for j in range(n):
    for i in range(n):
        print(f"[{A[j][i]:^3}]", end=" ")
    print()
# diagonal principal
soma = 0
for i in range(n):
    soma = soma + A[i][i]
if (soma != matriz):
    print("NÃO É MÁGICO")
    exit()
# diagonal secundaria
soma = 0
for i in range(n):
    soma = soma + A[i][n - 1 - i]
if (soma != matriz):
    print("NÃO É MÁGICO")
    exit()
# linhas
for i in range(n):
    soma = 0
    for j in range(n):
        soma = soma + A[i][j]
    if (soma != matriz):
        print("NÃO É MÁGICO")
        exit()
# colunas
for j in range(n):
    soma = 0
    for i in range(n):
        soma = soma + A[i][j]
    if (soma != matriz):
        print("NÃO É MÁGICO")
        exit()
print("É MÁGICO")
