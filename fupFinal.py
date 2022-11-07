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

def quantidadeDeEscolhas(player, sala, escolhaAnterior):
    quantEscolhas = 1 #randint(1,4)
    if sala == 0:
        print("Você esta na sala principal")
        return "Nenhum"
    elif quantEscolhas == 1:
        while True:
            lados = randint(1,4)
            if lados == 1 and escolhaAnterior != "Cima":
                print(f"A porta aberta esta na direção: Cima")
                salas = ["Cima"]
                qualItem = item()
                qualInimigo = inimigo()
                resultado = ""
                print(f"Monstro na sala: {qualInimigo}")
                print(f"Item na sala: {qualItem}")
                while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                    if qualInimigo != "Nenhum":
                        lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                        if lutar.lower() == "s":
                            resultado = batalha(player,qualInimigo)
                            qualInimigo = "Nenhum"
                    if player["defesa"] <= 0 :
                        print("Você perdeu")
                        input()
                        return "Derrota"
                    if resultado == "Vitoria" or qualInimigo == "Nenhum":
                        if qualItem != "Nenhum":
                            usar = input("Usar item: S/N\n")
                            while not(usar.lower() == "s" or usar.lower() == "n"):
                                usar = input("Usar item: S/N\n")
                            if usar.lower() == "s":
                                aplicandoItem(player, qualItem)
                                qualItem = "Nenhum"
                escolha = input("Você so pode ir para Cima\n")
                return escolha
            elif lados == 2 and escolhaAnterior != "Baixo":
                print(f"Você pode apenas ir para Baixo")
                salas = ["Baixo"]
                qualItem = item()
                qualInimigo = inimigo()
                resultado = ""
                print(f"Monstro na sala: {qualInimigo}")
                print(f"Item na sala: {qualItem}")
                while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                    if qualInimigo != "Nenhum":
                
                        lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                        if lutar.lower() == "s":
                            resultado = batalha(player,qualInimigo)
                            qualInimigo = "Nenhum"
                    if player["defesa"] <= 0 :
                        print("Você perdeu")
                        input()
                        return "Derrota"
                    if resultado == "Vitoria" or qualInimigo == "Nenhum":
                        if qualItem != "Nenhum":
                            usar = input("Usar item: S/N\n")
                            while not(usar.lower() == "s" or usar.lower() == "n"):
                                usar = input("Usar item: S/N\n")
                            if usar.lower() == "s":
                                aplicandoItem(player, qualItem)
                                qualItem = "Nenhum"
                print(player)
                print(lados)
                print("Você ganhou")
                escolha = input("Você so pode ir para Baixo\n")
                return escolha
            elif lados == 3 and escolhaAnterior != "Esquerda":
                print(f"Você pode apenas ir para Esquerda")
                salas = ["Esquerda"]
                qualItem = item()
                qualInimigo = inimigo()
                resultado = ""
                print(f"Monstro na sala: {qualInimigo}")
                print(f"Item na sala: {qualItem}")
                while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                    if qualInimigo != "Nenhum":
                        lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                        if lutar.lower() == "s":
                            resultado = batalha(player,qualInimigo)
                            qualInimigo = "Nenhum"
                    if player["defesa"] <= 0 :
                        print("Você perdeu")
                        input()
                        return "Derrota"
                    if resultado == "Vitoria" or qualInimigo == "Nenhum":
                        if qualItem != "Nenhum":
                            usar = input("Usar item: S/N\n")
                            while not(usar.lower() == "s" or usar.lower() == "n"):
                                usar = input("Usar item: S/N\n")
                            if usar.lower() == "s":
                                aplicandoItem(player, qualItem)
                                qualItem = "Nenhum"
                print(player)
                print(lados)
                print("Você ganhou")
                escolha = input("Você so pode ir para Esquerda\n")
                return escolha
            elif lados == 4 and escolhaAnterior != "Direita":
                print(f"Você pode apenas ir para Direita")
                salas = ["Direita"]
                qualItem = item()
                qualInimigo = inimigo()
                resultado = ""
                print(f"Monstro na sala: {qualInimigo}")
                print(f"Item na sala: {qualItem}")
                while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                    if qualInimigo != "Nenhum":
                        lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                        if lutar.lower() == "s":
                            resultado = batalha(player,qualInimigo)
                            qualInimigo = "Nenhum"
                    if player["defesa"] <= 0:
                        print("Você perdeu")
                        input()
                        return "Derrota"
                    if resultado == "Vitoria" or qualInimigo == "Nenhum":
                        if qualItem != "Nenhum":
                            usar = input("Usar item: S/N\n")
                            while not(usar.lower() == "s" or usar.lower() == "n"):
                                usar = input("Usar item: S/N\n")
                            if usar.lower() == "s":
                                aplicandoItem(player, qualItem)
                                qualItem = "Nenhum"
                print(player)
                print(lados)
                print("Você ganhou")
                escolha = input("Você so pode ir para Direita\n")
                return escolha
