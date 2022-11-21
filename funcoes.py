from random import randint
from time import sleep
def menu():
    tempo = 1
    sleep(tempo) #Menu simples apenas prints
    print(f"-------------------")
    sleep(tempo)
    print(f"-  TerminalSouls  -")   #A DECIDIR
    sleep(tempo)
    print(f"-------------------")
    sleep(tempo)
    print(f"- 1.   Jogar      -")
    sleep(tempo)
    print(f"- 2.   Livro      -")
    sleep(tempo)
    print(f"- 3. Instruções   -")
    sleep(tempo)
    print(f"- 4.  Creditos    -")
    sleep(tempo)
    print(f"- 0.   Sair       -")
    sleep(tempo)
    print(f"-------------------\n")
    sleep(tempo)
def instrucoes():
    tempo = 1 #Apresentação de como funciona o jogo
    sleep(tempo)
    print(f"-O jogo tem como objetivo garantir uma experiencia diferente a cada Execução-")
    sleep(tempo)
    print(f"-19 Itens que aparecem aleatoriamente-")
    sleep(tempo)
    print(f"-8 Monstros que aparecem aleatoriamente-")
    sleep(tempo)
    print(f"-A 3 Chefes diferentes-")
    sleep(tempo)
    input()
def mostrarLista(lista):
    tempo = 0.8
    sleep(tempo)
    print("\n______________________________")
    sleep(tempo)
    for i in range (len(lista)):
            sleep(tempo)
            print(f"[{i + 1}] {lista[i]} ")
    sleep(tempo)
    print("______________________________\n")
    sleep(tempo)
def livro():
    #Apresentação de mobs e itens
    tempo = 0.8
    itensDano = ["Espada de Ferro", "Alucard Sword", "Master Sword", "Laminas do Caos", "Dragon Slayer", "Espada de Madeira Amaldiçoada"]
    itensDefesa = ["Escudo de Madeira", "Escudo de Randuin", "Alucard Mail", "Escudo Hylian", "Berserk Armor", "Armadura de Warmog", "Escudo de Ferro Amaldiçoado"]
    itensFuga = ["Meia", "Botas Galvanizadas de Aço", "Passos de Mercurio","Bota de Couro", "Botas Espaciais", "Meia Furada"]
    itensConsumiveis = ["Pedra de amolar quebrada","Maçã envenenada","Poção de Veneno","Poção de Fraqueza","Poção de Lentidão","Anel Amaldiçoado","Anel da Paralisia"]
    monstros = ["Slime", "Rato", "Morto-vivo", "Esqueleto","Arqueiro Esqueleto", "Esqueleto Gigante","Arqueiro Esqueleto Gigante","Wheel Skeletons", "Black Knight", "Demonio Corvo", "Sif", "Arquimago"]
    while True:
        escolha = input("\nVocê quer olhar Itens, Monstros ou Sair?   (itens/monstros/sair)\n")
        while not(escolha.lower() == "itens" or escolha.lower() == "monstros" or escolha.lower() == "sair"):
            print("Escolha invalida")
            escolha = input("\nVocê quer olhar Itens, Monstros ou Sair?   (itens/monstros/sair)\n")
        if escolha.lower() == "itens":
            while True:
                qualitem = input("\nVer espadas, armaduras, itens de fuga, consumiveis ou sair ?   (espadas/armaduras/fuga/consumiveis/sair)\n")
                while not(qualitem.lower() == "espadas" or qualitem.lower() == "armaduras" or qualitem.lower() == "fuga" or qualitem.lower() == "consumiveis" or qualitem.lower() == "sair"):
                    print("Escolha invalida")
                    qualitem = input("\nVer espadas, armaduras, itens de fuga, consumiveis ou sair ?   (espadas/armaduras/fuga/consumiveis/sair)\n")
                if qualitem.lower() == "espadas":
                    mostrarLista(itensDano)
                    continue
                elif qualitem.lower() == "armaduras":
                    mostrarLista(itensDefesa)
                    continue
                elif qualitem.lower() == "fuga":
                    mostrarLista(itensFuga)
                    continue
                elif qualitem.lower() == "consumiveis":
                    mostrarLista(itensConsumiveis)
                    continue
                elif qualitem.lower() == "sair":
                    break
        elif escolha.lower() == "monstros":
            mostrarLista(monstros)
            continue
        elif escolha.lower() == "sair":
            break
