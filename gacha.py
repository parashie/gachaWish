import math
from random import choices

def rules():
    print('this simulates the gacha rolling process of popular game Genshin Impact \n We will be following similar rules as the game, but with a few changes \n For simplicity reasons, we will only have unspecified stars')

def rates():
    print('the rates will follow this pattern \n 5 star rate is 0.6% \n 4 star rate is 6% \n 3 star rate is 93.4%')

def wishRules():
    print('You will be asked to choose between 1 roll or 10 rolls \n we will not be using pity to increase drop rates')

print('Welcome to our wish simulator')
rules()
rates()
wishRules()

# this function will be used to simulate the gacha rolls
def wish():
    # we seperate the single wishes and 10 wishes
    wishes = int(input('How many wishes would you like to do? '))
    # single wish
    if wishes == 1:
        print('You have chosen to do 1 wish')
        for i in range(1):
            # our drops, and their rates are stored in a list
            roll = choices(['5 star', '4 star', '3 star'], [0.6, 6, 93.4])
            #return the results to the user
            print(roll)
    # 10 wishes
    elif wishes == 10:
        print('You have chosen to do 10 wishes')
        for i in range(10):
            # our drops, and their rates are stored in a list
            roll = choices(['5 star', '4 star', '3 star'], [0.6, 6, 93.4])
            #return the results to the user
            print(roll)
    else:
        # if the user inputs anything other than 1 or 10, we will ask them to try again
        print('Please enter 1 or 10')
        wish()


wish()

# this is to ask the user if they would like to do another wish
wishAgain = input('Would you like to do another wish? ')

# if the user inputs yes, we will run the wish function again
while wishAgain == 'yes' or wishAgain == 'Yes' or wishAgain == 'YES' or wishAgain == 'y' or wishAgain == 'Y':
    wish()
    wishAgain = input('Would you like to do another wish? ')
# if the user inputs anything other than yes, we will end the program
else:
    print('goodbye')



