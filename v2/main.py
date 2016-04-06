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
    __startTime = 0.0
    __totalQuestions = 0
    __correctAnswers = 0
    
    def __init__(self):
        self.__startTime = time.time()

    def setFinishTime(self):
        self.__finishTime = time.time()

    def iterationTime(self):
        return str("%.2f" % (time.time() - self.__startTime)) + ' seconds'

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
            question = 'What is the answer to ' + str(firstNumber) + ' + ' + str(secondNumber) + '? '
            answer = 0
            badCount = 0
            while True:
                try:
                    if(badCount > 3):
                        break
                    answer = int(input(question))
                    break
                except ValueError:
                    print('Opps, your answer needs to be a number \n')
                    badCount += 1
            
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

#create a new Player Object
player = Player(name)

#greet the player
print('Hello, ' + player.getName()  + '\n')

#create a new Game Object
game = Game()

#create a while loop to validate their input
while True:
    #ask them if they want to play
    play = input('Would you like to play a game? (Yes/No)')
    #if their answer is not either yes or no require them to answer the question again
    if play.lower() not in ('yes','no'):
        #let user know they need to put in a correct answer
        print('Please type either yes or no')
    else:
        # if they did answer yes or no this will run
        if play.lower() == 'yes':
            #if their answer was yes then we start the game
            game.startIteration()
            #after one iteration of the game runs let them know how many correct answers they got and their time
            print('You have answered ' + str(game.getCorrectAnswers()) + ' right in ' + str(game.iterationTime()))
            # would they like to play again
            play = input('Would you like to play a game? (Yes/No)')
        # if they said no they don't want to play again then break out of the validation loop
        if play.lower() == 'no' :
            print('Ok, maybe next time')
            break
                 




