from funcoes import item, inimigo, batalha, aplicandoItem
from random import randint
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
    quantEscolhas = 1 #randint(1,4)
    if sala == 0:
        print("Você esta na sala principal")
        return "Vitoria"
    elif quantEscolhas == 1:
        lados = randint(1,4)
        if lados == 1:
            print(f"A porta aberta esta na direção: Cima")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Item na sala: {qualItem}")
            print(f"Monstro na sala: {qualInimigo}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":
                    lutar = input("Lutar contra o Monstro agora ?: S/N")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                        if resultado == "Vitoria":
                            qualInimigo = "Nenhum"
                        elif resultado == "GameOver":
                            print("Você perdeu")
                            return "Derrota"
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N")
                        while not(usar.lower() == "s" or usar.lower() == "n"):
                            usar = input("Usar item: S/N")
                        if usar.lower() == "s":
                            aplicandoItem(player, qualItem)
                            qualItem = "Nenhum"
                        print(player)
            return "Vitoria"
        elif lados == 2:
            print(f"Você pode apenas ir para Baixo")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Item na sala: {qualItem}")
            print(f"Monstro na sala: {qualInimigo}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":
            
                    lutar = input("Lutar contra o Monstro agora ?: S/N")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                        if resultado == "Vitoria":
                            qualInimigo = "Nenhum"
                        elif resultado == "GameOver":
                            print("Você perdeu")
                            return "Derrota"
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N")
                        while not(usar.lower() == "s" or usar.lower() == "n"):
                            usar = input("Usar item: S/N")
                        if usar.lower() == "s":
                            aplicandoItem(player, qualItem)
                            qualItem = "Nenhum"
                        print(player)
            return "Vitoria"
        elif lados == 3:
            print(f"Você pode apenas ir para Esquerda")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Item na sala: {qualItem}")
            print(f"Monstro na sala: {qualInimigo}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":
                    lutar = input("Lutar contra o Monstro agora ?: S/N")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                        if resultado == "Vitoria":
                            qualInimigo = "Nenhum"
                        elif resultado == "GameOver":
                            print("Você perdeu")
                            return "Derrota"
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N")
                        while not(usar.lower() == "s" or usar.lower() == "n"):
                            usar = input("Usar item: S/N")
                        if usar.lower() == "s":
                            aplicandoItem(player, qualItem)
                            qualItem = "Nenhum"
                        print(player)
            return "Vitoria"
        else:
            print(f"Você pode apenas ir para Direita")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Item na sala: {qualItem}")
            print(f"Monstro na sala: {qualInimigo}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":
                    lutar = input("Lutar contra o Monstro agora ?: S/N")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        if resultado == "Vitoria":
                            qualInimigo = "Nenhum"
                        elif resultado == "GameOver":
                            print("Você perdeu")
                            return "Derrota"
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N")
                        while not(usar.lower() == "s" or usar.lower() == "n"):
                            usar = input("Usar item: S/N")
                        if usar.lower() == "s":
                            aplicandoItem(player, qualItem)
                            qualItem = "Nenhum"
                        print(player)
            return "Vitoria"
                
    """elif quantEscolhas == 2:
        lados = randint(1,6)
        if lados == 1:
            print(f"Você pode ir para Cima ou Baixo")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Item na sala: {qualItem}")
            print(f"Monstro na sala: {qualInimigo}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":
            
                    lutar = input("Lutar contra o Monstro agora ?: S/N")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        
                        qualInimigo = "Nenhum"
                        if resultado == "GameOver":
                            break
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N")
                    while not(usar.lower() == "s" or usar.lower() == "n"):
                        usar = input("Usar item: S/N")
                    if usar.lower() == "s":
                        aplicandoItem(player, qualItem)
                        qualItem = "Nenhum"
                        print(player)
                
        elif lados == 2:
            print(f"Você pode ir para Cima ou Direita")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Item na sala: {qualItem}")
            print(f"Monstro na sala: {qualInimigo}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":
                    lutar = input("Lutar contra o Monstro agora ?: S/N")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                        if resultado == "GameOver":
                            break
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N")
                    while not(usar.lower() == "s" or usar.lower() == "n"):
                        usar = input("Usar item: S/N")
                    if usar.lower() == "s":
                        aplicandoItem(player, qualItem)
                        qualItem = "Nenhum"
                        print(player)
        elif lados == 3:
            print(f"Você pode ir para Cima ou Esquerda")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Item na sala: {qualItem}")
            print(f"Monstro na sala: {qualInimigo}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":
            
                    lutar = input("Lutar contra o Monstro agora ?: S/N")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                        if resultado == "GameOver":
                            break
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N")
                    while not(usar.lower() == "s" or usar.lower() == "n"):
                        usar = input("Usar item: S/N")
                    if usar.lower() == "s":
                        aplicandoItem(player, qualItem)
                        qualItem = "Nenhum"
                        print(player)
        elif lados == 4:
            print(f"Você pode ir para Baixo ou Direita")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Item na sala: {qualItem}")
            print(f"Monstro na sala: {qualInimigo}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":
            
                    lutar = input("Lutar contra o Monstro agora ?: S/N")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                        if resultado == "GameOver":
                            break
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N")
                    while not(usar.lower() == "s" or usar.lower() == "n"):
                        usar = input("Usar item: S/N")
                    if usar.lower() == "s":
                        aplicandoItem(player, qualItem)
                        qualItem = "Nenhum"
                        print(player)
        elif lados == 5:
            print(f"Você pode ir para Baixo ou Esquerda")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Item na sala: {qualItem}")
            print(f"Monstro na sala: {qualInimigo}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":
            
                    lutar = input("Lutar contra o Monstro agora ?: S/N")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                        if resultado == "GameOver":
                            break
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N")
                    while not(usar.lower() == "s" or usar.lower() == "n"):
                        usar = input("Usar item: S/N")
                    if usar.lower() == "s":
                        aplicandoItem(player, qualItem)
                        qualItem = "Nenhum"
                        print(player)
        else:
            print(f"Você pode ir para Esquerda ou Direita")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Item na sala: {qualItem}")
            print(f"Monstro na sala: {qualInimigo}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":
            
                    lutar = input("Lutar contra o Monstro agora ?: S/N")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                        if resultado == "GameOver":
                            break
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N")
                    while not(usar.lower() == "s" or usar.lower() == "n"):
                        usar = input("Usar item: S/N")
                    if usar.lower() == "s":
                        aplicandoItem(player, qualItem)
                        qualItem = "Nenhum"
                        print(player)
    elif quantEscolhas == 3:
        lados = randint(1,4)
        if lados == 1:
            print("Você pode ir para Cima, Baixo ou Esquerda")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Item na sala: {qualItem}")
            print(f"Monstro na sala: {qualInimigo}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":
            
                    lutar = input("Lutar contra o Monstro agora ?: S/N")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                        if resultado == "GameOver":
                            break
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N")
                    while not(usar.lower() == "s" or usar.lower() == "n"):
                        usar = input("Usar item: S/N")
                    if usar.lower() == "s":
                        aplicandoItem(player, qualItem)
                        qualItem = "Nenhum"
                        print(player)
        elif lados == 2:
            print("Você pode ir para Cima, Baixo ou Direita")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Item na sala: {qualItem}")
            print(f"Monstro na sala: {qualInimigo}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":
            
                    lutar = input("Lutar contra o Monstro agora ?: S/N")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        
                        qualInimigo = "Nenhum"
                        if resultado == "GameOver":
                            break
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N")
                    while not(usar.lower() == "s" or usar.lower() == "n"):
                        usar = input("Usar item: S/N")
                    if usar.lower() == "s":
                        aplicandoItem(player, qualItem)
                        qualItem = "Nenhum"
                        print(player)
        elif lados == 3:
            print("Você pode ir para Esquerda, Direita ou Cima")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Item na sala: {qualItem}")
            print(f"Monstro na sala: {qualInimigo}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":
            
                    lutar = input("Lutar contra o Monstro agora ?: S/N")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                        if resultado == "GameOver":
                            break
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N")
                    while not(usar.lower() == "s" or usar.lower() == "n"):
                        usar = input("Usar item: S/N")
                    if usar.lower() == "s":
                        aplicandoItem(player, qualItem)
                        qualItem = "Nenhum"
                        print(player)
        else:
            print("Você pode ir para Esquerda, Direita ou Baixo")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Item na sala: {qualItem}")
            print(f"Monstro na sala: {qualInimigo}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":
            
                    lutar = input("Lutar contra o Monstro agora ?: S/N")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        
                        qualInimigo = "Nenhum"
                        if resultado == "GameOver":
                            break
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N")
                    while not(usar.lower() == "s" or usar.lower() == "n"):
                        usar = input("Usar item: S/N")
                    if usar.lower() == "s":
                        aplicandoItem(player, qualItem)
                        qualItem = "Nenhum"
                        print(player)
    elif quantEscolhas == 4:
        print("Você pode ir para todos os lados")
        qualItem = item()
        qualInimigo = inimigo()
        resultado = ""
        print(f"Item na sala: {qualItem}")
        print(f"Monstro na sala: {qualInimigo}")
        while not(qualInimigo == "Nenhum" or qualItem == "Nenhum"):
            if qualInimigo != "Nenhum":
        
                lutar = input("Lutar contra o Monstro agora ?: S/N")
                if lutar.lower() == "s":
                    resultado = batalha(player,qualInimigo)
                    qualInimigo = "Nenhum"
                    if resultado == "GameOver":
                        break
            if resultado == "Vitoria" or qualInimigo == "Nenhum":
                if qualItem != "Nenhum":
                    usar = input("Usar item: S/N")
                while not usar.lower() == "s" or not usar.lower() == "n":
                    usar = input("Usar item: S/N")
                if usar.lower() == "s":
                    aplicandoItem(player, qualItem)
                    qualItem = "Nenhum"
                    print(player)"""
                    
player1 = {
    "nome": "jogador1",
    "itens": [],
    "forca": 0,
    "defesa": 0,
    "fuga": 0
}
addStatus(player1)
resultado = "Vitoria"
contSala = 0
while resultado.lower() == "vitoria":
    resultado = quantidadeDeEscolhas(player1, contSala)
    contSala += 1
