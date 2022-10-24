import random
def temItem():
    itemSN = random.randint(1,5)
    if itemSN == 1 or itemSN == 2:
        return "S"
    else:
        return "N"
def item():
    qualItem = random.randint(1,3)
    if temItem() == "S":
        if qualItem == 1:
            return "Espada"
        elif qualItem == 2:
            return "Escudo"
        else:
            return "Bota"
    else:
        return "Nenhum"
def temInimigo():
    inimigoSN = random.randint(1,3)
    if inimigoSN == 1 or inimigoSN == 2:
        return "S"
    else:
        return "N"
def inimigo():
    qualInimigo = random.randint(1,4)
    if temInimigo() == "S":
        if qualInimigo == 1:
            return "Slime"
        elif qualInimigo == 2:
            return "Zumbi"
        elif qualInimigo == 3:
            return "Esqueleto"
        else:
            return "Aranha"
    else:
        return "Nenhum"
def aplicandoItem(player,item):
    if item == "Espada":
        player["forca"] += 1
        return player["forca"]
    elif item == "Escudo":
        player["defesa"] += 1
        return player["defesa"]
    else:
        player["fuga"] += 1
        return player["fuga"]

def batalha(player, monstro):
    if monstro == "Slime":
        slime ={
            "nome": "slime",
            "forca": 2,
            "defesa": 1
        }
        while player["defesa"] >= 0 or slime["defesa"] >= 0:
            player["defesa"] -= slime["forca"]
            slime["defesa"] -= player["forca"]
        if player["defesa"] <= 0:
            return player["defesa"]
        else:
            return "gameOver"
    elif monstro == "Zumbi":
        zumbi ={
            "nome": "Zumbi",
            "forca": 1,
            "defesa": 3
        }
        while player["defesa"] >= 0 or zumbi["defesa"] >= 0:
            player["defesa"] -= zumbi["forca"]
            zumbi["defesa"] -= player["forca"]
        if player["defesa"] <= 0:
            return player["defesa"]
        else:
            return "gameOver"
    elif monstro == "Esqueleto":
        esqueleto ={
            "nome": "esqueleto",
            "forca": 3,
            "defesa": 2
        }
        while player["defesa"] >= 0 or esqueleto["defesa"] >= 0:
            player["defesa"] -= esqueleto["forca"]
            esqueleto["defesa"] -= player["forca"]
        if player["defesa"] <= 0:
            return player["defesa"]
        else:
            return "gameOver"
    elif monstro == "Aranha":
        aranha ={
            "nome": "aranha",
            "forca": 3,
            "defesa": 3
        }
        while player["defesa"] >= 0 or aranha["defesa"] >= 0:
            player["defesa"] -= aranha["forca"]
            aranha["defesa"] -= player["forca"]
        if player["defesa"] <= 0:
            return player["defesa"]
        else:
            return "gameOver"
        
    
def addStatus(player):
    print(f"Quanto de cada <STATUS> você quer dar para {player['nome']}?")
    player["forca"] = int(input("Quanto de Força ? \n"))
    while player["forca"] <= 0 or player["forca"] > 5:
        print("Força muito alta ou INVALIDA. Novo valor:")
        player["forca"] = int(input("Quanto de Força ? \n"))
    player["defesa"] = int(input("Quanto de Defesa ? \n"))
    while player["defesa"] <= 0 or player["defesa"] > 11:
        print("Defesa muito alta ou INVALIDA. Novo valor:")
        player["defesa"] = int(input("Quanto de Defesa ? \n"))
    player["fuga"] = int(input("Quanto de Fuga ? \n"))
    while player["fuga"] < 0 or player["fuga"] > 3:
        print("Fuga muito alta ou INVALIDA. Novo valor:")
        player["fuga"] = int(input("Quanto de Fuga ? \n"))
