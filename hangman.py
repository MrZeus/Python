import random
import sys

words = ['chair','wall','pedophile','fire','hello','tree','dead','sawmill','allahu','david']

random.seed()
rightWord = random.choice(words)
guesses = 0

counter = 0
print(rightWord)
while counter < len(rightWord):
	counter+=1
	print("-",end='')

print("")

while True:
	guess = input("> ")

	if guess in rightWord:
		print("Yes, {} is in the word".format(guess))
	else:
		print("Nope, {} is not in the word".format(guess))
		guesses+=1
	
	if guesses >= 5:
		print("You lose!")
		print("The word was: {}".format(rightWord))
		sys.exit()


