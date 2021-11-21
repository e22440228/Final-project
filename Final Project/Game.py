import random

def checkInput(value):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    decision = 0
    for check in value:
        if check in numbers:
            decision += 1
        else:
            decision -= 1
    if decision == len(value):
        return True
    else:
        return False

def Players():
    numbers = [0,1,2,3,4,5,6,7,8,9]
    players_list = []
    player_string = input('How many players?\n')
    if checkInput(player_string) != True:
        while checkInput(player_string) != True:
            print('Please reenter again.')
            player_string = input('How many players?\n')
    player = int(player_string)
        
    return player

def BlackJack():
       
Players()
