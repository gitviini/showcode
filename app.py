import os
from time import sleep


path = os.getcwd()

run = True

ERRO = 'valor invalido'

def clear():
    if (os.name == 'posix'):
        os.system('clear')
    else: os.system('cls') 

def get_path(path = ''):
    list = os.listdir(path)
    for item in list:
        print(item)

while(run):
    option = 0
    try:
        option = int(input('0)EXIT\n1)SHOW PATH\n2):'))
        match option:
            case 0:
                run = False

            case 1:
                pass
            case _:
                print(ERRO)
    except Exception as erro: print(erro)
