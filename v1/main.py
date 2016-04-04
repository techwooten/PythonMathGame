#A simple math addition game
#tutorial at www.techwooten.com

#import random number generator
from random import randint

#use input function to get the players name
name = input('Hello, may I have your name? ')

#used to track score
score = 0

#greet the player
print('Hello, ' + name  + '\n')

#this function uses the imported module to get a random number between 0 and 9
def getNumber(start, end):
    return randint(start,end)

#a loop to provide the player with 10 math problems
for _ in range(10):
    firstNumber = getNumber(0,9) # getting the numbers to be added together
    secondNumber = getNumber(0,9)
    # below we ask the player for their answer
    answer = input('What is the answer to ' + str(firstNumber) + ' + ' + str(secondNumber) + '? ')
    # generate the correct answer
    correctAnswer = firstNumber + secondNumber

    # here we validate that the answer provided was the correct answer and update the score
    if(int(answer) == correctAnswer):
        score = score +1
        print('Good Job ' + name  + ', your score is ' + str(score) + '\n')
    else:
        score = score -1
        print('Oh no! ' + name + ', you got that answer wrong.  Your score is ' + str(score) + '\n')
