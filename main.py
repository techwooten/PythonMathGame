from random import randint

person = input('Hello, may I have your name? ')
score = 0

print('Hello, ' + person + '\n')

def getNumber():
    return randint(0,9)

for _ in range(10):
    firstNumber = getNumber()
    secondNumber = getNumber() 
    answer = input('What is the answer to ' + str(firstNumber) + ' + ' + str(secondNumber) + '? ')
    correctAnswer = firstNumber + secondNumber
    
    if(int(answer) == correctAnswer):
        score = score +1
        print('Good Job ' + person + ', your score is ' + str(score) + '\n')