def creditos():
    input() #Creditos / Nome da equipe
def addStatus(player):
    tempo = 1  #Adiciona o status ao dicionario Player
    
    print(f"\nQuanto de cada <STATUS> você quer dar para {player['Nome']}?")
    sleep(tempo)
    print("Forças recomendadas: 4500, 6000, 7500")
    sleep(tempo)
    player["forca"] = int(input("Quanto de Força ? \n"))
    print()
    sleep(tempo)

    while player["forca"] <= 0 or player["forca"] > 7500:
        print("Força muito alta ou INVALIDA. Novo valor.")
        sleep(tempo)
        print("Força max: 7500")
        sleep(tempo)
        player["forca"] = int(input("Quanto de Força ? \n"))
        sleep(tempo)

    print("Defesas recomendadas: 30000, 35000, 45000.")
    sleep(tempo)
    player["defesa"] = int(input("Quanto de Defesa ? \n"))
    print()
    sleep(tempo)

    if player["forca"] <= 4500:        
        while player["defesa"] <= 0 or player["defesa"] > 45000:
            print("Defesa muito alta ou INVALIDA. Novo valor.")
            sleep(tempo)
            print("Defesa max: 45000.")
            sleep(tempo)
            player["defesa"] = int(input("Quanto de Defesa ? \n"))
            print()
            sleep(tempo)

    elif player["forca"] <= 6000:        
        while player["defesa"] <= 0 or player["defesa"] > 35000:
            print("Defesa muito alta ou INVALIDA. Novo valor.")
            sleep(tempo)
            print("Defesa max: 35000.")
            sleep(tempo)
            player["defesa"] = int(input("Quanto de Defesa ? \n"))
            print()
            sleep(tempo)

    elif player["forca"] > 7500:
        while player["defesa"] <= 0 or player["defesa"] > 30000:
            print("Defesa muito alta ou INVALIDA. Novo valor.")
            sleep(tempo)
            print("Defesa max: 30000.")
            sleep(tempo)
            player["defesa"] = int(input("Quanto de Defesa ? \n"))
            print()
            sleep(tempo)

    print("Fuga recomendada: 3.")
    sleep(tempo)
    player["fuga"] = int(input("Quanto de Fuga ? \n"))
    print()
    sleep(tempo)

    while player["fuga"] < 0 or player["fuga"] > 3:
        print("Fuga muito alta ou INVALIDA. Novo valor:")
        sleep(tempo)
        print("Fuga max: 3.")
        sleep(tempo)
        player["fuga"] = int(input("Quanto de Fuga ? \n"))
        print()
        sleep(tempo)
def temItem(inimigo):
    itemSN = randint(1,5) #Com uma chance de 60% diz se tem ou nn Intem ou se tiver inimigo tem item
    if itemSN >= 3 or inimigo != "Nenhum":
        return "S"
    else:
        return "N"
def temInimigo():
    inimigoSN = randint(1,3)  
    if inimigoSN == 1 or inimigoSN == 2: #75% de chance de ter inimigo
        return "S"
    else:
        return "N"
