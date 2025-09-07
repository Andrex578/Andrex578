import time


import random

opcoes = ("pedra", "papel", "tesoura")

jogador = input("qual a sua escolha?")
computador = random.choice(opcoes)

print(computador)

if jogador == "pedra" and computador == "papel":
    print("você perdeu")
elif jogador == "papel" and computador == "tesoura":
  print("você perdeu")
elif jogador == "tesoura" and computador == "pedra":
  print("você perdeu")
elif jogador == "pedra" and computador == "tesoura":
   print("você ganhou")
elif jogador == "papel" and computador == "pedra":
  print("você ganhou")
elif jogador == "tesoura" and computador == "papel":
  print("você ganhou")
elif jogador == "pedra" and computador == "pedra":
  print("EMPATE")
elif jogador == "papel" and computador == "papel":
  print("EMPATE")
elif jogador == "tesoura" and computador == "tesoura":
  print("EMPATE")