def quantidadeDeEscolhas(player, sala):
    quantEscolhas = random.randint(1,4)
    if sala == 0:
        print("Você esta na sala principal")
    elif quantEscolhas == 1:
        lados = random.randint(1,4)
        if lados == 1:
            qualItem = item()
            qualInimigo = inimigo()
            if qualItem != "Nenhum":
                print(f"Item na sala: {qualItem}")
                usar = input("Usar item: S/N")
                if usar.lower() == "s":
                    aplicandoItem(player, qualItem)
            if qualInimigo != "Nenhum":
                print(f"Monstro na sala: {qualInimigo}")
                usar = input("Lutar contro o Monstro agora ?: S/N")
                if usar.lower() == "s":
                    batalha(player,qualInimigo)
        elif lados == 2:
            print(f"Você pode apenas ir para Baixo")
            item()
            inimigo()
            escolha = input("Oque você quer fazer ?")
            if escolha.lower() == "baixo" and qualInimigo != "Nenhum":
                print("Derrote os inimigos primeiro")
        elif lados == 3:
            print(f"Você pode apenas ir para Esquerda")
            item()
            inimigo()
            escolha = input("Oque você quer fazer ?")
            if escolha.lower() == "esquerda" and qualInimigo != "Nenhum":
                print("Derrote os inimigos primeiro")
        else:
            print(f"Você pode apenas ir para Direita")
            item()
            inimigo()
            escolha = input("Oque você quer fazer ?")
            if escolha.lower() == "direita" and qualInimigo != "Nenhum":
                print("Derrote os inimigos primeiro")
    elif quantEscolhas == 2:
        lados = random.randint(1,6)
        if lados == 1:
            print(f"Você pode ir para Cima ou Baixo")
            item()
            inimigo()
            escolha = input("Oque você quer fazer ?")
            if escolha.lower() == "cima" or escolha.lower() == "baixo" and qualInimigo != "Nenhum":
                print("Derrote os inimigos primeiro")
        elif lados == 2:
            print(f"Você pode ir para Cima ou Direita")
            item()
            inimigo()
            escolha = input("Oque você quer fazer ?")
            if escolha.lower() == "cima" or escolha.lower() == "direita" and qualInimigo != "Nenhum":
                print("Derrote os inimigos primeiro")
        elif lados == 3:
            print(f"Você pode ir para Cima ou Esquerda")
            item()
            inimigo()
            escolha = input("Oque você quer fazer ?")
            if escolha.lower() == "cima" or escolha.lower() == "esquerda" and qualInimigo != "Nenhum":
                print("Derrote os inimigos primeiro")
        elif lados == 4:
            print(f"Você pode ir para Baixo ou Direita")
            item()
            inimigo()
            escolha = input("Oque você quer fazer ?")
            if escolha.lower() == "baixo" or escolha.lower() == "direita" and qualInimigo != "Nenhum":
                print("Derrote os inimigos primeiro")
        elif lados == 5:
            print(f"Você pode ir para Baixo ou Esquerda")
            item()
            inimigo()
            escolha = input("Oque você quer fazer ?")
            if escolha.lower() == "baixo" or escolha.lower() == "esquerda" and qualInimigo != "Nenhum":
                print("Derrote os inimigos primeiro")
        else:
            print(f"Você pode ir para Esquerda ou Direita")
            item()
            inimigo()
            escolha = input("Oque você quer fazer ?")
            if escolha.lower() == "esquerda" or escolha.lower() == "direita" and qualInimigo != "Nenhum":
                print("Derrote os inimigos primeiro")
    elif quantEscolhas == 3:
        lados = random.randint(1,4)
        if lados == 1:
            print("Você pode ir para Cima, Baixo ou Esquerda")
            item()
            inimigo()
            escolha = input("Oque você quer fazer ?")
            if escolha.lower() == "cima" or escolha.lower() == "baixo" or escolha.lower() == "esquerda" and qualInimigo != "Nenhum":
                print("Derrote os inimigos primeiro")
        elif lados == 2:
            print("Você pode ir para Cima, Baixo ou Direita")
            item()
            inimigo()
            escolha = input("Oque você quer fazer ?")
            if escolha.lower() == "cima" or escolha.lower() == "baixo" or escolha.lower() == "direita" and qualInimigo != "Nenhum":
                print("Derrote os inimigos primeiro")
        elif lados == 3:
            print("Você pode ir para Esquerda, Direita ou Cima")
            item()
            inimigo()
            escolha = input("Oque você quer fazer ?")
            if escolha.lower() == "cima" or escolha.lower() == "direita" or escolha.lower() == "esquerda" and qualInimigo != "Nenhum":
                print("Derrote os inimigos primeiro")
        else:
            print("Você pode ir para Esquerda, Direita ou Baixo")
            item()
            inimigo()
            escolha = input("Oque você quer fazer ?")
            if escolha.lower() == "baixo" or escolha.lower() == "direita" or escolha.lower() == "esquerda" and qualInimigo != "Nenhum":
                print("Derrote os inimigos primeiro")
    elif quantEscolhas == 4:
        print("Você pode ir para todos os lados")
        item()
        inimigo()
        escolha = input("Oque você quer fazer ?")
        if escolha.lower() == "cima" or escolha.lower() == "baixo" or escolha.lower() == "direita" or escolha.lower() == "esquerda" and qualInimigo != "Nenhum":
                print("Derrote os inimigos primeiro")
def criarSala(sala):
    quantidadeDeEscolhas(sala)
quantPlayer = int(input("1 jogador ou 2 jogadores ?\n"))
while not(quantPlayer == 1 or quantPlayer == 2):
    quantPlayer = int(input("1 jogador ou 2 jogadores ?\n"))
player1 = {
    "nome": "jogador1",
    "itens": 0,
    "forca": 0,
    "defesa": 0,
    "fuga": 0
}
addStatus(player1)
if quantPlayer == 2:            # CRIA PLAYER 2 SE A QUANTIDADE DE JOGADORES FOR 2
    player2 = {
        "nome": "jogador2",
        "itens": 0,
        "forca": 0,
        "vitalidade": 0,
        "fuga": 0
    }
    addStatus(player2)
zero = ""
contSala = 0
while zero != "a":
    criarSala(player1, contSala)
    contSala += 1
    zero = input()