def item(inimigo):
    qualItem = randint(0,4) #Escolhe o item que vai ser retornado
     #Escolhe a variação do item que vai ser retornado / indice das listas
    if temItem(inimigo) == "S":
        if qualItem == 0:
            qualVariacao = randint(0,4)
            qualEspada = ["Espada de Ferro", "Alucard Sword", "Master Sword", "Laminas do Caos", "Dragon Slayer"]
            return qualEspada[qualVariacao]
        elif qualItem == 1:
            qualVariacao = randint(0,5)
            qualEscudo = ["Escudo de Madeira", "Escudo de Randuin", "Alucard Mail", "Escudo Hylian", "Berserk Armor", "Armadura de Warmog"]
            return qualEscudo[qualVariacao]
        elif qualItem == 2:
            qualVariacao = randint(0,4)
            qualBota = ["Meia", "Botas Galvanizadas de Aço", "Passos de Mercurio","Bota de Couro", "Botas Espaciais"]
            return qualBota[qualVariacao]
        elif qualItem == 3:
            qualVariacao = randint(0,2)
            BO = ["Espada de Madeira Amaldiçoada","Escudo de Ferro Amaldiçoado","Meia Furada"]
            return BO[qualVariacao]
        elif qualItem == 4:
            qualVariacao = randint(0,6)
            consumiveis = ["Pedra de amolar quebrada","Maçã envenenada","Poção de Veneno","Poção de Fraqueza","Poção de Lentidão","Anel Amaldiçoado","Anel da Paralisia"]
            return consumiveis[qualVariacao]
    else:
        return "Nenhum"
def inimigo(sala):
    if sala <= 7: 
        qualInimigo = randint(0,6) #Se a sala for menor igual a 6 sorteia todos os monstros da lista
    else:
        qualInimigo = randint(7,10) #Se a sala for maior que 6 so sorteia os 4 utimos monstros da lista
    if temInimigo() == "S":
            monstros = ["Slime", "Rato", "Morto-vivo", "Esqueleto","Arqueiro Esqueleto", "Esqueleto Gigante","Arqueiro Esqueleto Gigante","Wheel Skeletons", "Black Knight", "Demonio Corvo", "Sif", "Arquimago"]
            if qualInimigo == 0:
                return monstros[qualInimigo]
            elif qualInimigo == 1:
                return monstros[qualInimigo]
            elif qualInimigo == 2:
                return monstros[qualInimigo]
            elif qualInimigo == 3:
                return monstros[qualInimigo]
            elif qualInimigo == 4:
                return monstros[qualInimigo]
            elif qualInimigo == 5:
                return monstros[qualInimigo]
            elif qualInimigo == 6:
                return monstros[qualInimigo]
            elif qualInimigo == 7:
                return monstros[qualInimigo]
            elif qualInimigo == 8:
                return monstros[qualInimigo]
            elif qualInimigo == 9:
                return monstros[qualInimigo]
            elif qualInimigo == 10:
                return monstros[qualInimigo]
            elif qualInimigo == 11:
                return monstros[qualInimigo]
            
    else:
        return "Nenhum"
def aplicandoItem(player,item):
    #Quando a função é chamada ela recebe um item de acordo com o item ela muda alguns valores do dicionario player
    if item == "Espada de Ferro":
        player["forca"] += 100
    
    elif item == "Alucard Sword":
        player["forca"] += 300
    
    elif item == "Master Sword":
        player["forca"] += 500
    
    elif item == "Laminas do Caos":
        player["forca"] += 500

    elif item == "Dragon Slayer":
        player["forca"] += 750
        player["fuga"] -= 1
        
    elif item == "Escudo de Madeira":
        player["defesa"] += 2500
    
    elif item == "Escudo de Randuin":
        player["defesa"] += 2750

    elif item == "Alucard Mail":
        player["defesa"] += 3250
        
    elif item == "Escudo Hylian":
        player["defesa"] += 4000

    elif item == "Berserk Armor":
        player["defesa"] += 3500
        player["forca"] += 750
        player["fuga"] -= 1

    elif item == "Armadura de Warmog":
        player["defesa"] += 4000
        
    elif item == "Meia":
        player["fuga"] += 1
    
    elif item == "Botas Galvanizadas de Aço":
        player["fuga"] += 2
        player["defesa"] += 1000

    elif item == "Passos de Mercurio":
        player["fuga"] += 2
        player["defesa"] += 1000

    elif item == "Bota de Couro":
        player["fuga"] += 2
        
    elif item == "Botas Espaciais":
        player["fuga"] += 3
        
    elif item == "Espada de Madeira Amaldiçoada":
        player["forca"] += 3500
        player["defesa"] -= 3000
        player["fuga"] -= 3

    elif item == "Escudo de Ferro Amaldiçoado":
        player["defesa"] += 3500
        player["forca"] -= 3000
        player["fuga"] -= 3

    elif item == "Meia Furada":
        player["fuga"] += 3
        player["forca"] -= 3500
        player["defesa"] -= 3500 
    
    elif item == "Pedra de amolar quebrada":
        player["forca"] -= 450

    elif item == "Maçã envenenada":
        player["defesa"] -= 2000
    
    elif item == "Poção de Veneno":
        player["defesa"] -= 2005
    
    elif item == "Poção de Fraqueza":
        player["forca"] -= 345
    
    elif item == "Poção de Lentidão":
        player["fuga"] -= 2

    elif item == "Anel Amaldiçoado":
        player["forca"] -= 5000
        player["defesa"] -= 5000
        player["fuga"] -= 2

    elif item == "Anel da Paralisia":    
        player["fuga"] -= 4
