from random import randint
from time import sleep
def temItem(inimigo):
    itemSN = randint(1,5)
    if itemSN == 1 or itemSN == 2 or inimigo != "Nenhum":
        return "S"
    else:
        return "N"
def temInimigo():
    inimigoSN = randint(1,3)
    if inimigoSN == 1 or inimigoSN == 2:
        return "S"
    else:
        return "N"
def item(inimigo):
    qualItem = randint(0,3)
    qualVariacao = randint(0,2)
    if temItem(inimigo) == "S":
        if qualItem == 0:
            qualEspada = ["Espada de Madeira", "Espada de Ferro", "Dragon Slayer"]
            return qualEspada[qualVariacao]
        elif qualItem == 1:
            qualEscudo = ["Escudo de Madeira", "Escudo de Ferro", "Escudo Hylian"]
            return qualEscudo[qualVariacao]
        elif qualItem == 2:
            qualBota = ["Meia", "Bota de Couro", "Botas Espaciais"]
            return qualBota[qualVariacao]
        elif qualItem == 3:
            BO = ["Espada de Madeira Amaldiçoada","Escudo de Ferro Amaldiçoado","Meia Furada"]
            return BO[qualVariacao]
        elif qualItem == 4:
            pass  #ITENS RUINS ??
    else:
        return "Nenhum"
def inimigo(sala):
    qualInimigo = randint(0,3)
    if temInimigo() == "S":
        if sala <= 7:
            monstros = ["Slime", "Zumbi","Esqueleto","Aranha"]
            if qualInimigo == 0:
                return monstros[qualInimigo]
            elif qualInimigo == 1:
                return monstros[qualInimigo]
            elif qualInimigo == 2:
                return monstros[qualInimigo]
            else:
                return monstros[qualInimigo]
        elif sala > 7:
            monstros = ["Cavaleiro Negro", "Placeholder1","Placeholder2","Arquimago"]
            if qualInimigo == 0:
                return monstros[qualInimigo]
            elif qualInimigo == 1:
                return monstros[qualInimigo]
            elif qualInimigo == 2:
                return monstros[qualInimigo]
            else:
                return monstros[qualInimigo]
    else:
        return "Nenhum"
def aplicandoItem(player,item):
    if item == "Espada de Madeira":
        player["forca"] += 1
        
    elif item == "Espada de Ferro":
        player["forca"] += 2
        
    elif item == "Dragon Slayer":
        player["forca"] += 3
        
    elif item == "Escudo de Madeira":
        player["defesa"] += 2
        
    elif item == "Escudo de Ferro":
        player["defesa"] += 3
        
    elif item == "Escudo Hylian":
        player["defesa"] += 5
        
    elif item == "Meia":
        player["fuga"] += 1
        
    elif item == "Bota de Couro":
        player["fuga"] += 2
        
    elif item == "Botas Espaciais":
        player["fuga"] += 3
        
    elif item == "Espada de Madeira Amaldiçoada":
        player["forca"] += 3
        player["defesa"] -= 1
        player["fuga"] -= 1

    elif item == "Escudo de Ferro Amaldiçoado":
        player["defesa"] += 3
        player["forca"] -= 1
        player["fuga"] -= 1

    elif item == "Meia Furada":
        player["fuga"] += 4
        player["forca"] -= 2
        player["defesa"] -= 2   
