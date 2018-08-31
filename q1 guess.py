import random
for x in range(1):
    rando = random.randint(1,20)
    print (rando)

guesses = 0;

while True:
    print ("Guess a number between 1 and 20")
    guess = input()
    guess = int(guess)

    guesses += 1


    if rando > guess:
        print("Too low, guess again")

    if rando < guess:
        print ("Too high, guess again")

    if rando == guess:
        print ("That's right! It took you " + str(guesses) + " guesses")
        break
