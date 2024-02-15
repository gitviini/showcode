import os
from time import sleep

def clear():
    if (os.name == 'posix'):
        os.system('clear')
    else: os.system('cls')

def get_path():
    return os.getcwd()

path = get_path()

play = True

while(play):
    try:
        option = int(input())
        sleep(1)
    except Exception as erro: print(erro)