def batalha(player, monstro):
    tempo = 1
    if monstro == "Slime":
        mob ={
            "Nome": "Slime",
            "forca": 1,
            "defesa": 2
        }
        while (player["defesa"] >= 0 or mob["defesa"] >= 0):
            print(f"{player['Nome']} X {mob['Nome']}")
            sleep(tempo)
            player["defesa"] -= mob["forca"]
            if player["defesa"] <= 0:
                player["defesa"] = 0
                print(f"{player['Nome']} defesa: {player['defesa']}")
                sleep(tempo)
                print(f"{mob['Nome']} defesa: {mob['defesa']}")
                sleep(tempo)
                return "GameOver"
            print(f"{player['Nome']} defesa: {player['defesa']}")
            sleep(tempo)
            mob["defesa"] -= player["forca"]
            if mob["defesa"] <= 0:
                mob["defesa"] = 0
                print(f"{mob['Nome']} defesa: {mob['defesa']}")
                sleep(tempo)
                return "Vitoria"
            print(f"{mob['Nome']} defesa: {mob['defesa']}")
            sleep(tempo)           
    elif monstro == "Zumbi":
        mob ={
            "Nome": "Zumbi",
            "forca": 2,
            "defesa": 3
        }
        while (player["defesa"] >= 0 or mob["defesa"] >= 0):
            print(f"{player['Nome']} X {mob['Nome']}")
            sleep(tempo)
            player["defesa"] -= mob["forca"]
            if player["defesa"] <= 0:
                player["defesa"] = 0
                print(f"{player['Nome']} defesa: {player['defesa']}")
                sleep(tempo)
                print(f"{mob['Nome']} defesa: {mob['defesa']}")
                sleep(tempo)
                return "GameOver"
            print(f"{player['Nome']} defesa: {player['defesa']}")
            sleep(tempo)
            mob["defesa"] -= player["forca"]
            if mob["defesa"] <= 0:
                mob["defesa"] = 0
                print(f"{mob['Nome']} defesa: {mob['defesa']}")
                sleep(tempo)
                return "Vitoria"
            print(f"{mob['Nome']} defesa: {mob['defesa']}")
            sleep(tempo)
    elif monstro == "Esqueleto":
        mob ={
            "Nome": "Esqueleto",
            "forca": 3,
            "defesa": 3
        }
        while (player["defesa"] >= 0 or mob["defesa"] >= 0):
            print(f"{player['Nome']} X {mob['Nome']}")
            sleep(tempo)
            player["defesa"] -= mob["forca"]
            if player["defesa"] <= 0:
                player["defesa"] = 0
                print(f"{player['Nome']} defesa: {player['defesa']}")
                sleep(tempo)
                print(f"{mob['Nome']} defesa: {mob['defesa']}")
                sleep(tempo)
                return "GameOver"
            print(f"{player['Nome']} defesa: {player['defesa']}")
            sleep(tempo)
            mob["defesa"] -= player["forca"]
            if mob["defesa"] <= 0:
                mob["defesa"] = 0
                print(f"{mob['Nome']} defesa: {mob['defesa']}")
                sleep(tempo)
                return "Vitoria"
            print(f"{mob['Nome']} defesa: {mob['defesa']}")
            sleep(tempo)
    elif monstro == "Aranha":
        mob ={
            "Nome": "Aranha",
            "forca": 3,
            "defesa": 4
        }
        while (player["defesa"] >= 0 or mob["defesa"] >= 0):
            print(f"{player['Nome']} X {mob['Nome']}")
            sleep(tempo)
            player["defesa"] -= mob["forca"]
            if player["defesa"] <= 0:
                player["defesa"] = 0
                print(f"{player['Nome']} defesa: {player['defesa']}")
                sleep(tempo)
                print(f"{mob['Nome']} defesa: {mob['defesa']}")
                sleep(tempo)
                return "GameOver"
            print(f"{player['Nome']} defesa: {player['defesa']}")
            sleep(tempo)
            mob["defesa"] -= player["forca"]
            if mob["defesa"] <= 0:
                mob["defesa"] = 0
                print(f"{mob['Nome']} defesa: {mob['defesa']}")
                sleep(tempo)
                return "Vitoria"
            print(f"{mob['Nome']} defesa: {mob['defesa']}")
            sleep(tempo)
    elif monstro == "Cavaleiro Negro":
        mob ={
            "Nome": "Espadachim Negro",
            "forca": 4,
            "defesa": 4
        }
        sleep(tempo)
        print(f"Nome: {mob['Nome']}")
        sleep(tempo)
        print(f"forca: {mob['forca']}")
        sleep(tempo)
        print(f"defesa: {mob['defesa']}")
        sleep(tempo)
        while (player["defesa"] >= 0 or mob["defesa"] >= 0):
            print(f"{player['Nome']} X {mob['Nome']}")
            sleep(tempo)
            player["defesa"] -= mob["forca"]
            if player["defesa"] <= 0:
                player["defesa"] = 0
                print(f"{player['Nome']} defesa: {player['defesa']}")
                sleep(tempo)
                print(f"{mob['Nome']} defesa: {mob['defesa']}")
                sleep(tempo)
                return "GameOver"
            print(f"{player['Nome']} defesa: {player['defesa']}")
            sleep(tempo)
            mob["defesa"] -= player["forca"]
            if mob["defesa"] <= 0:
                mob["defesa"] = 0
                print(f"{mob['Nome']} defesa: {mob['defesa']}")
                sleep(tempo)
                return "Vitoria"
            print(f"{mob['Nome']} defesa: {mob['defesa']}")
            sleep(tempo)
    elif monstro == "Placeholder1":
        mob ={
            "Nome": "Placeholder1",
            "forca": 3,
            "defesa": 5
        }
        sleep(tempo)
        print(f"Nome: {mob['Nome']}")
        sleep(tempo)
        print(f"forca: {mob['forca']}")
        sleep(tempo)
        print(f"defesa: {mob['defesa']}")
        sleep(tempo)
        while (player["defesa"] >= 0 or mob["defesa"] >= 0):
            print(f"{player['Nome']} X {mob['Nome']}")
            sleep(tempo)
            player["defesa"] -= mob["forca"]
            if player["defesa"] <= 0:
                player["defesa"] = 0
                print(f"{player['Nome']} defesa: {player['defesa']}")
                sleep(tempo)
                print(f"{mob['Nome']} defesa: {mob['defesa']}")
                sleep(tempo)
                return "GameOver"
            print(f"{player['Nome']} defesa: {player['defesa']}")
            sleep(tempo)
            mob["defesa"] -= player["forca"]
            if mob["defesa"] <= 0:
                mob["defesa"] = 0
                print(f"{mob['Nome']} defesa: {mob['defesa']}")
                sleep(tempo)
                return "Vitoria"
            print(f"{mob['Nome']} defesa: {mob['defesa']}")
            sleep(tempo)
    elif monstro == "Placeholder2":
        mob ={
            "Nome": "Placeholder2",
            "forca": 4,
            "defesa": 5
        }
        sleep(tempo)
        print(f"Nome: {mob['Nome']}")
        sleep(tempo)
        print(f"forca: {mob['forca']}")
        sleep(tempo)
        print(f"defesa: {mob['defesa']}")
        sleep(tempo)
        while (player["defesa"] >= 0 or mob["defesa"] >= 0):
            print(f"{player['Nome']} X {mob['Nome']}")
            sleep(tempo)
            player["defesa"] -= mob["forca"]
            if player["defesa"] <= 0:
                player["defesa"] = 0
                print(f"{player['Nome']} defesa: {player['defesa']}")
                sleep(tempo)
                print(f"{mob['Nome']} defesa: {mob['defesa']}")
                sleep(tempo)
                return "GameOver"
            print(f"{player['Nome']} defesa: {player['defesa']}")
            sleep(tempo)
            mob["defesa"] -= player["forca"]
            if mob["defesa"] <= 0:
                mob["defesa"] = 0
                print(f"{mob['Nome']} defesa: {mob['defesa']}")
                sleep(tempo)
                return "Vitoria"
            print(f"{mob['Nome']} defesa: {mob['defesa']}")
            sleep(tempo)
    elif monstro == "Arquimago":
        mob ={
            "Nome": "Arquimago",
            "forca": 6,
            "defesa": 2
        }
        sleep(tempo)
        print(f"Nome: {mob['Nome']}")
        sleep(tempo)
        print(f"forca: {mob['forca']}")
        sleep(tempo)
        print(f"defesa: {mob['defesa']}")
        sleep(tempo)
        while (player["defesa"] >= 0 or mob["defesa"] >= 0):
            print(f"{player['Nome']} X {mob['Nome']}")
            sleep(tempo)
            player["defesa"] -= mob["forca"]
            if player["defesa"] <= 0:
                player["defesa"] = 0
                print(f"{player['Nome']} defesa: {player['defesa']}")
                sleep(tempo)
                print(f"{mob['Nome']} defesa: {mob['defesa']}")
                sleep(tempo)
                return "GameOver"
            print(f"{player['Nome']} defesa: {player['defesa']}")
            sleep(tempo)
            mob["defesa"] -= player["forca"]
            if mob["defesa"] <= 0:
                mob["defesa"] = 0
                print(f"{mob['Nome']} defesa: {mob['defesa']}")
                sleep(tempo)
                return "Vitoria"
            print(f"{mob['Nome']} defesa: {mob['defesa']}")
            sleep(tempo)
