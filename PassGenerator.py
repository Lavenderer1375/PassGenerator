import string
import random

characters = list(string.ascii_letters + string.digits + "! @ # $ % ^ & * ( ) < > ? | { , } [ ]")

def passGenerator():
    length = int(input("ENter the lenght of password:\n"))
    random.shuffle(characters)

    passWord = []
    for i in range(length):
        passWord.append(random.choice(characters))

    random.shuffle(passWord)

    print("".join(passWord))

user_input = ""
while user_input != "done":
    passGenerator()
