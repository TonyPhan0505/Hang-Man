import random
import os

def play_hangman(path):
	# randomize a word t start playing
	with open(path, "r") as f:
		words = [word.replace("\n","") for word in f.readlines()]
	word = random.choice(words)
	# count the number of characters in the word and generate spaces
	num_chars = len(word)
	# list of final messages
	messages = ["Well Done!", "Better Luck Next Time!"]
	# player's answer
	answer = ["_" for _ in range(num_chars)]
	# number of guesses
	guesses = 7

	# draw the hanger
	#  _____
	# |/    |
	# |     o
	# |    /|\
	# |     | 
	# |    / \
	hanger = [
		[" ", ("_"*5), " "],
		["|/    |"],
		["|", "     ", ""],
		["|", "    ", "", "", ""],
		["|", "     ", ""],
		["|", "    ", "", " ", ""],
	]

	# dictionary of body parts
	body = {
		7: None,
		6: ["o", 2, 2],  # remaining guesses: [body part, row index, position on row]
		5: ["/", 3, 2], 
		4: ["|", 3, 3], 
		3: ["\ ", 3, 4],
		2: ["|", 4, 2],
		1: ["/", 5, 2],
		0: ["\ ", 5, 4],
	}
	
	# game loop
	while "".join(answer) != word and guesses >= 0:
		# modify the hanger
		change = body[guesses]
		if change:
			hanger[change[1]][change[2]] = change[0]
		# display the hanger
		for row in hanger:
			print("".join(row))
		# display game state
		print(" ".join(answer))
		print(f"You have {guesses} tries remaining.")
		if guesses > 0:
			# Ask for input
			inp = input("Guess a letter:")
			# clear the screen
			os.system("clear")
		# Change game state
		if inp in word: 
			for i in range(len(word)):
				if word[i] == inp:
					answer[i] = inp
		else:
			# decrease number of guesses
			guesses -=1
	
	# display messages
	if "".join(answer) == word:
		print(messages[0])
		print(f"The word is: {word}.")
	else:
		print(messages[1])
		print(f"The word is: {word}.")

play_hangman("words.txt")
		