def fuga(player,monstro):
    mob = monstro
    if mob == "Slime":
        slime = {
            "fuga": 4
        }
        if player["fuga"] >= slime["fuga"]:
            return "fugiu"
        elif player["fuga"] <= slime["fuga"]:
            fugir = randint(1,5)
            if fugir <= 4:
                return "fugiu"
            else:
                return "falha"
    elif mob == "Zumbi":
        zumbi = {
            "fuga": 5
        }
        if player["fuga"] >= zumbi["fuga"]:
            return "fugiu"
        elif player["fuga"] <= zumbi["fuga"]:
            fugir = randint(1,5)
            if fugir <= 3:
                return "fugiu"
            else:
                return "falha"
    elif mob == "Esqueleto":
        esqueleto = {
            "fuga": 6
        }
        if player["fuga"] >= esqueleto["fuga"]:
            return "fugiu"
        elif player["fuga"] <= esqueleto["fuga"]:
            fugir = randint(1,5)
            if fugir <= 2:
                return "fugiu"
            else:
                return "falha"
    elif mob == "Aranha":
        aranha = {
            "fuga": 7
        }
        if player["fuga"] >= aranha["fuga"]:
            return "fugiu"
        elif player["fuga"] <= aranha["fuga"]:
            fugir = randint(1,5)
            if fugir == 1:
                return "fugiu"
            else:
                return "falha"  
    elif mob == "Cavaleiro Negro":
        cavaleiroNegro = {
            "fuga": 8
        }
        if player["fuga"] >= cavaleiroNegro["fuga"]:
            return "fugiu"
        elif player["fuga"] <= cavaleiroNegro["fuga"]:
            fugir = randint(1,5)
            if fugir >= 4:
                return "fugiu"
            else:
                return "falha" 
    elif mob == "Placeholder1":
        placeholder1 = {
            "fuga": 9
        }
        if player["fuga"] >= placeholder1["fuga"]:
            return "fugiu"
        elif player["fuga"] <= placeholder1["fuga"]:
            fugir = randint(1,5)
            if fugir >= 4:
                return "fugiu"
            else:
                return "falha" 
    elif mob == "Placeholder2":
        placeholder2 = {
            "fuga": 9
        }
        if player["fuga"] >= placeholder2["fuga"]:
            return "fugiu"
        elif player["fuga"] <= placeholder2["fuga"]:
            fugir = randint(1,5)
            if fugir >= 4:
                return "fugiu"
            else:
                return "falha" 
    elif mob == "Arquimago":
        arquiMago = {
            "fuga": 10
        }
        if player["fuga"] >= arquiMago["fuga"]:
            return "fugiu"
        elif player["fuga"] <= arquiMago["fuga"]:
            fugir = randint(1,5)
            if fugir >= 4:
                return "fugiu"
            else:
                return "falha" 
