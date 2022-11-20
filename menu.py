from funcoes import menu, instrucoes, creditos, livro
from fupFinal import jogar
while True:
    menu()
    escolha = input("Digite a opção:\n")
    while not(escolha == "0" or escolha == "1" or escolha == "2" or escolha == "3" or escolha == "4"):
        print("Escolha invalida")
        escolha = input("Digite a opção:\n")
    if escolha == "0":
        break #Salvar?????
    elif escolha == "1":
        jogar()
        continue
    elif escolha == "2":
        livro()
        continue
    elif escolha == "3":
        instrucoes()
        continue
    elif escolha == "4":
        creditos()
        continue