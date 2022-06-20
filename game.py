import random

Random_Number=random.randrange(0,100) #random.random >> a literally random number

# but if you want random number between the specific range : random.randrange()

# print(Random_Number)

UserGuess = None
print("")
No_of_guesses=0
print("                     WELCOME TO THE GUESS THE NUMBER GAME    ")
print("                       WE HOPE YOU WILL ENJOY THIS GAME    ")
print("  IN THIS GAME , THE COMPUTER THINKS OF A RANDOM NUMBER BETWEEN 1 AND 100 . THE PLAYER HAS TO GUESS THE NUMBER!")
while UserGuess!=Random_Number :
    print(" ")
    # print("            LET'S START")
    print(" ")
    UserGuess = int(input("Guess the Number := "))

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


if No_of_guesses==1 :

    print("Total No. of Guesses are : ",No_of_guesses)
    print("Omg!!!You just broke the record :o ")
    print("---------------------------------------------------")

elif 1<No_of_guesses and No_of_guesses<6 :

    print("Total No. of Guesses are : ",No_of_guesses)
    print("You're Awarded With 'THE BEST PERFORMANCE!!'")
    print("---------------------------------------------------")

elif 5<No_of_guesses and No_of_guesses<11 :
    print("Total No. of Guesses are : ",No_of_guesses)
    print("You're Awarded With 'THE GOOD PERFORMANCE!!'")
    print("Now You Can Try To Get 'THE BEST PERFORMANCE!!' Award")
    print("---------------------------------------------------")

elif 10<No_of_guesses and No_of_guesses<20 :
    print("Total No. of Guesses are : ",No_of_guesses)
    print("You're Awarded With 'THE BAD PERFORMANCE!!'")
    print("Try To Get 'THE GOOD PERFORMANCE!!' Award")
    print("Wishing you Good Luck :) ")
    print("---------------------------------------------------")

elif No_of_guesses>19 :
    print("Total No. of Guesses are : ",No_of_guesses)
    print("You're Awarded With 'THE WORST PERFORMANCE!!'")
    print("Try To Get 'THE GOOD PERFORMANCE!!' Award")
    print("Wishing you Good Luck :) ")
    print("---------------------------------------------------")


