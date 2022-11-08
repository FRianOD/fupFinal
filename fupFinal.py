from funcoes import item, inimigo, batalha, aplicandoItem
from random import randint
from time import sleep
def addStatus(player):
    tempo = 0.5
    
    print(f"Quanto de cada <STATUS> você quer dar para {player['nome']}?")
    player["forca"] = int(input("Quanto de Força ? \n"))
    sleep(tempo)

    while player["forca"] <= 0 or player["forca"] > 10:
        print("Força muito alta ou INVALIDA. Novo valor:")
        player["forca"] = int(input("Quanto de Força ? \n"))
        sleep(tempo)

    player["defesa"] = int(input("Quanto de Defesa ? \n"))
    sleep(tempo)

    if player["forca"] <= 5:        
        while player["defesa"] <= 0 or player["defesa"] > 10:
            print("Defesa muito alta ou INVALIDA. Novo valor:")
            player["defesa"] = int(input("Quanto de Defesa ? \n"))
            sleep(tempo)

    elif player["forca"] > 5:
        while player["defesa"] <= 0 or player["defesa"] > 5:
            print("Defesa muito alta ou INVALIDA. Novo valor:")
            player["defesa"] = int(input("Quanto de Defesa ? \n"))
            sleep(tempo)

    player["fuga"] = int(input("Quanto de Fuga ? \n"))
    sleep(tempo)

    while player["fuga"] < 0 or player["fuga"] > 3:
        print("Fuga muito alta ou INVALIDA. Novo valor:")
        player["fuga"] = int(input("Quanto de Fuga ? \n"))
        sleep(tempo)

