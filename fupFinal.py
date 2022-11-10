from funcoes import item, inimigo, qualBoss, batalhaBoss,salas
from random import randint
from time import sleep
def addStatus(player):
    tempo = 0.5
    
    print(f"Quanto de cada <STATUS> você quer dar para {player['Nome']}?")
    sleep(tempo)
    print("Forças recomendadas: 2, 5, 10")
    sleep(tempo)
    player["forca"] = int(input("Quanto de Força ? \n"))
    sleep(tempo)

    while player["forca"] <= 0 or player["forca"] > 10:
        print("Força muito alta ou INVALIDA. Novo valor.")
        sleep(tempo)
        print("Força max: 10")
        sleep(tempo)
        player["forca"] = int(input("Quanto de Força ? \n"))
        sleep(tempo)

    print("Defesas recomendadas: 5, 10, 15.")
    sleep(tempo)
    player["defesa"] = int(input("Quanto de Defesa ? \n"))
    sleep(tempo)

    if player["forca"] <= 2:        
        while player["defesa"] <= 0 or player["defesa"] > 15:
            print("Defesa muito alta ou INVALIDA. Novo valor.")
            sleep(tempo)
            print("Defesa max: 14.")
            sleep(tempo)
            player["defesa"] = int(input("Quanto de Defesa ? \n"))
            sleep(tempo)

    elif player["forca"] <= 5:        
        while player["defesa"] <= 0 or player["defesa"] > 10:
            print("Defesa muito alta ou INVALIDA. Novo valor.")
            sleep(tempo)
            print("Defesa max: 9.")
            sleep(tempo)
            player["defesa"] = int(input("Quanto de Defesa ? \n"))
            sleep(tempo)

    elif player["forca"] > 5:
        while player["defesa"] <= 0 or player["defesa"] > 5:
            print("Defesa muito alta ou INVALIDA. Novo valor.")
            sleep(tempo)
            print("Defesa max: 5.")
            sleep(tempo)
            player["defesa"] = int(input("Quanto de Defesa ? \n"))
            sleep(tempo)

    print("Fuga recomendada: 3.")
    sleep(tempo)
    player["fuga"] = int(input("Quanto de Fuga ? \n"))
    sleep(tempo)

    while player["fuga"] < 0 or player["fuga"] > 3:
        print("Fuga muito alta ou INVALIDA. Novo valor:")
        sleep(tempo)
        print("Fuga max: 3.")
        sleep(tempo)
        player["fuga"] = int(input("Quanto de Fuga ? \n"))
        sleep(tempo)

