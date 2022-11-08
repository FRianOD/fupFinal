from random import randint
def temItem():
    itemSN = randint(1,5)
    if itemSN == 1 or itemSN == 2:
        return "S"
    else:
        return "N"
def temInimigo():
    inimigoSN = randint(1,3)
    if inimigoSN == 1 or inimigoSN == 2:
        return "S"
    else:
        return "N"
def item():
    qualItem = randint(0,2)
    qualVariacao = randint(0,2)
    if temItem() == "S" or temInimigo() == "S" :
        if qualItem == 0:
            qualEspada = ["Espada de Madeira", "Espada de Ferro", "Dragon Slayer"]
            return qualEspada[qualVariacao]
        elif qualItem == 1:
            qualEscudo = ["Escudo de Madeira", "Escudo de Ferro", "Escudo Hylian"]
            return qualEscudo[qualVariacao]
        else:
            qualBota = ["Meia", "Bota de Couro", "Botas Espaciais"]
            return qualBota[qualVariacao]
    else:
        return "Nenhum"
def inimigo():
    qualInimigo = randint(0,3)
    monstros = ["Slime", "Zumbi","Esqueleto","Aranha"]
    if temInimigo() == "S":
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
        return player["forca"]
    elif item == "Espada de Ferro":
        player["forca"] += 2
        return player["forca"]
    elif item == "Dragon Slayer":
        player["forca"] += 3
        return player["forca"]
    elif item == "Escudo de Madeira":
        player["defesa"] += 2
        return player["defesa"]
    elif item == "Escudo de Ferro":
        player["defesa"] += 3
        return player["defesa"]
    elif item == "Escudo Hylian":
        player["defesa"] += 5
        return player["defesa"]
    elif item == "Meia":
        player["fuga"] += 1
        return player["fuga"]
    elif item == "Bota de Couro":
        player["fuga"] += 2
        return player["fuga"]
    elif item == "Botas Espaciais":
        player["fuga"] += 3
        return player["fuga"]
def batalha(player, monstro):
    if monstro == "Slime":
        slime ={
            "nome": "Slime",
            "forca": 1,
            "defesa": 1
        }
        while (player["defesa"] >= 0 or slime["defesa"] >= 0):
            player["defesa"] -= slime["forca"]
            slime["defesa"] -= player["forca"]
            if player["defesa"] >= 0 and slime["defesa"] <= 0:
                return "Vitoria"
            elif slime["defesa"] >= 0 and player["defesa"] <= 0:
                return "GameOver"
    elif monstro == "Zumbi":
        zumbi ={
            "nome": "Zumbi",
            "forca": 2,
            "defesa": 2
        }
        while (player["defesa"] >= 0 or zumbi["defesa"] >= 0):
            player["defesa"] -= zumbi["forca"]
            zumbi["defesa"] -= player["forca"]
            if player["defesa"] >= 0 and zumbi["defesa"] <= 0:
                return "Vitoria"
            elif zumbi["defesa"] >= 0 and player["defesa"] <= 0:
                return "GameOver"
    elif monstro == "Esqueleto":
        esqueleto ={
            "nome": "Esqueleto",
            "forca": 2,
            "defesa": 3
        }
        while (player["defesa"] >= 0 or esqueleto["defesa"] >= 0):
            player["defesa"] -= esqueleto["forca"]
            esqueleto["defesa"] -= player["forca"]
            if player["defesa"] >= 0 and esqueleto["defesa"] <= 0:
                return "Vitoria"
            elif esqueleto["defesa"] >= 0 and player["defesa"] <= 0:
                return "GameOver"
    elif monstro == "Aranha":
        aranha ={
            "nome": "Aranha",
            "forca": 3,
            "defesa": 3
        }
        while (player["defesa"] >= 0 or aranha["defesa"] >= 0):
            player["defesa"] -= aranha["forca"]
            aranha["defesa"] -= player["forca"]
            if player["defesa"] >= 0 and aranha["defesa"] <= 0:
                return "Vitoria"
            elif aranha["defesa"] >= 0 and player["defesa"] <= 0:
                return "GameOver"
def qualBoss():
    escolhaDeBoss = randint(0,2)
    bosses = ["Locus, Moonlight Knight", "Grunbeld, The Great Flame Dragon","Nosferatu Zodd, The Immortal"]
    if escolhaDeBoss == 0:
        return bosses[escolhaDeBoss]
    elif escolhaDeBoss == 1:
        return bosses[escolhaDeBoss]
    else:
        return bosses[escolhaDeBoss]
def batalhaBoss(player,boss):
    if boss == "Locus, Moonlight Knight":
        locus = {
            "Nome": "Locus, Moonlight Knight"
        }
    elif boss == "Grunbeld, The Great Flame Dragon":
        grunbeld = {
            "Nome": "Grunbeld, The Great Flame Dragon"
        }
    elif boss == "Nosferatu Zodd, The Immortal":
        zodd = {
            "Nome": "Nosferatu Zodd, The Immortal"
        }