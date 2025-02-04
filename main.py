import json
import time
import random as rand


# * Game
with open('questions.json', "r") as f:   # Json reader
    questions = json.load(f)

# ! BAD CODE NEEDS REWORKING
random = rand.choice(questions)
random1 = rand.choice(questions) 
quest = random['A'],random['B'],random['C'],random['D']
quest1 = random1['A'],random1['B'],random1['C'],random1['D']
print(random['prompt'])
answer = input(quest)

if answer == random['answer']: # Game itself
    print('Correct')
    print(random1['prompt'])
    answer = input(quest1)
    if answer == random1['answer']:
        print('Correct')
    else:
        print('Incorrect')
else: 
    print('Incorrect')    

# * GUI
