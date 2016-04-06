#A simple math addition game
#tutorial at www.techwooten.com

#import random number generator
from random import randint
import time

class Player:
    __score = 0
    __name = ''

    
    def __init__(self, name):
        self.__score = 0
        self.__name = name

    def setName(self, name):
        self.__name = name

    def updateScore(self, score):
        self.__score = self.__score + score

    def getName(self):
        return self.__name

    def getScore(self):
        return self.__score

class Game:
    __startTime = 0
    __finishTime = 0
    __totalQuestions = 0
    __correctAnswers = 0
    
    def __init__(self):
        self.__startTime = time.time()

    def setFinishTime(self):
        self.__finishTime = time.time()

    def iterationTime(self):
        return str((self.__startTime - self.__finishTime)/60) + 'min'

    #this function uses the imported module to get a random number between 0 and 9
    def getNumber(self,start, end):
        return randint(start,end)

    def getTotalQuestions(self):
        return self.__totalQuestions

    def getCorrectAnswers(self):
        return self.__correctAnswers

    def startIteration(self):
        #a loop to provide the player with 10 math problems
        for _ in range(10):
            self.__totalQuestions += 1
            firstNumber = self.getNumber(0,9) # getting the numbers to be added together
            secondNumber = self.getNumber(0,9)
            # below we ask the player for their answer
            answer = input('What is the answer to ' + str(firstNumber) + ' + ' + str(secondNumber) + '? ')
            # generate the correct answer
            correctAnswer = firstNumber + secondNumber
            
            # here we validate that the answer provided was the correct answer and update the score
            if(int(answer) == correctAnswer):
                player.updateScore(+1)
                self.__correctAnswers += 1
                print('Good Job ' + player.getName()  + ', your score is ' + str(player.getScore()) + '\n')
            else:
                player.updateScore(-1)
                print('Oh no! ' + player.getName() + ', you got that answer wrong.  Your score is ' + str(player.getScore()) + '\n')
                


#use input function to get the players name
name = input('Hello, may I have your name? ')

player = Player(name)

#greet the player
print('Hello, ' + player.getName()  + '\n')

play = input('Would you like to play a game? (Yes/No)')
game = Game()
while(play == 'Yes'):
    game.startIteration()
    print('You have answered ' + str(game.getCorrectAnswers()) + ' right in ' + str(game.iterationTime())
    play = input('Would you like to play a game? (Yes/No)')

if play == 'No' :
    print('Ok, maybe next time')
else:
    print('Please type either Yes or No')



