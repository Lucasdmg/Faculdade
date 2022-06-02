print('JOGO 2 OU 1')
cont1=0
cont2=0
cont3=0
while True:
    print("*-"* 10)
    a=int(input("Rafa joga >> " ))
    b=int(input("Helena joga >> " ))
    c=int(input("Lucas joga >> " ))
    if a == b == c:
        print(f"Empate !!! ")
        break
    if a == b or b == a:
        print("Lucas Ganhou")
        cont1 += 1
    if a == c or c == a:
        print("Helena Ganhou")
        cont2 += 1
    if b == c or c == b:
        print("Rafa Ganhou")
        cont3 += 1
    print(f"PLACAR >> Rafa {cont3} - Helena {cont2} - Lucas {cont1} << ")
    if cont1 == cont2 == cont3:
        print("EMPATEEE")
        break
    if cont1 > 2:
        print("Lucas Venceu o Jogo!!! ")
        break
    if cont2 > 2:
        print(" Helena Venceu o Jogo !!! ")
        break
    if cont3 > 2:
        print("Rafa Venceu o jogo !!! ")
        break
