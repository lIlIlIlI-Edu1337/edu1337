############################
print("Jogo de Advinhação")
print("Tente advinhar um número de 0 a 15!")
print("Eduardo Alves Martin N°8")
############################
############################
print("Jogo de Advinhação")
print("Tente advinhar um número de 0 a 15!")
print("Eduardo Alves Martin N°8")
############################
import random
import os

erros=1
sorteado=random.randrange(0,100)
jogador=int(input("Digite seu número!") )
while (sorteado!=jogador):
    os.system('cls')
if(sorteado>jogador):
    print("O número é maior!")
elif(sorteado<jogador):
    print("O número é menor!")
erros += 1
jogador=int(input("Digite seu número: "))
print("Número" + str(jogador) + ",você acertou em: " + str(erros+1) + "tentativas")