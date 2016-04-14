# A simple math addition game
# tutorial at www.techwooten.com

# import random number generator
from random import randint


class Player:
    __score = 0
    __name = ''

    def __init__(self, name):
        self.__score = 0
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def update_score(self, score):
        self.__score = self.__score + score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


# use input function to get the players name
name = input('Hello, may I have your name? ')

# create a new Player Object
player = Player(name)

# greet the player
print('Hello, ' + player.get_name()  + '\n')

# this function uses the imported module to get a random number between 0 and 9
def get_number(start, end):
    return randint(start, end)

# create a while loop to validate their input
while True:
    # ask them if they want to play
    play = input('Would you like to play a game? (Yes/No)')
    # if their answer is not either yes or no require them to answer the question again
    if play.lower() not in ('yes','no'):
        # let user know they need to put in a correct answer
        print('Please type either yes or no')
    else:
        # if they did answer yes or no this will run
        if play.lower() == 'yes':
            for _ in range(10):
                first_number = get_number(0,9) # getting the numbers to be added together
                second_number = get_number(0,9)
                # below we ask the player for their answer
                question = 'What is the answer to ' + str(first_number) + ' + ' + str(second_number) + '? '
                bad_count = 0
                while True:
                    try:
                        if bad_count > 3:
                            break
                        answer = int(input(question))
                        break
                    except ValueError:
                        print('Opps, your answer needs to be a number \n')
                        bad_count += 1

                # generate the correct answer
                correct_answer = first_number + second_number
                    
                # here we validate that the answer provided was the correct answer and update the score
                if int(answer) == correct_answer:
                    player.update_score(+1)
                    print('Good Job ' + player.get_name()  + ', your score is ' + str(player.get_score()) + '\n')
                else:
                    player.update_score(-1)
                    print('Oh no! ' + player.get_name() + ', you got that answer wrong.  Your score is ' +
                          str(player.get_score()) + '\n')

            play = input('Would you like to play a game? (Yes/No)')
            # if they said no they don't want to play again then break out of the validation loop
        if play.lower() == 'no' :
            print('Ok, maybe next time')
            break
                 




