# This is a guess the number game

import random

name = input("hello. what is your name? ")

print("well, " + name + ", I am thinking of number betweem  1 and 20. ")

secretnumber = random.randint(1, 20)

# print("the secretnumber = " + str(secretnumber) )

for guesstaken in range(1, 7) :
    print("take a guess")
    guess = int(input())

    if guess < secretnumber:
        print(" mistake your guess is too low")

    elif guess > secretnumber:
        print(" mistake your guess is too high")

    else:
        break

if guess == secretnumber:
    print("correct" + " your trys are "+ str(guesstaken)  )

else:
    print ("nope, the number i thinking is : " + str(secretnumber))
  
