from random import randint
def temItem():
    itemSN = randint(1,5)
    if itemSN == 1 or itemSN == 2:
        return "S"
    else:
        return "N"
def item():
    qualItem = randint(0,2)
    itens = ["Espada","Escudo","bota"]
    if temItem() == "S":
        if qualItem == 0:
            return itens[qualItem]
        elif qualItem == 1:
            return itens[qualItem]
        else:
            return itens[qualItem]
    else:
        return "Nenhum"
def temInimigo():
    inimigoSN = randint(1,3)
    if inimigoSN == 1 or inimigoSN == 2:
        return "S"
    else:
        return "N"
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
            "nome": "Slime",
            "forca": 2,
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
            "forca": 1,
            "defesa": 3
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
            "forca": 3,
            "defesa": 2
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