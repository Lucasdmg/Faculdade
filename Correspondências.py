print("Tabelas de Preços e Correspondencias")
print("***"*10)
print("Digite as Dimenções do Pacote")
print("Peso")
peso=int(input(" >>> "))
while True:
    if peso == 0:
        print("Peso Incorreto!!!")
        break
    if peso <= 20:
        print(f"Voce selecionou \n {peso}g")
        print("Valor: R$7,52" )
        break
    if peso <= 50:
        print(f"Voce selecionou \n {peso}g")
        print("Valor: R$8,19")
        break
    if peso <= 100:
        print(f"Voce selecionou \n {peso}g")
        print("Valor: R$9,25")
        break
    if peso <= 150:
        print(f"Voce selecionou \n {peso}g")
        print("Valor: R$9,99")
        break
    if peso <= 200:
        print(f"Voce selecionou \n {peso}g")
        print("Valor: R$10,70")
    break
