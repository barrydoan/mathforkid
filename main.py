import random

correct_answer = 0

for i in range(10):
    x = random.randrange(20)
    y = random.randrange(20)
    result = input(f"{x} + {y} = ")
    result = int(result)
    if result == (x + y):
        correct_answer+=1
        print("Your answer is correct!")
    else:
        print("Your answer is incorrect!")

print(f"You have just finished your math. This is your score: {correct_answer * 10}")