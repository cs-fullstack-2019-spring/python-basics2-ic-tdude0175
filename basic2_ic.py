import random
def main():
    # problem1()
    # problem2()
    # problem3()
    problem4()
# Create a function that has two variables.
# One called greeting and nother called myName.
# Print out greeting and myName two different ways without using the following examples
#
# print(greeting + myName)
# print(greeting, myName)

# first one works
# not enough arguments to format string
# need a space for second way
# don't need anything between the two if you put a space inside the variable called
# the information end NEEDS to be inside quotation marks for it to be located


def problem1():
    name = input("What is your name?")
    greeting = ("Hello there ")
    print(f"{greeting}  {name}")
    print("%s %s" % (greeting,name))
    print('{0}{1}' .format(greeting,name))

# Create a function that asks the user for a secret password.
# Create a loop that quits with the user's quit word.
# If the user doesn't enter that word, ask them to guess again.
# .lower is not working? need to put() at the end of it
# quit word? 3 inputs?
# how can you use string formatting?

def problem2():
    secretPassword = input("what will your password be set to?")
    while(True):
        userInput = input("please confirm password")
        if(userInput.upper() == "QUIT"):
            break
        elif(userInput == secretPassword):
            break
        elif(userInput != secretPassword):
            print("guess again.")
# Create a function that prints 0 to 100 three times in a row (vertically).

# ? range? loop inside loop?
#

def problem3():
    for y in range(3):
        for x in range(0,101):
            print(x)
# Create a random number.
# Ask the user to guess the random number.
# Keep letting the user guess until they get it right, then quit.
# random.randint
# have to import random
# random has no attribute .randomint
# if based on trying a certain amount of times it needs to be higher due to priority

def problem4():
    targetNumber = (random.randint(1,50))
    tries = 0

    while(True):
        userInput = int(input("guess a number between 1 and 50"))
        tries+=1
        if(tries==3):
            print("sorry you lose")
            break
        elif(userInput> targetNumber):
            print("that's to high")
        elif(userInput< targetNumber):
            print("that's to low")
        elif(userInput==targetNumber):
            print("good job")
            break
# Ask the user to create a number for the computer to guess.
# Create random numbers until the computer gets that number.
# Once it guesses the number, alert the user how many times it took to guess the random number.



if __name__ == '__main__':
    main()