def batalha(player, monstro):
    tempo = 1
    #Quando a função é chamada ela recebe um monstro, cria um dicionario desse monstro e batalha com o player, retornando Vitoria ou Derrota
    if monstro == "Slime":
        mob ={
            "Nome": "Slime",
            "forca": 2000,
            "defesa": 15000
        }   
    elif monstro == "Rato":
        mob ={
            "Nome": "Rato",
            "forca": 2000,
            "defesa": 13500
        }         
    elif monstro == "Morto-vivo":
        mob ={
            "Nome": "Morto-vivo",
            "forca": 2750,
            "defesa": 17025
        }           
    elif monstro == "Esqueleto":
        mob ={
            "Nome": "Esqueleto",
            "forca": 2750,
            "defesa": 20000
        }       
    elif monstro == "Arqueiro Esqueleto":
        mob ={
            "Nome": "Arqueiro Esqueleto",
            "forca": 2750,
            "defesa": 20000
        }             
    elif monstro == "Esqueleto Gigante":
        mob ={
            "Nome": "Esqueleto Gigante",
            "forca": 3500,
            "defesa": 26000
        }
    elif monstro == "Arqueiro Esqueleto Gigante":
        mob ={
            "Nome": "Arqueiro Esqueleto Gigante",
            "forca": 4000,
            "defesa": 23500
        }
    elif monstro == "Wheel Skeletons":
        mob ={
            "Nome": "Wheel Skeletons",
            "forca": 4000,
            "defesa": 25000
        } 
    elif monstro == "Black Knight":
        mob ={
            "Nome": "Black Knight",
            "forca": 3500,
            "defesa": 35000
        }          
    elif monstro == "Demonio Corvo":
        mob ={
            "Nome": "Demonio Corvo",
            "forca": 2900,
            "defesa": 32000
        }     
    elif monstro == "Sif":
        mob ={
            "Nome": "Sif",
            "forca": 3450,
            "defesa": 32500
        }       
    elif monstro == "Arquimago":
        mob ={
            "Nome": "Arquimago",
            "forca": 4000,
            "defesa": 25000
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
        mob["defesa"] -= player["forca"]
        if mob["defesa"] <= 0:
            mob["defesa"] = 0
            print(f"{mob['Nome']} defesa: {mob['defesa']}")
            sleep(tempo)
            print(f"{player['Nome']} defesa: {player['defesa']}")
            sleep(tempo)
            return "Vitoria"
        print(f"{mob['Nome']} defesa: {mob['defesa']}")
        sleep(tempo)
        player["defesa"] -= mob["forca"]
        if player["defesa"] <= 0:
            player["defesa"] = 0
            print(f"{player['Nome']} defesa: {player['defesa']}")
            sleep(tempo)
            return "GameOver"
        print(f"{player['Nome']} defesa: {player['defesa']}")
        sleep(tempo)     
def fuga(player,monstro):
    #A função recebe um monstro, cria um dicionario com um "Chave:Valor" que é fuga,dps comparando fuga de player com fuga de mob, retornando Fugiu ou Falha
    mob = monstro
    if mob == "Slime":
        slime = {
            "fuga": 5
        }
        if player["fuga"] >= slime["fuga"]:
            player["fuga"] -= 2
            return "fugiu"
        elif player["fuga"] <= slime["fuga"]:
            fugir = randint(1,5)
            if fugir <= 4:
                player["fuga"] -= 1
                return "fugiu"
            else:
                return "falha"
    elif mob == "Rato":
        rato = {
            "fuga": 5
        }
        if player["fuga"] >= rato["fuga"]:
            player["fuga"] -= 2
            return "fugiu"
        elif player["fuga"] <= rato["fuga"]:
            fugir = randint(1,5)
            if fugir <= 4:
                player["fuga"] -= 1
                return "fugiu"
            else:
                return "falha"
    elif mob == "Morto-vivo":
        undead = {
            "fuga": 5
        }
        if player["fuga"] >= undead["fuga"]:
            player["fuga"] -= 2
            return "fugiu"
        elif player["fuga"] <= undead["fuga"]:
            fugir = randint(1,5)
            if fugir <= 3:
                player["fuga"] -= 1
                return "fugiu"
            else:
                return "falha"
    elif mob == "Esqueleto":
        esqueleto = {
            "fuga": 6
        }
        if player["fuga"] >= esqueleto["fuga"]:
            player["fuga"] -= 2
            return "fugiu"
        elif player["fuga"] <= esqueleto["fuga"]:
            fugir = randint(1,5)
            if fugir <= 2:
                player["fuga"] -= 1
                return "fugiu"
            else:
                return "falha"
    elif mob == "Aranha":
        aranha = {
            "fuga": 7
        }
        if player["fuga"] >= aranha["fuga"]:
            player["fuga"] -= 2
            return "fugiu"
        elif player["fuga"] <= aranha["fuga"]:
            fugir = randint(1,5)
            if fugir == 1:
                player["fuga"] -= 1
                return "fugiu"
            else:
                return "falha"  
    elif mob == "Black Knight":
        blackKnight = {
            "fuga": 10
        }
        if player["fuga"] >= blackKnight["fuga"]:
            player["fuga"] -= 3
            return "fugiu"
        elif player["fuga"] <= blackKnight["fuga"]:
            fugir = randint(1,5)
            if fugir >= 4:
                player["fuga"] -= 2
                return "fugiu"
            else:
                return "falha" 
    elif mob == "Lagarto de Cristal":
        lagartoDeCristal = {
            "fuga": 11
        }
        if player["fuga"] >= lagartoDeCristal["fuga"]:
            player["fuga"] -= 3
            return "fugiu"
        elif player["fuga"] <= lagartoDeCristal["fuga"]:
            fugir = randint(1,5)
            if fugir >= 4:
                player["fuga"] -= 2
                return "fugiu"
            else:
                return "falha" 
    elif mob == "Sif":
        sif = {
            "fuga": 11
        }
        if player["fuga"] >= sif["fuga"]:
            player["fuga"] -= 3
            return "fugiu"
        elif player["fuga"] <= sif["fuga"]:
            fugir = randint(1,5)
            if fugir >= 4:
                player["fuga"] -= 2
                return "fugiu"
            else:
                return "falha" 
    elif mob == "Arquimago":
        arquiMago = {
            "fuga": 13
        }
        if player["fuga"] >= arquiMago["fuga"]:
            player["fuga"] -= 3
            return "fugiu"
        elif player["fuga"] <= arquiMago["fuga"]:
            fugir = randint(1,5)
            if fugir >= 4:
                player["fuga"] -= 2
                return "fugiu"
            else:
                return "falha" 
def qualBoss():
    escolhaDeBoss = randint(0,2) #Sorteia o Boss
    bosses = ["Izalith", "Nito","Gwyn"]
    if escolhaDeBoss == 0:
        return bosses[escolhaDeBoss]
    elif escolhaDeBoss == 1:
        return bosses[escolhaDeBoss]
    else:
        return bosses[escolhaDeBoss]
def batalhaBoss(player,boss):
    #Quando a função é chamada recebe o Boss sorteado, criando um dicionario diferente para cada boss, dps botando boss para batalhar com player
    #Retornando Vitoria ou Derrota
    tempo = 1
    if boss == "Izalith":
        chefe = {
            "Nome": "Bruxa de Izalith",
            "forca": 15000,
            "defesa": 40000
        }
        sleep(tempo)
        print(f"Nome: {chefe['Nome']}")
        sleep(tempo)
        print(f"forca: {chefe['forca']}")
        sleep(tempo)
        print(f"defesa: {chefe['defesa']}")
        sleep(tempo)

        print("Lute ou morra para Izalith")
        sleep(tempo)
        while True:
            acao = input("Você ira lutar, ver detalhes ou tentar fugir ?")  #Inputs esperados lutar/fugir
            sleep(tempo)
            tentativa = 0  #Variavel contador
            while acao.lower() != "lutar" or acao.lower() != "detalhes":
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
                    chefe["defesa"] -= player["forca"]
                    if chefe["defesa"] <= 0:
                        chefe["defesa"] = 0
                        print(f"{player['Nome']} defesa: {player['defesa']}")
                        sleep(tempo)
                        print(f"Izalith defesa: {chefe['defesa']}")
                        sleep(tempo)
                        return player["defesa"]
                    print(f"Izalith defesa: {chefe['defesa']}")
                    sleep(tempo)
                    player["defesa"] -= chefe["forca"]
                    if player["defesa"] <= 0:
                        player["defesa"] = 0
                        print(f"{player['Nome']} defesa: {player['defesa']}")
                        sleep(tempo)
                        return player["defesa"]
                    print(f"{player['Nome']} defesa: {player['defesa']}")
                    sleep(tempo)
            elif acao.lower() == "detalhes":
                detalhes(boss)
    elif boss == "Nito":
        chefe = {
            "Nome": "Nito, o Lorde dos Túmulos",
            "forca": 8500,
            "defesa": 55000
        }
        sleep(tempo)
        print(f"Nome: {chefe['Nome']}")
        sleep(tempo)
        print(f"forca: {chefe['forca']}")
        sleep(tempo)
        print(f"defesa: {chefe['defesa']}")
        sleep(tempo)

        print("Lute ou morra para Nito")
        sleep(tempo)
        while True:
            acao = input("Você ira lutar, ver detalhes ou tentar fugir ?")  #Inputs esperados lutar/fugir
            sleep(tempo)
            tentativa = 0  #Variavel contador
            while acao.lower() != "lutar" or acao.lower() != "detalhes":
                if tentativa < 2:
                    print("Lute ou morra")
                    sleep(tempo)
                    acao = input("Você ira lutar, ver detalhes ou tentar fugir ?")
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
                    chefe["defesa"] -= player["forca"]
                    if chefe["defesa"] <= 0:
                        chefe["defesa"] = 0
                        print(f"{player['Nome']} defesa: {player['defesa']}")
                        sleep(tempo)
                        print(f"Nito defesa: {chefe['defesa']}")
                        sleep(tempo)
                        return player["defesa"]
                    print(f"Nito defesa: {chefe['defesa']}")
                    sleep(tempo)
                    player["defesa"] -= chefe["forca"]
                    if player["defesa"] <= 0:
                        player["defesa"] = 0
                        print(f"{player['Nome']} defesa: {player['defesa']}")
                        sleep(tempo)
                        return player["defesa"]
                    print(f"{player['Nome']} defesa: {player['defesa']}")
                    sleep(tempo)
            elif acao.lower() == "detalhes":
                detalhes(boss)
    elif boss == "Gwyn":
        chefe = {
            "Nome": "Gwyn, o Lorde das Cinzas",
            "forca": 13500,
            "defesa": 50000
        }
        sleep(tempo)
        print(f"Nome: {chefe['Nome']}")
        sleep(tempo)
        print(f"forca: {chefe['forca']}")
        sleep(tempo)
        print(f"defesa: {chefe['defesa']}")
        sleep(tempo)

        print("Lute ou morra para Gwyn")
        sleep(tempo)
        while True:
            acao = input("Você ira lutar, ver detalhes ou tentar fugir ? (lutar/detalhes/fugir")  #Inputs esperados lutar/fugir
            sleep(tempo)
            tentativa = 0  #Variavel contador
            while acao.lower() != "lutar" or acao.lower() != "detalhes":
                if tentativa < 2:
                    print("Lute ou morra")
                    sleep(tempo)
                    acao = input("Você ira lutar, ver detalhes ou tentar fugir ?")
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
                    chefe["defesa"] -= player["forca"]
                    if chefe["defesa"] <= 0:
                        chefe["defesa"] = 0
                        print(f"{player['Nome']} defesa: {player['defesa']}")
                        sleep(tempo)
                        print(f"Gwyn defesa: {chefe['defesa']}")
                        sleep(tempo)
                        return player["defesa"]
                    print(f"Gwyn defesa: {chefe['defesa']}")
                    sleep(tempo)
                    player["defesa"] -= chefe["forca"]
                    if player["defesa"] <= 0:
                        player["defesa"] = 0
                        print(f"{player['Nome']} defesa: {player['defesa']}")
                        sleep(tempo)
                        return player["defesa"]
                    print(f"{player['Nome']} defesa: {player['defesa']}")
                    sleep(tempo)
            elif acao.lower() == "detalhes":
                detalhes(boss)
def detalhes(monstro):
    tempo = 0.05
    arq = open("monstros.txt", "r")
    for i in arq:
        if monstro in i:
            textoMonstro = i.split(";")
            for j in textoMonstro[1]:
                print(j, end='', flush=True)
                sleep(tempo)
            break
    input()
    arq.close()
def fogueira(player,sala):
    d5 = randint(1,5)
    if d5 <= 3:
        d20 = randint(0,20)
        if d20 <= 5:
            print("Você limpou a sala, você avistou um braseiro jogado no chão")
            verStatus = input("Ver Status no braseiro? (S/N)")
            while not(verStatus.lower() == "s" or verStatus.lower() == "n"):
                sentar = input("Ver Status no braseiro? (S/N)")
            if verStatus.lower() == "s":
                mostrarStatus(player,sala)
            return
        elif d20 > 5 and d20 <= 15:
            sentar = input("Você limpou a sala, você avistou uma fogueira com um braseiro ao lado, sentar ? (S/N)")
            while not(sentar.lower() == "s" or sentar.lower() == "n"):
                sentar = input("Você limpou a sala, você avistou uma fogueira com um braseiro ao lado, sentar ? (S/N)")
            if sentar.lower() == "s":
                player["forca"] += 200
                player["defesa"] += 1200
                player["fuga"] += 1
                verStatus = input("Ver Status no braseiro? (S/N)")
                while not(verStatus.lower() == "s" or verStatus.lower() == "n"):
                    sentar = input("Ver Status no braseiro? (S/N)")
                if verStatus.lower() == "s":
                    mostrarStatus(player,sala)
            if sentar.lower() == "n":
                verStatus = input("Ver Status no braseiro? (S/N)")
                while not(verStatus.lower() == "s" or verStatus.lower() == "n"):
                    sentar = input("Ver Status no braseiro? (S/N)")
                if verStatus.lower() == "s":
                    mostrarStatus(player,sala)
            return
        elif d20 > 15:
            sentar = input("Você limpou a sala, você avistou uma fogueira sagrada com um braseiro ao lado, sentar ? (S/N)")
            while not(sentar.lower() == "s" or sentar.lower() == "n"):
                sentar = input("Você limpou a sala, você avistou uma fogueira sagrada com um braseiro ao lado, sentar ? (S/N)")
            if sentar.lower() == "s":
                player["forca"] += 600
                player["defesa"] += 3600
                player["fuga"] += 2
                verStatus = input("Ver Status no braseiro? (S/N)")
                while not(verStatus.lower() == "s" or verStatus.lower() == "n"):
                    sentar = input("Ver Status no braseiro? (S/N)")
                if verStatus.lower() == "s":
                    mostrarStatus(player,sala)
            if sentar.lower() == "n":
                verStatus = input("Ver Status no braseiro? (S/N)")
                while not(verStatus.lower() == "s" or verStatus.lower() == "n"):
                    sentar = input("Ver Status no braseiro? (S/N)")
                if verStatus.lower() == "s":
                    mostrarStatus(player,sala)
            return
    elif d5 > 3:
        d20 = randint(1,20)
        if d20 <= 13:
            print("A sala esta limpa apenas a(s) porta(s) espera você")
        if d20 > 13 and d20 <= 18:
            print("FOGUEIRA AMALDIÇOADA")
        else:
            print("Fogueira Fudida")
def salas(player,inimigo,item):
    #Cria as coisas que tem em toda sala como: Inimigo, Item, Batalha, etc... 
    tempo = 1
    resultado = ""
    print(f"Monstro na sala: {inimigo}")
    sleep(tempo)
    print(f"Item na sala: {item}\n")
    sleep(tempo)
    while not(inimigo == "Nenhum" and item == "Nenhum"):
        if inimigo != "Nenhum":
            lutar = input("Lutar contra o Monstro, ver detalhes ou tentar Fugir?   (lutar/detalhes/fugir)\n")   #Input esperado lutar/detalhes/fugir
            sleep(tempo)
            while not(lutar.lower() == "lutar" or lutar.lower() == "detalhes" or lutar.lower() == "fugir"):
                lutar = input("Lutar, verdetalhes ou Fugir?   (lutar/detalhes/fugir)\n")
                sleep(tempo)
            if lutar.lower() == "lutar":
                resultado = batalha(player,inimigo)
                inimigo = "Nenhum"
            elif lutar.lower() == "detalhes":
                detalhes(inimigo)
            elif lutar.lower() == "fugir":
                fugir = fuga(player, inimigo)
                if fugir == "fugiu":
                    print("Você conseguiu fugir\n")
                    sleep(tempo)
                    inimigo = "Nenhum"
                elif fugir == "falha":
                    print("Você não conseguiu fugir, Seu status de fuga caiu para 0\n")
                    sleep(tempo)
                    player["fuga"] = 0
        if player["defesa"] <= 0:
            print("Você perdeu\n")
            input()
            return "Derrota"
        if resultado == "Vitoria" or inimigo == "Nenhum":
            if item != "Nenhum":
                print(f"item: {item}")
                usar = input("Usar item: (S/N)\n")
                sleep(tempo)
                while not(usar.lower() == "s" or usar.lower() == "n"):
                    usar = input("Usar item: (S/N)\n")
                    sleep(tempo)
                if usar.lower() == "s":
                    aplicandoItem(player, item)
                    item = "Nenhum"
                elif usar.lower() == "n":
                    item = "Nenhum"
    return "Vitoria"
def mostrarStatus(player,sala):
    tempo = 1
    print("\n--------------------------------")
    sleep(tempo)
    print(f"{player['Nome']} <STATUS>:")
    sleep(tempo)
    print(f"Força: {player['forca']}")
    sleep(tempo)
    print(f"Defesa: {player['defesa']}")
    sleep(tempo)
    print(f"Fuga: {player['fuga']}")
    sleep(tempo)
    print(f"Sala: {sala}")
    sleep(tempo)
    print("----------------------------------\n")
    sleep(tempo)