import json
import difflib

from difflib import get_close_matches

data = json.load(open('dictionary.json'))

def retrieve_definition(word):

    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0:
        action = input("did you mean this %s instead? [y:n]" %get_close_matches(word, data.keys())[0])
        if action == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif action == 'n':
            return ("word not in dict")
        else:
            return ("action not recognised")
word_user = input("Enter a key:")

output = retrieve_definition(word_user)

if type(output) == list:
    for item in output:
        print("-", item)
else:
    print("-", output)