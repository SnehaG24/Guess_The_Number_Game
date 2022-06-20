import random

Random_Number=random.randrange(0,100) #random.random >> a literal random number

# but if you want random number between the specific range : random.randrange()

print(Random_Number)
print(" ")
print("                     WELCOME TO THE GUESS THE NUMBER GAME    ")
print("                       WE HOPE YOU WILL ENJOY THIS GAME    ")
print("  IN THIS GAME , THE COMPUTER THINKS OF A RANDOM NUMBER BETWEEN 1 AND 100 . THE PLAYER HAS TO GUESS THE NUMBER!")
print(" ")

UserGuess = None

No_of_guesses=0

while UserGuess!=Random_Number :

    UserGuess = int(input(" Guess the Number := "))

    No_of_guesses=No_of_guesses+1

    if UserGuess==Random_Number :
        print("---------------------------------------------------")
        print("Hurrayy!!! You guessed the Right Number Yeahhh :)")

    else :

        if UserGuess>Random_Number:
            print("Oops! You guessed the Wrong number :( ")
            print("No Worries here's a Hint : Go For the Smaller Number Than Your Previous Guessed Number")

        else :
            print("Oops! You guessed the Wrong number :( ")
            print("No Worries here's a Hint : Go For the Larger Number Than Your Previous Guessed Number")


print("You guessed the number in",No_of_guesses,"guesses")
print("---------------------------------------------------")

with open("hiscore.txt","r") as f :
    hiscore=int(f.read())

if(No_of_guesses<hiscore):
    print("You Have just broken the high score!")
    with open("hiscore.txt","w") as f :
        f.write(str(No_of_guesses))
print("---------------------------------------------------")