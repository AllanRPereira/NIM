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


def human(players, n_toothpicks, min_tooth, max_tooth):
	players[0] = players[0].title()
	players[1] = players[1].title()
	player_current = 0

	while True:
		print("| " * n_toothpicks, end="\n\n")
		player_remove = int(input(players[player_current] + ", digite quantos palitos deseja remover:"))
		print("")

		if min_tooth <= player_remove <= max_tooth and player_remove <= n_toothpicks:
			n_toothpicks -= player_remove
		elif player_remove > n_toothpicks:
			print("Número digitado é maior do que o número de palitos disponíveis!!Tente Novamente", end="\n\n")
			continue
		else:
			print("Número digitado fora do intervalo definido!!Tente Novamente", end="\n\n")
			continue
			
		if n_toothpicks <= min_tooth:
			print("O jogador ", players[player_current], " ganhou a partida!!")
			return 0
		else:
			if player_current == 0:
				player_current += 1
			else:
				player_current -= 1


print("Bem Vindo ao NIM!!")

while True:

	n_toothpicks = int(input("Digite o número de palitos (5 <= x < 40) e deve ser ímpar:"))

	if 5 <= n_toothpicks < 40 and n_toothpicks % 2 != 0:
		pass
	else:
		print("O número de palitos está fora dos limites ou é par!! Tente novamente", end="\n\n")
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

	if player_or_computer != 1 and player_or_computer != 2:
		print("Valor para modo de jogo inválido!! Tente Novamente", end="\n\n")
		time.sleep(2)
	else:
		name_player1 = input("Digite seu nome:")
		print("")
		if player_or_computer == 1: 
			computer(name_player1, n_toothpicks, min_toothpicks, max_toothpicks)
		else:
			name_player2 = input("Digite o nome do jogador 2:")
			human([name_player1, name_player2], n_toothpicks, min_toothpicks, max_toothpicks)
