from funcoes import item, inimigo, qualBoss, batalhaBoss, salas, addStatus, fogueira
from random import randint
from time import sleep
def jogar():
    def quantidadeDeEscolhas(player, sala, escolhaAnterior):
        while True:
            quantEscolhas = randint(1,7)
            tempo = 1
            if sala == 0:
                texto = '"Tudo veio do fogo e tudo retornara ao fogo - Eraclito"\n'
                tempoTexto = 0.1
                for i in texto:
                    print(i, end='', flush=True)
                    sleep(tempoTexto)
                sleep(tempo)
                print("Você esta na sala principal.")
                sleep(tempo)
                print("Você segue para unica porta aberta")
                sleep(tempo)
                return "Nenhum"
            elif quantEscolhas == 7 and sala > 13:
                print("\nA porta atras de você se fecha.")
                sleep(tempo)
                print("Não a nenhuma porta aberta.")
                sleep(tempo)
                print("Você chegou a sala do boss")
                sleep(tempo)
                
                boss = qualBoss()
                print(f"Boss da sala: {boss}\n")
                sleep(tempo)

                batalhaBoss(player, boss)
                if player["defesa"] > 0:
                    sleep(tempo)
                    print(f"\nVocê derrotou o BOSS: {boss}!!!")
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
                        print("\nA porta atras de você se fecha.")
                        sleep(tempo)
                        print("Você pode apenas ir para Cima")
                        sleep(tempo)
                        qualInimigo = inimigo(sala)
                        qualItem = item(qualInimigo)
                        result = salas(player,qualInimigo,qualItem)
                        if result == "Vitoria":
                            fogueira(player,sala)
                            print("Você so pode ir para Cima")
                            sleep(tempo)
                            escolha = input("Qual lado você ira ?\n")
                            
                            while escolha != "Cima":
                                sleep(tempo)
                                escolha = input("Você so pode ir para Cima\n")
                                
                            return escolha
                        else:
                            return "Acabou"
                    elif lados == 2 and not(escolhaAnterior == "Cima"):
                        print("\nA porta atras de você se fecha.")
                        sleep(tempo)
                        print("Você pode apenas ir para Baixo")
                        sleep(tempo)
                        qualInimigo = inimigo(sala)
                        qualItem = item(qualInimigo)
                        result = salas(player,qualInimigo,qualItem)
                        if result == "Vitoria":
                            fogueira(player,sala)
                            print("Você so pode ir para Baixo")
                            sleep(tempo)
                            escolha = input("Qual lado você ira ?\n")
                            
                            while escolha != "Baixo":
                                sleep(tempo)
                                escolha = input("Você so pode ir para Baixo\n")
                                
                            return escolha
                        else:
                            return "Acabou"
                    elif lados == 3 and not(escolhaAnterior == "Direita"):
                        print("\nA porta atras de você se fecha.")
                        sleep(tempo)
                        print("Você pode apenas ir para Esquerda")
                        sleep(tempo)
                        qualInimigo = inimigo(sala)
                        qualItem = item(qualInimigo)
                        result = salas(player,qualInimigo,qualItem)
                        if result == "Vitoria":
                            fogueira(player,sala)
                            print("Você so pode ir para Esquerda")
                            sleep(tempo)
                            escolha = input("Qual lado você ira ?\n")
                            
                            while escolha != "Esquerda":
                                sleep(tempo)
                                escolha = input("Você so pode ir para Esquerda\n")  
                                        
                            return escolha
                        else:
                            return "Acabou"
                    elif lados == 4 and not(escolhaAnterior == "Esquerda"):
                        print("\nA porta atras de você se fecha.")
                        sleep(tempo)
                        print("Você pode apenas ir para Direita")
                        sleep(tempo)
                        qualInimigo = inimigo(sala)
                        qualItem = item(qualInimigo)
                        result = salas(player,qualInimigo,qualItem)
                        if result == "Vitoria":
                            fogueira(player,sala)
                            print("Você so pode ir para Direita")
                            sleep(tempo)
                            escolha = input("Qual lado você ira ?\n")
                            
                            while escolha != "Direita":
                                sleep(tempo)
                                escolha = input("Você so pode ir para Direita\n")
                                
                            return escolha
                        else:
                            return "Acabou"  
            elif quantEscolhas == 2:
                while True:
                    lados = randint(1,6)
                    if lados == 1 and not(escolhaAnterior == "Cima" or escolhaAnterior == "Baixo"):
                        print("\nA porta atras de você se fecha.")
                        sleep(tempo)
                        print("Você pode ir para Cima ou Baixo")
                        sleep(tempo)
                        qualInimigo = inimigo(sala)
                        qualItem = item(qualInimigo)
                        result = salas(player,qualInimigo,qualItem)
                        if result == "Vitoria":
                            fogueira(player,sala)
                            print("Você so pode ir para Cima ou Baixo")
                            sleep(tempo)
                            escolha = input("Qual lado você ira ?\n")
                            
                            while not(escolha == "Cima" or escolha == "Baixo"):
                                sleep(tempo)
                                escolha = input("Você so pode ir para Cima ou Baixo\n")
                                
                            return escolha
                        else:
                            return "Acabou"
                    elif lados == 2 and not(escolhaAnterior == "Baixo" or escolhaAnterior == "Esquerda"):
                        print("\nA porta atras de você se fecha.")
                        sleep(tempo)
                        print("Você pode ir para Cima ou Direita")
                        sleep(tempo)
                        qualInimigo = inimigo(sala)
                        qualItem = item(qualInimigo)
                        result = salas(player,qualInimigo,qualItem)
                        if result == "Vitoria":
                            fogueira(player,sala)
                            print("Você so pode ir para Cima ou Direita")
                            sleep(tempo)
                            escolha = input("Qual lado você ira ?\n")
                        
                            while not(escolha == "Cima" or escolha == "Direita"):
                                sleep(tempo)
                                escolha = input("Você so pode ir para Cima ou Direita\n")
                                
                            return escolha
                        else:
                            return "Acabou"
                    elif lados == 3 and not(escolhaAnterior == "Baixo" or escolhaAnterior == "Direita"):
                        print("\nA porta atras de você se fecha.")
                        sleep(tempo)
                        print("Você pode ir para Cima ou Esquerda")
                        sleep(tempo)
                        qualInimigo = inimigo(sala)
                        qualItem = item(qualInimigo)
                        result = salas(player,qualInimigo,qualItem)
                        if result == "Vitoria":
                            fogueira(player,sala)
                            print("Você so pode ir para Cima ou Esquerda")
                            sleep(tempo)
                            escolha = input("Qual lado você ira ?\n")
                            
                            while not(escolha == "Cima" or escolha == "Esquerda"):
                                sleep(tempo)
                                escolha = input("Você so pode ir para Cima ou Esquerda\n")
                                
                            return escolha
                        else:
                            return "Acabou"
                    elif lados == 4 and not(escolhaAnterior == "Cima" or escolhaAnterior == "Esquerda"):
                        print("\nA porta atras de você se fecha.")
                        sleep(tempo)
                        print("Você pode ir para Baixo ou Direita")
                        sleep(tempo)
                        qualInimigo = inimigo(sala)
                        qualItem = item(qualInimigo)
                        result = salas(player,qualInimigo,qualItem)
                        if result == "Vitoria":
                            fogueira(player,sala)
                            print("Você so pode ir para Baixo ou Direita")
                            sleep(tempo)
                            escolha = input("Qual lado você ira ?\n")
                            
                            while not(escolha == "Baixo" or escolha == "Direita"):
                                sleep(tempo)
                                escolha = input("Você so pode ir para Baixo ou Direita\n")
                            
                            return escolha
                        else:
                            return "Acabou"
                    elif lados == 5 and not(escolhaAnterior == "Cima" or escolhaAnterior == "Direita"):
                        print("\nA porta atras de você se fecha.")
                        sleep(tempo)
                        print("Você pode ir para Baixo ou Esquerda")
                        sleep(tempo)
                        qualInimigo = inimigo(sala)
                        qualItem = item(qualInimigo)
                        result = salas(player,qualInimigo,qualItem)
                        if result == "Vitoria":
                            fogueira(player,sala)
                            print("Você so pode ir para Baixo ou Esquerda")
                            sleep(tempo)
                            escolha = input("Qual lado você ira ?\n")
                        
                            while not(escolha == "Baixo" or escolha == "Esquerda"):
                                sleep(tempo)
                                escolha = input("Você so pode ir para Baixo ou Esquerda\n")
                                
                            return escolha
                        else:
                            return "Acabou"
                    elif lados == 6 and not(escolhaAnterior == "Esquerda" or escolhaAnterior == "Direita"):
                        print("\nA porta atras de você se fecha.")
                        sleep(tempo)
                        print("Você pode ir para Esquerda ou Direita")
                        sleep(tempo)
                        qualInimigo = inimigo(sala)
                        qualItem = item(qualInimigo)
                        result = salas(player,qualInimigo,qualItem)
                        if result == "Vitoria":
                            fogueira(player,sala)
                            print("Você so pode ir para Esquerda ou Direita")
                            sleep(tempo)
                            escolha = input("Qual lado você ira ?\n")
                            while not(escolha == "Esquerda" or escolha == "Direita"):
                                sleep(tempo)
                                escolha = input("Você so pode ir para Esquerda ou Direita\n")
                                
                            return escolha
                        else:
                            return "Acabou"
            elif quantEscolhas == 3:
                while True:
                    lados = randint(1,4)
                    if lados == 1 and not(escolhaAnterior == "Cima" or escolhaAnterior == "Baixo" or escolhaAnterior == "Direita"):
                        print("\nA porta atras de você se fecha.")
                        sleep(tempo)
                        print("Você pode ir para Cima, Baixo ou Esquerda")
                        sleep(tempo)
                        qualInimigo = inimigo(sala)
                        qualItem = item(qualInimigo)
                        result = salas(player,qualInimigo,qualItem)
                        if result == "Vitoria":
                            fogueira(player,sala)
                            print("Você so pode ir para Cima, Baixo ou Esquerda")
                            sleep(tempo)
                            escolha = input("Qual lado você ira ?\n")
                            
                            while not(escolha == "Cima" or escolha == "Baixo" or escolha == "Esquerda"):
                                sleep(tempo)
                                escolha = input("Você so pode ir para Cima, Baixo ou Esquerda\n")
                                
                            return escolha
                        else:
                            return "Acabou"
                    elif lados == 2 and not(escolhaAnterior == "Cima" or escolhaAnterior == "Baixo" or escolhaAnterior == "Esquerda"):
                        print("\nA porta atras de você se fecha.")
                        sleep(tempo)
                        print("Você pode ir para Cima, Baixo ou Direita")
                        sleep(tempo)
                        qualInimigo = inimigo(sala)
                        qualItem = item(qualInimigo)
                        result = salas(player,qualInimigo,qualItem)
                        if result == "Vitoria":
                            fogueira(player,sala)
                            print("Você so pode ir para Cima, Baixo ou Direita")
                            sleep(tempo)
                            escolha = input("Qual lado você ira ?\n")
    
                            while not(escolha == "Cima" or escolha == "Baixo" or escolha == "Direita"):
                                sleep(tempo)
                                escolha = input("Você so pode ir para Cima, Baixo ou Direita\n")
                                
                            return escolha
                        else:
                            return "Acabou"
                    elif lados == 3 and not(escolhaAnterior == "Direita" or escolhaAnterior == "Esquerda" or escolhaAnterior == "Baixo"):
                        print("\nA porta atras de você se fecha.")
                        sleep(tempo)
                        print("Você pode ir para Esquerda, Direita ou Cima")
                        sleep(tempo)
                        qualInimigo = inimigo(sala)
                        qualItem = item(qualInimigo)
                        result = salas(player,qualInimigo,qualItem)
                        if result == "Vitoria":
                            fogueira(player,sala)
                            print("Você so pode ir para Esquerda, Direita ou Cima")
                            sleep(tempo)
                            escolha = input("Qual lado você ira ?\n")
                            
                            while not(escolha == "Direita" or escolha == "Esquerda" or escolha == "Cima"):
                                sleep(tempo)
                                escolha = input("Você so pode ir para Esquerda, Direita ou Cima\n")
                                
                            return escolha
                        else:
                            return "Acabou"
                    elif lados == 4 and not(escolhaAnterior == "Direita" or escolhaAnterior == "Esquerda" or escolhaAnterior == "Cima"):
                        print("\nA porta atras de você se fecha.")
                        sleep(tempo)
                        print("Você pode ir para Esquerda, Direita ou Baixo")
                        sleep(tempo)
                        qualInimigo = inimigo(sala)
                        qualItem = item(qualInimigo)
                        result = salas(player,qualInimigo,qualItem)
                        if result == "Vitoria":
                            fogueira(player,sala)
                            print("Você so pode ir para Esquerda, Direita ou Baixo")
                            sleep(tempo)
                            escolha = input("Qual lado você ira ?\n")
                            
                            while not(escolha == "Esquerda" or escolha == "Direita" or escolha == "Baixo"):
                                sleep(tempo)
                                escolha = input("Você so pode ir para Direita, Esquerda ou Baixo\n")
                                
                            return escolha
                        else:
                            return "Acabou"
    player1 = {
        "Nome": input("Insira um nome:\n"),
        "forca": 0,
        "defesa": 0,
        "fuga": 0
    }
    addStatus(player1)
    escolha = "Nenhum"
    contSala = 0
    tempo = 1.5
    while escolha == "Nenhum" or escolha == "Cima" or escolha == "Baixo" or escolha == "Esquerda" or escolha == "Direita":
        escolhaAnterior = escolha
        escolha = quantidadeDeEscolhas(player1, contSala, escolhaAnterior)
        sleep(tempo)
        contSala += 1