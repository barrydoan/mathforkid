import random

correct_answer = 0

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

for i in range(10):
    x = random.randrange(20)
    y = random.randrange(20)
    result = input(f"{color.GREEN}{x} + {y} = ")
    result = int(result)
    if result == (x + y):
        correct_answer+=1
        print(f"Your answer is correct!{color.END}")
    else:
        print(f"{color.RED}Your answer is incorrect!{color.END}")

print(f"{color.GREEN}You have just finished your math. This is your score: {correct_answer * 10}{color.END}")