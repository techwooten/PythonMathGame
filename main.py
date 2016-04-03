#A simple math addition game
#tutorial at www.techwooten.com

#import random number generator
from random import randint

#use input function to get the players name
person = input('Hello, may I have your name? ')

#used to track score
score = 0

#greet the player
print('Hello, ' + person + '\n')

#this function uses the imported module to get a random number between 0 and 9
def getNumber():
    return randint(0,9)

#a loop to provide the player with 10 math problems
for _ in range(10):
    firstNumber = getNumber() # getting the numbers to be added together
    secondNumber = getNumber()
    # below we ask the player for their answer
    answer = input('What is the answer to ' + str(firstNumber) + ' + ' + str(secondNumber) + '? ')
    # generate the correct answer
    correctAnswer = firstNumber + secondNumber

    # here we validate that the answer provided was the correct answer and update the score
    if(int(answer) == correctAnswer):
        score = score +1
        print('Good Job ' + person + ', your score is ' + str(score) + '\n')
    else:
        score = score -1
        print('Oh no! ' + person + ', you got that answer wrong.  Your score is ' + str(score) + '\n')
