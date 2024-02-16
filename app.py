import os
from time import sleep

path = os.getcwd()

fouder = 'files'

text = '0)EXIT\n1)SHOW DIR\n2)NEW\n3)EDIT\n4)DELETE\n:'

run = True

ERRO = '\033[31minvalid value\033[m'

def fouder_exists(path = '', fouder = '') -> any:
    list = os.listdir(path)
    exists = False
    for item in list:
        if item == fouder: exists = True
    
    if exists == False:
        os.mkdir(fouder)
        print('fouder_exists:. \033[32;3mcreate fouder\033[m')
    else: print('fouder_exists:. \033[33;3mfouder exists\033[m')

def new_file(path = '', name_file = '', fouder = '') -> any:
    try:
        os.system(f'echo "" > {os.path.join(path,fouder,name_file)}')
        print(f'\033[32msucess\033[m:. \033[;3mnew file {name_file} created.\033[m')
        sleep(1.5)
    except: 
        print(f'new_file:. \033[33;3merror create new file "{name_file}\033[m"')
        sleep(1.5)

def delete_file(path = '', name_file = '', fouder = '') -> any:
    try:
        if os.name == 'posix':
            os.system(f'rm -r {os.path.join(path,fouder,name_file)}')
            print(f'delete_file:. \033[;3m{name_file} deleted\033[m')
        elif os.name == 'nt':
            os.system(f'erase {os.path.join(path,fouder,name_file)}')
            print(f'delete_file:. \033[;3m{name_file} deleted\033[m')
    except: print(f'delete_file:. \033[31;3m{name_file} not deleted\033[m')

def clear() -> any:
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls') 

def get_files(path = '', fouder = '') -> any:
    list = os.listdir(os.path.join(path, fouder))
    for item in list:
        print(f'\033[;3m-> {item}\033[m')

while(run):
    option = 0
    try:
        clear()
        option = int(input(text))
        clear()
        match option:
            case 0:
                print('\033[31m...\033[m')
                sleep(0.5)
                run = False
                os.close()
            case 1:
                fouder_exists(path, fouder)
                get_files(path, fouder)
            case 2:
                name = input('new file name\n:')
                if name.find(' ') == -1 or name != '':
                    fouder_exists(path, fouder)
                    new_file(path, name, fouder)
                else: print(ERRO)
            case 3:
                pass
            case 4:
                get_files(path, fouder)
                name = input('choose file will delete\n:')
                if name.find(' ') == -1 or name != '':
                    delete_file(path, name, fouder)
                else: print(ERRO)
            case _:
                print(ERRO)
        sleep(1.5)
    except: 
        print(ERRO)
        sleep(1.5)
