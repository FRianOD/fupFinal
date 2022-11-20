from time import sleep
monstros = ["Slime", "Rato", "Morto-vivo", "Esqueleto", "Esqueleto Gigante","Arqueiro Esqueleto Gigante","Wheel Skeletons", "Black Knight", "Lagarto de Cristal", "Sif", "Arquimago"]
tempo = 0.05
arq = open("monstros.txt", "r")
for i in arq:
    if monstros[3] in i:
        textoMonstro = i.split(";")
        for j in textoMonstro[1]:
            print(j, end='', flush=True)
            sleep(tempo)
        break
arq.close()