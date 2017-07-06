import time 

def computer(name, n_toothpicks, min_toothpicks, max_toothpicks):
	name = name.title()

	while n_toothpicks >= min_toothpicks:
		
		print("| " * n_toothpicks)
		player_remove = int(input(name + " digite quantos palitos deseja remover:"))

		if min_toothpicks <= player_remove <= max_toothpicks: 
			n_toothpicks -= player_remove
			computer_remove = intelligence(n_toothpicks, min_toothpicks, max_toothpicks)

			print("O Computador removeu ", computer_remove, " palitos", end="\n\n")

			if n_toothpicks <= min_toothpicks:
				print("O jogador ", name.title(), " ganhou o jogo!!!")
				return 0
			else:
				n_toothpicks -= computer_remove
				if n_toothpicks <= min_toothpicks:
					print("O computador ganhou o jogo!!!")
					return 0

			time.sleep(2)

		else:
			print("Você digitou um valor que está fora do mínimo e máximo definidos!! Tente novamente", end="\n\n")
			time.sleep(2)

def intelligence(n_toothpicks, min_tooth, max_tooth):
	if n_toothpicks <= min_toothpicks + max_tooth:
		return n_toothpicks - min_tooth

	rest = n_toothpicks % (min_tooth + max_tooth)

	if rest < max_tooth:
		return rest + min_tooth
	elif rest >= max_tooth:
		return rest - min_tooth
	else:
		return 1


def human():
	pass

print("Bem Vindo ao NIM!!")

while True:

	n_toothpicks = int(input("Digite o número de palitos (5 <= x < 40):"))

	if 5 <= n_toothpicks < 40:
		pass
	else:
		print("O número de palitos está fora dos limites!! Tente novamente", end="\n\n")
		time.sleep(2)
		continue

	min_toothpicks = int(input("Digite o mínimo de palitos à retirar (4 >= min >= 1):"))
	max_toothpicks = int(input("Digite o máximo de palitos à retirar (min <= max <= 4):"))

	if 1 <= min_toothpicks <= max_toothpicks <= 4:
		pass
	else:
		print("Os valores apresentados estão fora do limite para os palitos à retirar!! Tente novamente", end="\n\n")
		time.sleep(2)
		continue

	player_or_computer = int(input("Digite 1 para jogar contra o PC ou 2 contra um colega:"))
	print("")

	if player_or_computer != 1 and 2:
		print("Valor para modo de jogo inválido!! Tente Novamente", end="\n\n")
		time.sleep(2)
	else:
		name = input("Digite seu nome:")
		print("")
		if player_or_computer == 1: 
			computer(name, n_toothpicks, min_toothpicks, max_toothpicks)
		else:
			human()


