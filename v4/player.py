import time


class Player:
    __score = 0
    __name = ''
    __total_questions = 0
    __correct_answers = 0

    def __init__(self, name):
        self.__score = 0
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def update_score(self, score, correct):
        if correct:
            self.__score = self.__score + score
        else:
            self.__score = self.__score - score

        self.__add_question(correct)

    def __add_question(self, correct):
        self.__total_questions += 1
        if correct:
            self.__correct_answers += 1

    def get_correct_answers(self):
        return str(self.__correct_answers)

    def get_total_questions(self):
        return str(self.__total_questions)
    
