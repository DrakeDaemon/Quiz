import json

# Reading JSONs
listof = "list.json"
with open(listof, "r") as f:
    questions = json.load(f)
    
print (questions)