def qualBoss():
    escolhaDeBoss = randint(0,2)
    bosses = ["Locus", "Grunbeld","Zodd"]
    if escolhaDeBoss == 0:
        return bosses[escolhaDeBoss]
    elif escolhaDeBoss == 1:
        return bosses[escolhaDeBoss]
    else:
        return bosses[escolhaDeBoss]
def batalhaBoss(player,boss):
    tempo = 1.5
    if boss == "Locus":
        chefe = {
            "Nome": "Locus, Moonlight Knight",
            "forca": 8,
            "defesa": 7
        }
        sleep(tempo)
        print(f"Nome: {chefe['Nome']}")
        sleep(tempo)
        print(f"forca: {chefe['forca']}")
        sleep(tempo)
        print(f"defesa: {chefe['defesa']}")
        sleep(tempo)

        print("Lute ou morra para Locus")
        sleep(tempo)
        acao = input("Você ira lutar ou tentar fugir ?")  #Inputs esperados lutar/fugir
        sleep(tempo)
        tentativa = 0  #Variavel contador
        while acao.lower() != "lutar":
            if tentativa < 2:
                print("Lute ou morra")
                sleep(tempo)
                acao = input("Você ira lutar ou tentar fugir ?")
                sleep(tempo)
                tentativa += 1
            elif tentativa == 2:
                print("Você tentou correr")
                sleep(tempo)
                player["defesa"] = 0
                return player["defesa"]
        if acao.lower() == "lutar":
            print(f"{player['Nome']} X {chefe['Nome']}")
            while (player["defesa"] >= 0 or chefe["defesa"] >= 0):
                sleep(tempo)
                player["defesa"] -= chefe["forca"]
                if player["defesa"] <= 0:
                    player["defesa"] = 0
                    print(f"{player['Nome']} defesa: {player['defesa']}")
                    sleep(tempo)
                    print(f"Locus defesa: {chefe['defesa']}")
                    sleep(tempo)
                    print("Fraco")
                    sleep(tempo)
                    return player["defesa"]
                print(f"{player['Nome']} defesa: {player['defesa']}")
                sleep(tempo)
                chefe["defesa"] -= player["forca"]
                if chefe["defesa"] <= 0:
                    chefe["defesa"] = 0
                    print(f"Locus defesa: {chefe['defesa']}")
                    sleep(tempo)
                    return player["defesa"]
                print(f"Locus defesa: {chefe['defesa']}")
                sleep(tempo)

    elif boss == "Grunbeld":
        chefe = {
            "Nome": "Grunbeld, The Great Flame Dragon",
            "forca": 6,
            "defesa": 14
        }
        sleep(tempo)
        print(f"Nome: {chefe['Nome']}")
        sleep(tempo)
        print(f"forca: {chefe['forca']}")
        sleep(tempo)
        print(f"defesa: {chefe['defesa']}")
        sleep(tempo)

        print("Lute ou morra para Grunbeld")
        sleep(tempo)
        acao = input("Você ira lutar ou tentar fugir ?")  #Inputs esperados lutar/fugir
        sleep(tempo)
        tentativa = 0  #Variavel contador
        while acao.lower() != "lutar":
            if tentativa < 2:
                print("Lute ou morra")
                sleep(tempo)
                acao = input("Você ira lutar ou tentar fugir ?")
                sleep(tempo)
                tentativa += 1
            elif tentativa == 2:
                print("Você tentou correr")
                sleep(tempo)
                player["defesa"] = 0
                return player["defesa"]
        if acao.lower() == "lutar":
            print(f"{player['Nome']} X {chefe['Nome']}")
            while (player["defesa"] >= 0 or chefe["defesa"] >= 0):
                sleep(tempo)
                player["defesa"] -= chefe["forca"]
                print(f"{player['Nome']} defesa: {player['defesa']}")
                chefe["defesa"] -= player["forca"]
                print(f"Grunbeld defesa: {chefe['defesa']}")
                if player["defesa"] >= 0 and chefe["defesa"] <= 0:
                    return player["defesa"]
                elif chefe["defesa"] >= 0 and player["defesa"] <= 0:
                    print("Fraco")
                    sleep(tempo)
                    player["defesa"] = 0
                    return player["defesa"]

    elif boss == "Zodd":
        chefe = {
            "Nome": "Nosferatu Zodd, The Immortal",
            "forca": 9,
            "defesa": 12
        }
        sleep(tempo)
        print(f"Nome: {chefe['Nome']}")
        sleep(tempo)
        print(f"forca: {chefe['forca']}")
        sleep(tempo)
        print(f"defesa: {chefe['defesa']}")
        sleep(tempo)

        print("Lute ou morra para Zodd")
        sleep(tempo)
        acao = input("Você ira lutar ou tentar fugir ?")  #Inputs esperados lutar/fugir
        sleep(tempo)
        tentativa = 0  #Variavel contador
        while acao.lower() != "lutar":
            if tentativa < 2:
                print("Lute ou morra")
                sleep(tempo)
                acao = input("Você ira lutar ou tentar fugir ?")
                sleep(tempo)
                tentativa += 1
            elif tentativa == 2:
                print("Você tentou correr")
                sleep(tempo)
                player["defesa"] = 0
                return player["defesa"]
        if acao.lower() == "lutar":
            print(f"{player['Nome']} X {chefe['Nome']}")
            while (player["defesa"] >= 0 or chefe["defesa"] >= 0):
                sleep(tempo)
                player["defesa"] -= chefe["forca"]
                print(f"{player['Nome']} defesa: {player['defesa']}")
                chefe["defesa"] -= player["forca"]
                print(f"Zodd defesa: {chefe['defesa']}")
                if player["defesa"] >= 0 and chefe["defesa"] <= 0:
                    return player["defesa"]
                elif chefe["defesa"] >= 0 and player["defesa"] <= 0:
                    print("Fraco")
                    sleep(tempo)
                    player["defesa"] = 0
                    return player["defesa"]