"""              
    elif quantEscolhas == 2:
        lados = randint(1,6)
        if lados == 1:
            print(f"Você pode ir para Cima ou Baixo")
            salas = ["Cima", "Baixo"]
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Monstro na sala: {qualInimigo}")
            print(f"Item na sala: {qualItem}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":            
                    lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                if player["defesa"] <= 0 :
                    print("Você perdeu")
                    input()
                    return "Derrota"
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N\n")
                        while not(usar.lower() == "s" or usar.lower() == "n"):
                            usar = input("Usar item: S/N\n")
                        if usar.lower() == "s":
                            aplicandoItem(player, qualItem)
                            qualItem = "Nenhum"
            print(player)
            print("Você ganhou")
            input()
            return "Vitoria"
                
        elif lados == 2:
            print(f"Você pode ir para Cima ou Direita")
            salas = ["Cima", "Direita"]
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Monstro na sala: {qualInimigo}")
            print(f"Item na sala: {qualItem}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":            
                    lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                if player["defesa"] <= 0 :
                    print("Você perdeu")
                    input()
                    return "Derrota"
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N\n")
                        while not(usar.lower() == "s" or usar.lower() == "n"):
                            usar = input("Usar item: S/N\n")
                        if usar.lower() == "s":
                            aplicandoItem(player, qualItem)
                            qualItem = "Nenhum"
            print(player)
            print("Você ganhou")
            input()
            return "Vitoria"
        elif lados == 3:
            print(f"Você pode ir para Cima ou Esquerda")
            salas = ["Cima", "Esquerda"]
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Monstro na sala: {qualInimigo}")
            print(f"Item na sala: {qualItem}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":
                    lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                if player["defesa"] <= 0 :
                    print("Você perdeu")
                    input()
                    return "Derrota"
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N\n")
                        while not(usar.lower() == "s" or usar.lower() == "n"):
                            usar = input("Usar item: S/N\n")
                        if usar.lower() == "s":
                            aplicandoItem(player, qualItem)
                            qualItem = "Nenhum"
            print(player)
            print("Você ganhou")
            input()
            return "Vitoria"
        elif lados == 4:
            print(f"Você pode ir para Baixo ou Direita")
            salas = ["Baixo", "Direita"]
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Monstro na sala: {qualInimigo}")
            print(f"Item na sala: {qualItem}")            
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":
                    lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                if player["defesa"] <= 0 :
                    print("Você perdeu")
                    input()
                    return "Derrota"
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N\n")
                        while not(usar.lower() == "s" or usar.lower() == "n"):
                            usar = input("Usar item: S/N\n")
                        if usar.lower() == "s":
                            aplicandoItem(player, qualItem)
                            qualItem = "Nenhum"
            print(player)
            print("Você ganhou")
            input()
            return "Vitoria"
        elif lados == 5:
            print(f"Você pode ir para Baixo ou Esquerda")
            salas = ["Baixo", "Esquerda"]
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Monstro na sala: {qualInimigo}")
            print(f"Item na sala: {qualItem}")
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":            
                    lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                if player["defesa"] <= 0 :
                    print("Você perdeu")
                    input()
                    return "Derrota"
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N\n")
                        while not(usar.lower() == "s" or usar.lower() == "n"):
                            usar = input("Usar item: S/N\n")
                        if usar.lower() == "s":
                            aplicandoItem(player, qualItem)
                            qualItem = "Nenhum"
            print(player)
            print("Você ganhou")
            input()
            return "Vitoria"
        else:
            print(f"Você pode ir para Esquerda ou Direita")
            salas = ["Esquerda", "Direita"]
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Monstro na sala: {qualInimigo}")
            print(f"Item na sala: {qualItem}")           
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":            
                    lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                if player["defesa"] <= 0 :
                    print("Você perdeu")
                    input()
                    return "Derrota"
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N\n")
                        while not(usar.lower() == "s" or usar.lower() == "n"):
                            usar = input("Usar item: S/N\n")
                        if usar.lower() == "s":
                            aplicandoItem(player, qualItem)
                            qualItem = "Nenhum"
            print(player)
            print("Você ganhou")
            input()
            return "Vitoria"
    elif quantEscolhas == 3:
        lados = randint(1,4)
        if lados == 1:
            print("Você pode ir para Cima, Baixo ou Esquerda")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Monstro na sala: {qualInimigo}")
            print(f"Item na sala: {qualItem}")            
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":            
                    lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                if player["defesa"] <= 0 :
                    print("Você perdeu")
                    input()
                    return "Derrota"
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N\n")
                        while not(usar.lower() == "s" or usar.lower() == "n"):
                            usar = input("Usar item: S/N\n")
                        if usar.lower() == "s":
                            aplicandoItem(player, qualItem)
                            qualItem = "Nenhum"
            print(player)
            print("Você ganhou")
            input()
            return "Vitoria"
        elif lados == 2:
            print("Você pode ir para Cima, Baixo ou Direita")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Monstro na sala: {qualInimigo}")
            print(f"Item na sala: {qualItem}")            
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":            
                    lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                if player["defesa"] <= 0 :
                    print("Você perdeu")
                    input()
                    return "Derrota"
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N\n")
                        while not(usar.lower() == "s" or usar.lower() == "n"):
                            usar = input("Usar item: S/N\n")
                        if usar.lower() == "s":
                            aplicandoItem(player, qualItem)
                            qualItem = "Nenhum"
            print(player)
            print("Você ganhou")
            input()
            return "Vitoria"
        elif lados == 3:
            print("Você pode ir para Esquerda, Direita ou Cima")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Monstro na sala: {qualInimigo}")
            print(f"Item na sala: {qualItem}")            
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":            
                    lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                if player["defesa"] <= 0 :
                    print("Você perdeu")
                    input()
                    return "Derrota"
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N\n")
                        while not(usar.lower() == "s" or usar.lower() == "n"):
                            usar = input("Usar item: S/N\n")
                        if usar.lower() == "s":
                            aplicandoItem(player, qualItem)
                            qualItem = "Nenhum"
            print(player)
            print("Você ganhou")
            input()
            return "Vitoria"
        else:
            print("Você pode ir para Esquerda, Direita ou Baixo")
            qualItem = item()
            qualInimigo = inimigo()
            resultado = ""
            print(f"Monstro na sala: {qualInimigo}")
            print(f"Item na sala: {qualItem}")            
            while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                if qualInimigo != "Nenhum":           
                    lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                    if lutar.lower() == "s":
                        resultado = batalha(player,qualInimigo)
                        qualInimigo = "Nenhum"
                if player["defesa"] <= 0 :
                    print("Você perdeu")
                    input
                    return "Derrota"
                if resultado == "Vitoria" or qualInimigo == "Nenhum":
                    if qualItem != "Nenhum":
                        usar = input("Usar item: S/N\n")
                        while not(usar.lower() == "s" or usar.lower() == "n"):
                            usar = input("Usar item: S/N\n")
                        if usar.lower() == "s":
                            aplicandoItem(player, qualItem)
                            qualItem = "Nenhum"
            print(player)
            print("Você ganhou")
            input()
            return "Vitoria"
    elif quantEscolhas == 4:
        print("Você pode ir para todos os lados")
        qualItem = item()
        qualInimigo = inimigo()
        resultado = ""
        print(f"Monstro na sala: {qualInimigo}")
        print(f"Item na sala: {qualItem}")        
        while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
            if qualInimigo != "Nenhum":            
                lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                if lutar.lower() == "s":
                    resultado = batalha(player,qualInimigo)
                    qualInimigo = "Nenhum"
            if player["defesa"] <= 0 :
                print("Você perdeu")
                input()
                return "Derrota"
            if resultado == "Vitoria" or qualInimigo == "Nenhum":
                if qualItem != "Nenhum":
                    usar = input("Usar item: S/N\n")
                    while not(usar.lower() == "s" or usar.lower() == "n"):
                        usar = input("Usar item: S/N\n")
                    if usar.lower() == "s":
                        aplicandoItem(player, qualItem)
                        qualItem = "Nenhum"
            print(player)
            print("Você ganhou")
            input()
            return "Vitoria"
"""
player1 = {
    "nome": "jogador1",
    "itens": [],
    "forca": 0,
    "defesa": 0,
    "fuga": 0
}
addStatus(player1)
escolha = "Nenhum"
contSala = 0
while escolha == "Nenhum" or escolha == "Cima" or escolha == "Baixo" or escolha == "Esquerda" or escolha == "Direita":
    escolhaAnterior = escolha
    escolha = quantidadeDeEscolhas(player1, contSala, escolhaAnterior)
    contSala += 1
