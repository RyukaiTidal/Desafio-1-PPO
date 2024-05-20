from classes import *

print(f"LIFE SIMULATOR BASIC")

name = input("Bem vindo ao primeiro desafio!"
             "\n Para iniciar, Insira o nome. \n-")
age = int(input("Agora, insira a idade. \n-"))
weight = float(input("E por fim, insira o peso inicial. \n-"))

player = Pessoa(name, age, weight)

menuc = "nairs"
player.opcoes()
while True:
    menuc = input("Digite a sua ação: \n-")
    player.menu(menuc)
    if menuc in "Sair,sair":
        break
