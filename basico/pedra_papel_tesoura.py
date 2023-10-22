import random


i = 0
s = 0
while True:
    usuario = input("pedra,papel ou tesoura: ")
    respostas = random.choice(["pedra", "papel", "tesoura"])
    print("{} x {}" .format(usuario, respostas))
    if usuario == "pedra" and respostas == "tesoura":
        print("!!! jogador venceu !!!")
        i = i + 1
    elif usuario == "papel" and respostas == "pedra":
        print("!!! jogador venceu !!!")
        i = i + 1
    elif usuario == "tesoura" and respostas == "papel":
        print("!!! jogador venceu !!!")
        i = i + 1
    elif usuario == respostas:
        print("!!! EMPATE !!!")
    else:
        print("!!! maquina venceu !!!")
        s = s + 1
    pergunta = input("digite s se quiser continuar ou (n) se quiser parar")
    if i + s == 5: 
            print("placar final\n usuaruio: {} x maquina: {}" .format(i,s))
            if s > i:
                print("!!! MAQUINA VENCEU !!!")
            elif s < i:
                print("!!! JOGADOR VENCEU !!!")
            break
            
