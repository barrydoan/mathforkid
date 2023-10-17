import random
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def print_history(history):
    for i in history:
        print(i)

correct_answer = 0
change_question = True
x = 0
y = 0
history = []

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

clear()

for i in range(10):
    if change_question:
        x = random.randrange(20)
        y = random.randrange(20)
    result = input(f"{color.GREEN}{x} + {y} = {color.END}")
    result = int(result)
    clear()
    if result == (x + y):
        correct_answer+=1
        change_question = True
        history.append(f"{color.GREEN}{x} + {y} = {result}{color.END}")
        print_history(history=history)
        print(f"{color.GREEN}Your answer is correct!{color.END}")
    else:
        change_question = False
        history.append(f"{color.RED}{x} + {y} = {result}{color.END}")
        print_history(history=history)
        print(f"{color.RED}Your answer is incorrect!{color.END}")
clear()
print_history(history=history)
print(f"{color.GREEN}You have just finished your math. This is your score: {correct_answer * 10}{color.END}")