def salas(player,inimigo,item): 
    tempo = 1
    resultado = ""
    print(f"Monstro na sala: {inimigo}")
    sleep(tempo)
    print(f"Item na sala: {item}")
    sleep(tempo)
    while not(inimigo == "Nenhum" and item == "Nenhum"):
        if inimigo != "Nenhum":
            lutar = input("Lutar contra o Monstro ou tentar Fugir ?\n")   #Input esperado lutar/fugir
            sleep(tempo)
            while not(lutar.lower() != "lutar" or lutar.lower() != "fugir"):
                lutar = input("Lutar ou Fugir\n")
                sleep(tempo)
            if lutar.lower() == "lutar":
                resultado = batalha(player,inimigo)
                inimigo = "Nenhum"
            elif lutar.lower() == "fugir":
                fugir = fuga(player, inimigo)
                if fugir == "fugiu":
                    print("Você conseguiu fugir")
                    sleep(tempo)
                    inimigo = "Nenhum"
                elif fugir == "falha":
                    print("Você não conseguiu fugir, Seu status de fuga caiu para 0")
                    sleep(tempo)
                    player["fuga"] = 0
        if player["defesa"] <= 0 :
            print("Você perdeu")
            input()
            return "Derrota"
        if resultado == "Vitoria" or inimigo == "Nenhum":
            if item != "Nenhum":
                usar = input("Usar item: S/N\n")
                sleep(tempo)
                while not(usar.lower() == "s" or usar.lower() == "n"):
                    usar = input("Usar item: S/N\n")
                    sleep(tempo)
                if usar.lower() == "s":
                    aplicandoItem(player, item)
                    item = "Nenhum"
                elif usar.lower() == "n":
                    item = "Nenhum"
    return "Vitoria"