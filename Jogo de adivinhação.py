import time
import random


def jogar():

    print("Ola, me chamo Clarissa, sou sua inteligencia artificial preferida... ér você sabe q eu nao sou um I.A, MAS VAMOS FINGIR QUE EU SOU. :)")
    time.sleep(1.25)
    print("E hoje iremos jogar um jogo onde eu pensarei em um numero e você tera que descobrir o numero!")
    time.sleep(1.25)
    print("Entao seja muito bem vindo ao jogo de advinhação ")
    print("Primeiro quero saber seu nome :)")


    nome = input("Digite aqui seu nome: ")
    numero_secreto = random.randrange(1, 101)
    numero_de_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade hoje", nome, "?")
    print("(1) Fácil  (2) Médio  (3) Dificil", numero_secreto)

    nivel = int(input("Qual nivel você escolhe? "))

    if nivel == 1:
        numero_de_tentativas = 20
    elif nivel == 2:
        numero_de_tentativas = 10
    else:
        numero_de_tentativas = 5


    for rodada in range(1, numero_de_tentativas + 1):

        print("Tentativa {} de {}".format(rodada, numero_de_tentativas))
        chute_str = input("Digite um numero de 1 a 100!: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Ei ei ei, você deve chutar um número de 1 a 100!!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Voce acertou ebaa, voce fez {} pontos!!".format(pontos))
            break
        else:
            if maior:
                print("Voce errou, o seu chute foi maior que o numero secreto")
                if rodada == numero_de_tentativas:
                    print("Acabaram suas tentativas, o numero secreto era {} e voce fez {} pontos".format(numero_secreto, pontos))

            elif menor:
                print("Voce errou, o seu chute foi menor que o numero secreto")
                if rodada == numero_de_tentativas:
                    print("Acabaram suas tentativas, o numero secreto era {} e voce fez {} pontos".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Foi muuuito divertido jogar com voce", nome, "sempre que quiser eu estarei te esperando ok? byee")
    time.sleep(1.25)
    print("____________________Clarissa desligando...____________________")
    time.sleep(1.25)
    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()
