class Game:
    __start_time = 0.0
    __total_questions = 0
    __correct_answers = 0

    def __init__(self):
        self.__startTime = time.time()

    def iteration_time(self):
        return str("%.2f" % (time.time() - self.__startTime)) + ' seconds'

    # this function uses the imported module to get a random number between 0 and 9
    def get_number(self,start, end):
        return randint(start,end)

    def get_total_questions(self):
        return self.__total_questions

    def get_correct_answers(self):
        return self.__correct_answers

    def start_iteration(self):
        # a loop to provide the player with 10 math problems
        for _ in range(10):
            self.__total_questions += 1
            first_number = self.get_number(0, 9) # getting the numbers to be added together
            second_number = self.get_number(0, 9)
            # below we ask the player for their answer
            question = 'What is the answer to ' + str(first_number) + ' + ' + str(second_number) + '? '
            answer = 0
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
                self.__correct_answers += 1
                print('Good Job ' + player.get_name()  + ', your score is ' + str(player.get_score()) + '\n')
            else:
                player.update_score(-1)
                print('Oh no! ' + player.get_name() + ', you got that answer wrong.  Your score is ' +
                      str(player.get_score()) + '\n')