def quantidadeDeEscolhas(player, sala, escolhaAnterior):
    quantEscolhas = 1 #randint(1,5)
    tempo = 1
    if sala == 0:
        print("Você esta na sala principal.\nVocê segue para unica porta aberta")
        sleep(tempo)
        return "Nenhum"
    elif quantEscolhas == 5 and sala >= 7:
        print("Você derrotou o BOSS!!!\nParabens!!!\nFIM DE JOGO!!!")
        sleep(tempo)
        return "Acabou"
    elif quantEscolhas == 1:
        while True:
            lados = randint(1,4)
            if lados == 1 and escolhaAnterior != "Baixo":
                print("A porta atras de você se fecha.\nA porta aberta esta na direção: Cima")
                sleep(tempo)
                salas = ["Cima"]
                qualItem = item()
                qualInimigo = inimigo()
                resultado = ""
                print(f"Monstro na sala: {qualInimigo}")
                sleep(tempo)
                print(f"Item na sala: {qualItem}")
                sleep(tempo)
                while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                    if qualInimigo != "Nenhum":
                        lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                        sleep(tempo)
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
                            sleep(tempo)
                            while not(usar.lower() == "s" or usar.lower() == "n"):
                                usar = input("Usar item: S/N\n")
                                sleep(tempo)
                            if usar.lower() == "s":
                                aplicandoItem(player, qualItem)
                                qualItem = "Nenhum"
                print(player)
                print("Sala Limpa!")
                sleep(tempo)
                print("Você so pode ir para Cima")
                escolha = input("Qual lado você ira ?\n")
                sleep(tempo)
                while escolha != "Cima":
                    escolha = input("Você so pode ir para Cima\n")
                    sleep(tempo)
                return escolha
            elif lados == 2 and escolhaAnterior != "Cima":
                print("""A porta atras de você se fecha.\nVocê pode apenas ir para Baixo""")
                sleep(tempo)
                salas = ["Baixo"]
                qualItem = item()
                qualInimigo = inimigo()
                resultado = ""
                print(f"Monstro na sala: {qualInimigo}")
                sleep(tempo)
                print(f"Item na sala: {qualItem}")
                sleep(tempo)
                while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                    if qualInimigo != "Nenhum":
                
                        lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                        sleep(tempo)
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
                            sleep(tempo)
                            while not(usar.lower() == "s" or usar.lower() == "n"):
                                usar = input("Usar item: S/N\n")
                                sleep(tempo)
                            if usar.lower() == "s":
                                aplicandoItem(player, qualItem)
                                qualItem = "Nenhum"
                print(player)
                print("Sala Limpa!")
                sleep(tempo)
                print("Você so pode ir para Baixo")
                escolha = input("Qual lado você ira ?\n")
                sleep(tempo)
                while escolha != "Baixo":
                    escolha = input("Você so pode ir para Baixo\n")
                    sleep(tempo)
                return escolha
            elif lados == 3 and escolhaAnterior != "Direita":
                print("A porta atras de você se fecha.\nVocê pode apenas ir para Esquerda")
                sleep(tempo)
                salas = ["Esquerda"]
                qualItem = item()
                qualInimigo = inimigo()
                resultado = ""
                print(f"Monstro na sala: {qualInimigo}")
                sleep(tempo)
                print(f"Item na sala: {qualItem}")
                sleep(tempo)
                while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                    if qualInimigo != "Nenhum":
                        lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                        sleep(tempo)
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
                            sleep(tempo)
                            while not(usar.lower() == "s" or usar.lower() == "n"):
                                usar = input("Usar item: S/N\n")
                                sleep(tempo)
                            if usar.lower() == "s":
                                aplicandoItem(player, qualItem)
                                qualItem = "Nenhum"
                print(player)
                print("Sala Limpa!")
                sleep(tempo)
                print("Você so pode ir para Esquerda")
                escolha = input("Qual lado você ira ?\n")
                sleep(tempo)
                while escolha != "Esquerda":
                    escolha = input("Você so pode ir para Esquerda\n")  
                    sleep(tempo)              
                return escolha
            elif lados == 4 and escolhaAnterior != "Esquerda":
                print("A porta atras de você se fecha.\nVocê pode apenas ir para Direita")
                sleep(tempo)
                salas = ["Direita"]
                qualItem = item()
                qualInimigo = inimigo()
                resultado = ""
                print(f"Monstro na sala: {qualInimigo}")
                sleep(tempo)
                print(f"Item na sala: {qualItem}")
                sleep(tempo)
                while not(qualInimigo == "Nenhum" and qualItem == "Nenhum"):
                    if qualInimigo != "Nenhum":
                        lutar = input("Lutar contra o Monstro agora ?: S/N\n")
                        sleep(tempo)
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
                            sleep(tempo)
                            while not(usar.lower() == "s" or usar.lower() == "n"):
                                usar = input("Usar item: S/N\n")
                                sleep(tempo)
                            if usar.lower() == "s":
                                aplicandoItem(player, qualItem)
                                qualItem = "Nenhum"
                print(player)
                print("Sala Limpa!")
                sleep(tempo)
                print("Você so pode ir para Direita")
                escolha = input("Qual lado você ira ?\n")
                sleep(tempo)
                while escolha != "Direita":
                    escolha = input("Você so pode ir para Direita\n")
                    sleep(tempo)
                return escolha
