import random

answer = random.randint(1, 100)
correct = False
while correct == False:
    guess = int(input('guess='))
    print('Your guess is', guess)
    if guess == answer :
        print('Good guess')
        correct = True
    elif guess < answer:
        print('Too low')
    else:
        print('Too high')