def quantidadeDeEscolhas(player, sala, escolhaAnterior):
    while True:
        quantEscolhas = randint(1,7)
        tempo = 1
        if sala == 0:
            print("Você esta na sala principal.")
            sleep(tempo)
            print("Você segue para unica porta aberta")
            sleep(tempo)
            return "Nenhum"
        elif quantEscolhas >= 4 and sala >= 7:
            print("A porta atras de você se fecha.")
            sleep(tempo)
            print("Não a nenhuma porta aberta.")
            sleep(tempo)
            print("Você chegou a sala do boss")
            sleep(tempo)
            
            boss = qualBoss()
            print(f"Boss da sala: {boss}")
            sleep(tempo)

            batalhaBoss(player, boss)
            if player["defesa"] > 0:
                sleep(tempo)
                print(f"Você derrotou o BOSS: {boss}!!!")
                sleep(tempo)
                print(f"Parabens!!!")
                sleep(tempo)
                print(f"FIM DE JOGO!!!")
                return "Acabou"
            elif player["defesa"] <= 0:
                sleep(tempo)
                return "Acabou"
        elif quantEscolhas == 1:
            while True:
                lados = randint(1,4)
                if lados == 1 and not(escolhaAnterior == "Baixo"):
                    print("A porta atras de você se fecha.")
                    sleep(tempo)
                    print("Você pode apenas ir para Cima")
                    sleep(tempo)
                    qualInimigo = inimigo()
                    qualItem = item(qualInimigo)
                    result = salas(player,qualInimigo,qualItem)
                    if result == "Vitoria":
                        print(player)
                        sleep(tempo)
                        print("Sala Limpa!")
                        sleep(tempo)
                        print("Você so pode ir para Cima")
                        escolha = input("Qual lado você ira ?\n")
                        sleep(tempo)
                        while escolha != "Cima":
                            escolha = input("Você so pode ir para Cima\n")
                            sleep(tempo)
                        return escolha
                    else:
                        return "Acabou"
                elif lados == 2 and not(escolhaAnterior == "Cima"):
                    print("A porta atras de você se fecha.")
                    sleep(tempo)
                    print("Você pode apenas ir para Baixo")
                    sleep(tempo)
                    qualInimigo = inimigo()
                    qualItem = item(qualInimigo)
                    result = salas(player,qualInimigo,qualItem)
                    if result == "Vitoria":
                        print(player)
                        sleep(tempo)
                        print("Sala Limpa!")
                        sleep(tempo)
                        print("Você so pode ir para Baixo")
                        escolha = input("Qual lado você ira ?\n")
                        sleep(tempo)
                        while escolha != "Baixo":
                            escolha = input("Você so pode ir para Baixo\n")
                            sleep(tempo)
                        return escolha
                    else:
                        return "Acabou"
                elif lados == 3 and not(escolhaAnterior == "Direita"):
                    print("A porta atras de você se fecha.")
                    sleep(tempo)
                    print("Você pode apenas ir para Esquerda")
                    sleep(tempo)
                    qualInimigo = inimigo()
                    qualItem = item(qualInimigo)
                    result = salas(player,qualInimigo,qualItem)
                    if result == "Vitoria":
                        print(player)
                        sleep(tempo)
                        print("Sala Limpa!")
                        sleep(tempo)
                        print("Você so pode ir para Esquerda")
                        escolha = input("Qual lado você ira ?\n")
                        sleep(tempo)
                        while escolha != "Esquerda":
                            escolha = input("Você so pode ir para Esquerda\n")  
                            sleep(tempo)              
                        return escolha
                    else:
                        return "Acabou"
                elif lados == 4 and not(escolhaAnterior == "Esquerda"):
                    print("A porta atras de você se fecha.")
                    sleep(tempo)
                    print("Você pode apenas ir para Direita")
                    sleep(tempo)
                    qualInimigo = inimigo()
                    qualItem = item(qualInimigo)
                    result = salas(player,qualInimigo,qualItem)
                    if result == "Vitoria":
                        print(player)
                        sleep(tempo)
                        print("Sala Limpa!")
                        sleep(tempo)
                        print("Você so pode ir para Direita")
                        escolha = input("Qual lado você ira ?\n")
                        sleep(tempo)
                        while escolha != "Direita":
                            escolha = input("Você so pode ir para Direita\n")
                            sleep(tempo)
                        return escolha
                    else:
                        return "Acabou"  
        elif quantEscolhas == 2:
            while True:
                lados = randint(1,6)
                if lados == 1 and not(escolhaAnterior == "Cima" or escolhaAnterior == "Baixo"):
                    print("A porta atras de você se fecha.")
                    sleep(tempo)
                    print("Você pode ir para Cima ou Baixo")
                    sleep(tempo)
                    qualInimigo = inimigo()
                    qualItem = item(qualInimigo)
                    result = salas(player,qualInimigo,qualItem)
                    if result == "Vitoria":
                        print(player)
                        sleep(tempo)
                        print("Sala Limpa!")
                        sleep(tempo)
                        print("Você so pode ir para Cima ou Baixo")
                        sleep(tempo)
                        escolha = input("Qual lado você ira ?\n")
                        sleep(tempo)
                        while not(escolha == "Cima" or escolha == "Baixo"):
                            escolha = input("Você so pode ir para Cima ou Baixo\n")
                            sleep(tempo)
                        return escolha
                    else:
                        return "Acabou"
                elif lados == 2 and not(escolhaAnterior == "Baixo" or escolhaAnterior == "Esquerda"):
                    print("A porta atras de você se fecha.")
                    sleep(tempo)
                    print("Você pode ir para Cima ou Direita")
                    sleep(tempo)
                    qualInimigo = inimigo()
                    qualItem = item(qualInimigo)
                    result = salas(player,qualInimigo,qualItem)
                    if result == "Vitoria":
                        print(player)
                        sleep(tempo)
                        print("Sala Limpa!")
                        sleep(tempo)
                        print("Você so pode ir para Cima ou Direita")
                        sleep(tempo)
                        escolha = input("Qual lado você ira ?\n")
                        sleep(tempo)
                        while not(escolha == "Cima" or escolha == "Direita"):
                            escolha = input("Você so pode ir para Cima ou Direita\n")
                            sleep(tempo)
                        return escolha
                    else:
                        return "Acabou"
                elif lados == 3 and not(escolhaAnterior == "Baixo" or escolhaAnterior == "Direita"):
                    print("A porta atras de você se fecha.")
                    sleep(tempo)
                    print("Você pode ir para Cima ou Esquerda")
                    sleep(tempo)
                    qualInimigo = inimigo()
                    qualItem = item(qualInimigo)
                    result = salas(player,qualInimigo,qualItem)
                    if result == "Vitoria":
                        print(player)
                        sleep(tempo)
                        print("Sala Limpa!")
                        sleep(tempo)
                        print("Você so pode ir para Cima ou Esquerda")
                        sleep(tempo)
                        escolha = input("Qual lado você ira ?\n")
                        sleep(tempo)
                        while not(escolha == "Cima" or escolha == "Esquerda"):
                            escolha = input("Você so pode ir para Cima ou Esquerda\n")
                            sleep(tempo)
                        return escolha
                    else:
                        return "Acabou"
                elif lados == 4 and not(escolhaAnterior == "Cima" or escolhaAnterior == "Esquerda"):
                    print("A porta atras de você se fecha.")
                    sleep(tempo)
                    print("Você pode ir para Baixo ou Direita")
                    sleep(tempo)
                    qualInimigo = inimigo()
                    qualItem = item(qualInimigo)
                    result = salas(player,qualInimigo,qualItem)
                    if result == "Vitoria":
                        print(player)
                        sleep(tempo)
                        print("Sala Limpa!")
                        sleep(tempo)
                        print("Você so pode ir para Baixo ou Direita")
                        sleep(tempo)
                        escolha = input("Qual lado você ira ?\n")
                        sleep(tempo)
                        while not(escolha == "Baixo" or escolha == "Direita"):
                            escolha = input("Você so pode ir para Baixo ou Direita\n")
                            sleep(tempo)
                        return escolha
                    else:
                        return "Acabou"
                elif lados == 5 and not(escolhaAnterior == "Cima" or escolhaAnterior == "Direita"):
                    print("A porta atras de você se fecha.")
                    sleep(tempo)
                    print("Você pode ir para Baixo ou Esquerda")
                    sleep(tempo)
                    qualInimigo = inimigo()
                    qualItem = item(qualInimigo)
                    result = salas(player,qualInimigo,qualItem)
                    if result == "Vitoria":
                        print(player)
                        sleep(tempo)
                        print("Sala Limpa!")
                        sleep(tempo)
                        print("Você so pode ir para Baixo ou Esquerda")
                        sleep(tempo)
                        escolha = input("Qual lado você ira ?\n")
                        sleep(tempo)
                        while not(escolha == "Baixo" or escolha == "Esquerda"):
                            escolha = input("Você so pode ir para Baixo ou Esquerda\n")
                            sleep(tempo)
                        return escolha
                    else:
                        return "Acabou"
                elif lados == 6 and not(escolhaAnterior == "Esquerda" or escolhaAnterior == "Direita"):
                    print("A porta atras de você se fecha.")
                    sleep(tempo)
                    print("Você pode ir para Esquerda ou Direita")
                    sleep(tempo)
                    qualInimigo = inimigo()
                    qualItem = item(qualInimigo)
                    result = salas(player,qualInimigo,qualItem)
                    if result == "Vitoria":
                        print(player)
                        sleep(tempo)
                        print("Sala Limpa!")
                        sleep(tempo)
                        print("Você so pode ir para Esquerda ou Direita")
                        sleep(tempo)
                        escolha = input("Qual lado você ira ?\n")
                        sleep(tempo)
                        while not(escolha == "Esquerda" or escolha == "Direita"):
                            escolha = input("Você so pode ir para Esquerda ou Direita\n")
                            sleep(tempo)
                        return escolha
                    else:
                        return "Acabou"
        elif quantEscolhas == 3:
            while True:
                lados = randint(1,4)
                if lados == 1 and not(escolhaAnterior == "Cima" or escolhaAnterior == "Baixo" or escolhaAnterior == "Direita"):
                    print("A porta atras de você se fecha.")
                    sleep(tempo)
                    print("Você pode ir para Cima, Baixo ou Esquerda")
                    sleep(tempo)
                    qualInimigo = inimigo()
                    qualItem = item(qualInimigo)
                    result = salas(player,qualInimigo,qualItem)
                    if result == "Vitoria":
                        print(player)
                        sleep(tempo)
                        print("Sala Limpa!")
                        sleep(tempo)
                        print("Você so pode ir para Cima, Baixo ou Esquerda")
                        sleep(tempo)
                        escolha = input("Qual lado você ira ?\n")
                        sleep(tempo)
                        while not(escolha == "Cima" or escolha == "Baixo" or escolha == "Esquerda"):
                            escolha = input("Você so pode ir para Cima, Baixo ou Esquerda\n")
                            sleep(tempo)
                        return escolha
                    else:
                        return "Acabou"
                elif lados == 2 and not(escolhaAnterior == "Cima" or escolhaAnterior == "Baixo" or escolhaAnterior == "Esquerda"):
                    print("A porta atras de você se fecha.")
                    sleep(tempo)
                    print("Você pode ir para Cima, Baixo ou Direita")
                    sleep(tempo)
                    qualInimigo = inimigo()
                    qualItem = item(qualInimigo)
                    result = salas(player,qualInimigo,qualItem)
                    if result == "Vitoria":
                        print(player)
                        sleep(tempo)
                        print("Sala Limpa!")
                        sleep(tempo)
                        print("Você so pode ir para Cima, Baixo ou Direita")
                        sleep(tempo)
                        escolha = input("Qual lado você ira ?\n")
                        sleep(tempo)
                        while not(escolha == "Cima" or escolha == "Baixo" or escolha == "Direita"):
                            escolha = input("Você so pode ir para Cima, Baixo ou Direita\n")
                            sleep(tempo)
                        return escolha
                    else:
                        return "Acabou"
                elif lados == 3 and not(escolhaAnterior == "Direita" or escolhaAnterior == "Esquerda" or escolhaAnterior == "Baixo"):
                    print("A porta atras de você se fecha.")
                    sleep(tempo)
                    print("Você pode ir para Esquerda, Direita ou Cima")
                    sleep(tempo)
                    qualInimigo = inimigo()
                    qualItem = item(qualInimigo)
                    result = salas(player,qualInimigo,qualItem)
                    if result == "Vitoria":
                        print(player)
                        sleep(tempo)
                        print("Sala Limpa!")
                        sleep(tempo)
                        print("Você so pode ir para Esquerda, Direita ou Cima")
                        sleep(tempo)
                        escolha = input("Qual lado você ira ?\n")
                        sleep(tempo)
                        while not(escolha == "Direita" or escolha == "Esquerda" or escolha == "Cima"):
                            escolha = input("Você so pode ir para Esquerda, Direita ou Cima\n")
                            sleep(tempo)
                        return escolha
                    else:
                        return "Acabou"
                elif lados == 4 and not(escolhaAnterior == "Direita" or escolhaAnterior == "Esquerda" or escolhaAnterior == "Cima"):
                    print("A porta atras de você se fecha.")
                    sleep(tempo)
                    print("Você pode ir para Esquerda, Direita ou Baixo")
                    sleep(tempo)
                    qualInimigo = inimigo()
                    qualItem = item(qualInimigo)
                    result = salas(player,qualInimigo,qualItem)
                    if result == "Vitoria":
                        print(player)
                        sleep(tempo)
                        print("Sala Limpa!")
                        sleep(tempo)
                        print("Você so pode ir para Esquerda, Direita ou Baixo")
                        sleep(tempo)
                        escolha = input("Qual lado você ira ?\n")
                        sleep(tempo)
                        while not(escolha == "Esquerda" or escolha == "Direita" or escolha == "Baixo"):
                            escolha = input("Você so pode ir para Direita, Esquerda ou Baixo\n")
                            sleep(tempo)
                        return escolha
                    else:
                        return "Acabou"
nomePlayer = input("Insira um nome:\n")

player1 = {
    "Nome": nomePlayer,
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
