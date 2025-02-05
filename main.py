import json
import random as rand

# JSON reader
with open('questions.json', "r") as f:  
    questions = json.load(f)

# Game functions

# Questions, choices, answers.
def quiz(questions):
    i = 0
    while i != 1:
        i += 1
        try:
            print(questions['prompt'])
            print(questions['choices'])
            answer = input('Your answer: ')
            if answer == questions['answer'].casefold():
                print('Correct.')
                return True
            elif answer.casefold() == 'exit':
                exit()
            else:
                print('\nIncorrect.\n')
                return False
        except ValueError:
            print('Incorrect data. Restart programm.')
            exit()

# Number of questions, starts quiz
def start():
    try:
            # Keep track of asked question indices
            asked_questions = set()  
            y = 0 # Number of questions
            num = 0 # Max number of questions
            while True:
                num = int(input('Enter number of questions(1-39): '))
                if num > 0 and num <= 39:
                    break
                else:
                    print('Please enter correct number.')
            # Not fully understood (used chat gpt).
            for i in range(num):
                while True:
                    rand_index = rand.randint(0, len(questions) - 1)
                    if rand_index not in asked_questions:
                        asked_questions.add(rand_index)
                        current_question = questions[rand_index]
                        break
                print(f'Question {i+1} out of {num}:')
                quiz(current_question)
                if y == num:
                    break
    except ValueError:
            print('Incorrect data. Restart programm.')
            exit()

# Keeps programm running
if __name__ == "__main__":
    start()