import random

def generate():
    number_of_the_text = random.randint(1, 5)
    with open("../texts/""text" + str(number_of_the_text) + ".txt", mode='rt') as file:
        text = " ".join(file.read().split())
        return text

