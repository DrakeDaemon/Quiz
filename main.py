import json
import time


# * Game
with open('list.json', "r") as f:   # Json reader
    questions = json.load(f)    
 # ! BAD CODE NEEDS REWORKING
print(questions[0]['prompt'])
answer = input(questions[0]['options'])

if answer == questions[0]['answer']: # Game itself
    print('Correct')
    print(questions[1]['prompt'])
    answer = input(questions[1]['options'])
    if answer == questions[1]['answer']:
        print('Correct')
    else:
        print('Incorrect')
else: 
    print('Incorrect')    

# * GUI