"""
    elif quantEscolhas == 2:
        while True:
            lados = randint(1,6)
            if lados == 1 and (escolhaAnterior != "Cima" or escolhaAnterior != "Baixo"):
                print("A porta atras de você se fecha.\nVocê pode ir para Cima ou Baixo")
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
                print("Sala Limpa!")
                print("Você so pode ir para Cima ou Baixo")
                escolha = input("Qual lado você ira ?\n")
                while not(escolha == "Cima" or escolha == "Baixo"):
                    escolha = input("Você so pode ir para Cima ou Baixo\n")
                return escolha
                    
            elif lados == 2 and (escolhaAnterior != "Baixo" or escolhaAnterior != "Esquerda"):
                print("A porta atras de você se fecha.\nVocê pode ir para Cima ou Direita")
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
                print("Sala Limpa!")
                print("Você so pode ir para Cima ou Direita")
                escolha = input("Qual lado você ira ?\n")
                while not(escolha == "Cima" or escolha == "Direita"):
                    escolha = input("Você so pode ir para Cima ou Direita\n")
                return escolha
            elif lados == 3 and (escolhaAnterior != "Baixo" or escolhaAnterior != "Direita"):
                print("A porta atras de você se fecha.\nVocê pode ir para Cima ou Esquerda")
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
                print("Sala Limpa!")
                print("Você so pode ir para Cima ou Esquerda")
                escolha = input("Qual lado você ira ?\n")
                while not(escolha == "Cima" or escolha == "Esquerda"):
                    escolha = input("Você so pode ir para Cima ou Esquerda\n")
                return escolha
            elif lados == 4 and (escolhaAnterior != "Cima" or escolhaAnterior != "Esquerda"):
                print("A porta atras de você se fecha.\nVocê pode ir para Baixo ou Direita")
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
                print("Sala Limpa!")
                print("Você so pode ir para Baixo ou Direita")
                escolha = input("Qual lado você ira ?\n")
                while not(escolha == "Baixo" or escolha == "Direita"):
                    escolha = input("Você so pode ir para Baixo ou Direita\n")
                return escolha
            elif lados == 5 and (escolhaAnterior != "Cima" or escolhaAnterior != "Direita"):
                print("A porta atras de você se fecha.\nVocê pode ir para Baixo ou Esquerda")
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
                print("Sala Limpa!")
                print("Você so pode ir para Baixo ou Esquerda")
                escolha = input("Qual lado você ira ?\n")
                while not(escolha == "Baixo" or escolha == "Esquerda"):
                    escolha = input("Você so pode ir para Baixo ou Esquerda\n")
                return escolha
            elif lados == 6 and (escolhaAnterior != "Baixo" or escolhaAnterior != "Esquerda"):
                print("A porta atras de você se fecha.\nVocê pode ir para Esquerda ou Direita")
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
                print("Sala Limpa!")
                print("Você so pode ir para Esquerda ou Direita")
                escolha = input("Qual lado você ira ?\n")
                while not(escolha == "Esquerda" or escolha == "Direita"):
                    escolha = input("Você so pode ir para Esquerda ou Direita\n")
                return escolha
    elif quantEscolhas == 3:
        while True:
            lados = randint(1,4)
            if lados == 1 and (escolhaAnterior == "Cima" or escolhaAnterior == "Baixo" or escolhaAnterior == "Direita"):
                print("A porta atras de Você se fecha.\nVocê pode ir para Cima, Baixo ou Esquerda")
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
                print("Sala Limpa!")
                print("Você so pode ir para Cima, Baixo ou Esquerda")
                escolha = input("Qual lado você ira ?\n")
                while not(escolha == "Cima" or escolha == "Baixo" or escolha == "Esquerda"):
                    escolha = input("Você so pode ir para Cima, Baixo ou Esquerda\n")
                return escolha
            elif lados == 2 and (escolhaAnterior == "Cima" or escolhaAnterior == "Baixo" or escolhaAnterior == "Esquerda"):
                print("A porta atras de Você se fecha.\nVocê pode ir para Cima, Baixo ou Direita")
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
                print("Sala Limpa!")
                print("Você so pode ir para Cima, Baixo ou Direita")
                escolha = input("Qual lado você ira ?\n")
                while not(escolha == "Cima" or escolha == "Baixo" or escolha == "Direita"):
                    escolha = input("Você so pode ir para Cima, Baixo ou Direita\n")
                return escolha
            elif lados == 3 and (escolhaAnterior == "Direita" or escolhaAnterior == "Esquerda" or escolhaAnterior == "Baixo"):
                print("A porta atras de Você se fecha.\nVocê pode ir para Esquerda, Direita ou Cima")
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
                print("Sala Limpa!")
                print("Você so pode ir para Esquerda, Direita ou Cima")
                escolha = input("Qual lado você ira ?\n")
                while not(escolha == "Direita" or escolha == "Esquerda" or escolha == "Cima"):
                    escolha = input("Você so pode ir para Esquerda, Direita ou Cima\n")
                return escolha
            elif lados == 4 and (escolhaAnterior == "Direita" or escolhaAnterior == "Esquerda" or escolhaAnterior == "Cima"):
                print("A porta atras de Você se fecha.\nVocê pode ir para Esquerda, Direita ou Baixo")
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
                print("Sala Limpa!")
                print("Você so pode ir para Esquerda, Direita ou Baixo")
                escolha = input("Qual lado você ira ?\n")
                while not(escolha == "Esquerda" or escolha == "Direita" or escolha == "Baixo"):
                    escolha = input("Você so pode ir para Direita, Esquerda ou Baixo\n")
                return escolha
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
