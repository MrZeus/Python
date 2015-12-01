import random
import sys

words = ['chair', 'wall', 'pedophile', 'fire', 'hello', 'tree', 'dead', 'sawmill', 'allahu', 'david']

random.seed()
rightWord = random.choice(words)
wrongs = 0

counter = 0
print(rightWord)
while counter < len(rightWord):
    counter += 1
    print("-", end='')

print("")
while True:
    guess = input("> ")

    if guess in rightWord:								#TODO: Spara hints till nästa gissning
        print("Yes, {} is in the word".format(guess))
        pos = rightWord.index(guess)
        print(pos)
        counter = 0
        while counter < pos:
            counter += 1
            print("-", end='')

        print(guess, end='')

        while counter < (len(rightWord) - 1):
            counter += 1
            print("-", end='')

        print("")
    else:
        print("Nope, {} is not in the word".format(guess))
        wrongs += 1

    if wrongs >= 5:
        print("You lose!")
        print("The word was: {}".format(rightWord))
        sys.exit()
