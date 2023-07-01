import random

games = ["roblox","valorant","League of Legends","minecraft","brawlhalla","counter strike","smite","paladins","overwatch","terraria"]
gameEscolhido = games[random.randint(0,9)]
palavra = "_" * len(gameEscolhido)

def game():
    global palavra

    print("Jogo da forca \n")

    print(palavra)

    letraEscolhida = input("tente uma letra:")

    if letraEscolhida not in gameEscolhido:
        print("perdeu uma vida")

    contador = 0

    for caractere in gameEscolhido: 
        if caractere == letraEscolhida:
            index = int(gameEscolhido.find(caractere, contador))

            palavra = palavra[:index] + palavra[index+1:]
            palavra = palavra[:index] + letraEscolhida + palavra[index:]

        contador += 1   

    game()

game()