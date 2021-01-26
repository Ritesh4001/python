import random as r #importing module


num = r.randrange(100) # to get a range from 1 to 100

guess =5

while guess >= 0:#applying the loop
    your_guess = int(input("enter your guess"))


    def check(x):#creating a loop
        if your_guess ==x:
            print('you win')
        elif your_guess > x:
            print('you are close please keep trying lower')

        else:
            print('you are close please keep trying higher')


    if guess > 1:
        check(num)

    elif guess == 1:
        check(num)
        print('this your last chance, make the most of it')

    else:
        print("you lost")

        guess = guess-1