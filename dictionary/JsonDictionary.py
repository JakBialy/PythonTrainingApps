import json
from difflib import get_close_matches


def find_in_dictionary():
    look_for = input("Enter a word please")
    look_for_lower = look_for.lower()
    if look_for in data:
        return data[look_for]
    elif look_for_lower in data:
        return data[look_for_lower]
    elif len(get_close_matches(look_for_lower, data.keys())) > 0:
        user_response = input(
            "Did you mean %s instead? Enter Y is yes or N is no" % get_close_matches(look_for_lower, data.keys(), 1,
                                                                                     0.8))
        if user_response == "Y":
            return data[get_close_matches(look_for_lower, data.keys(), 1, 0.8)[0]]
        elif user_response == "N":
            return "The word doesn't exist, please double check"
        else:
            return "We didn't understand your entry"
    else:
        return "No such word in a dictionary"


while True:
    data = json.load(open("data.json"))
    dictionary_answer = find_in_dictionary()
    if type(dictionary_answer) == list:
        for statement in dictionary_answer:
            print(statement)
    else:
        print(dictionary_answer)

    answer = input("Would you like to ask for something else? If yes press Y if not press N")
    if answer == "N":
        break

