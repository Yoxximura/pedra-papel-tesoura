# Jogo do pedra, papel e tesoura com o computador

import random #Gera escolhas aleatórias
opcoes = ["pedra", "papel", "tesoura"] #Essas são as opções dos jogadores

jogador1 = input("Escolha pedra, papel ou tesoura:\n").lower() #Solicita ao jogador para escolher. ".lower ()" caso o jogador coloque letra maiúscula
while jogador1 not in ["pedra", "papel", "papel"]: #Verificando se o jogador escolheu corretamente
    jogador1 = input('Escolha umas das três opções "pedra, papel ou tesoura":\n').strip().lower()
pc = random.choice(opcoes) #O computador escolhe aleatoriamente uma opção

# Mostra o que cada um escolheu
print(f"Você escolheu: {jogador1}")
if jogador1 == "pedra":
    print(pedra)
elif jogador1 == "papel":
    print(papel)
else:
    print(tesoura)

print(f"O computador escolheu: {pc}")

if pc== "pedra":
    print(pedra)
elif pc == "papel":
    print(papel)
else:
    print(tesoura)

if jogador1 == pc:
    print("Empate!")

#Verifica se o computador ganhou
elif (pc == "pedra" and jogador1 == "tesoura") or \
        (pc == "tesoura" and jogador1 == "papel") or \
        (pc == 'papel' and jogador1 == 'pedra'):
    print("O computador venceu!!!")
#Verifica se você venceu
else:
    print("Você ganhou, Parabéns!!!")


