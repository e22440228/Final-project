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
    if int(player_string) > 7:
        print('There is too much people in this game.')
        while checkInput(player_string) != True or int(player_string) > 7:
            print('Please reenter again.')
            player_string = input('How many players?\n')
        player = int(player_string)
        return player
    player = int(player_string)
    return player
      
def BlackJack():
    BJplayers = Players()
    d = {}
    special = {11:'J',12:'Q',13:'K'}
    score = {}
    card_appear = {}
    print('Total Players are:',BJplayers)
    for i in range(1,BJplayers+1,1):
        card = random.randint(1,13)
        if card not in card_appear:
            card_appear[card] = 0
        card_appear[card] = card_appear[card] + 1
        
        if card in [11,12,13]:
            print("Player",i,",",special[card])
            card = 10
            if i not in score:
                score[i] = 0
            score[i] = score[i] + card
        else:
            print("Player",i,",",card)
            if i not in score:
                score[i] = 0
            score[i] = score[i] + card
    print(score)
    print(card_appear)
    #while finish != True:
        

BlackJack()
