import random
import time
import sys


lista = ["Sim, com toda certeza", "As chances são altas", "Não sei", "Talvez sim, talvez não""Acho que não",
         "Acho que sim", "Tente e descubra", "Não posso te responder isso", "Não, acho que não ",
         "Tenho certeza que não", "Se concentre, depois pergunte de novo", "Não tente fazer isso",
         "Você vai conseguir"]


def userinput():
    questao = "Digite sua duvida:"
    print(questao)
    userQ = input("")

    print("\nEstou Pensando..\n")
    time.sleep(3)
    print(random.choice(lista))

    resultado()

def resultado():
    print("Gostaria de fazer outra pergunta ? (sim ou não)")
    resposta = input('> ')
    while(input):
        if resposta == "sim":
            userinput()
        else:
            print("Obrigado por jogar")
            sys.exit(0)

print("Bem vindo ao Jogo da bola magica")
userinput()