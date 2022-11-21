from time import sleep
monstros = ["Mimic","Demonio asa de Morcego","Golem de Cristal","Slime", "Rato", "Morto-vivo", "Esqueleto","Arqueiro Esqueleto", "Esqueleto Gigante","Arqueiro Esqueleto Gigante","Wheel Skeletons", "Black Knight", "Demonio Corvo", "Sif", "Arquimago"]
tempo = 0.01
arq = open("monstros.txt", "r")
for i in arq:
    for k in monstros:
        if k in i:
            textoMonstro = i.split(";")
            for j in textoMonstro[1]:
                print(j, end='', flush=True)
                sleep(tempo)
            break
arq.close()