import random
import time
import os

clear = lambda: os.system('clear')
line = lambda: print('')
wait = lambda: time.sleep(0.5)

Nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
Suits = ['Spade', 'Heart', 'Diamond', 'Club']
spliter = ' '
deck = [ (suit + spliter + num) for num in Nums for suit in Suits]

dealer = []
player = []

tern = 0

def intro():
    print('BLACKJACK 0.0.1')
    print('Copyright 2017-2019 Potados.')
    wait()
    line()
    print('Loading', end='')
    for i in range(0, 15):
        print('.', end='', flush=True)
        time.sleep(0.08)
    print('complete')
    wait()
    line()
    print('Press enter to start...')
    input()
    clear()

def dealerTurn():
    if calcTotal(dealer) >= 17:
        print('DEALER GOT Nothing')
    while calcTotal(dealer) <= 16:
        delPick(True)
        wait()

def delPick(p):
    dealerPick = deck.pop(deck.index(random.choice(deck)))
    dealer.append(dealerPick)
    if p == True:
        print('DEALER GOT', dealerPick)
    else:
        print('DEALER GOT ???')

def plaPick(p):
    playerPick = deck.pop(deck.index(random.choice(deck)))
    player.append(playerPick)
    if p == True:
        print('YOU GOT', playerPick)

def open(p):
    line()
    print('==============================')
    if p == True:
        print('dealer has', dealer, ', TOTAL', calcTotal(dealer))
    else:
        print('dealer has', dealer[0:1])

    print('you have', player, ', TOTAL' ,calcTotal(player))
    print('==============================')

def calcTotal(L):
    total = 0
    for i in L:
        if i.split(spliter)[1] == 'A':
            total += 11
        elif i.split(spliter)[1] == 'J':
            total += 10
        elif i.split(spliter)[1] == 'Q':
            total += 10
        elif i.split(spliter)[1] == 'K':
            total += 10
        else:
            total += int(i.split(spliter)[1])

    return total

def end(how):
    line()
    win = 'YOU WIN!'
    lose = 'YOU LOSE...'
    draw = 'DRAW'

    if how == 1:
        for i in win:
            for j in range(win.index(i) + 5):
                print(' ', end='')
            print(i)
            wait()
    elif how == 2:
        for i in 'YOU LOSE...':
            print(i)
            wait()
    elif how == 3:
        for i in 'DRAW':
            print('   ', end='')
            print(i)
            wait()

clear()

intro()

print('**game start**')

line()

wait()
plaPick(True)
wait()
plaPick(True)

wait()
line()
wait()

delPick(True)
wait()
delPick(False)

wait()

open(False)

notFirst = False

line()

wait()

print('Your Turn')

wait()

choice = int(input('Hit:1 | Stay:0 > '))

while choice != 0:
    if choice == 1:
        clear()
        plaPick(True)
        wait()
        open(False)
        if calcTotal(player) > 21:
            wait()
            line()
            print('**TOTAL OVER 21**')
            break

    line()

    wait()
    choice = int(input('Hit:1 | Stay:0 > '))

clear()

wait()
print('Your Turn finished')

line()

wait()

dealerTurn()

wait()

open(True)

wait()

line()
print('**Game Finished**')

wait()

if calcTotal(player) <= 21 and calcTotal(dealer) <= 21:
    if calcTotal(player) > calcTotal(dealer):
        end(1)
    elif calcTotal(player) < calcTotal(dealer):
        end(2)
    else:
        end(3)

elif calcTotal(player) <= 21 and calcTotal(dealer) > 21:
    end(1)

elif calcTotal(player) > 21 and calcTotal(dealer) <= 21:
    end(2)

else:
    if calcTotal(player) < calcTotal(dealer):
        end(1)
    elif calcTotal(player) > calcTotal(dealer):
        end(2)
    else:
        end(3)

line()
