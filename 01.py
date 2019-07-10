# -*- coding: UTF-8 -*-

# author by : Steven Lu

import random
import codecs
import copy

jokers = ('♞', '♘')

marks = ('♠', '♥', '♦', '♣')

nums = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

deck = []
for c in jokers:
    deck.append(c)

for cn in nums:
    for cm in marks:
        card = cm + cn
        deck.append(card)

print('create my deck, total cards is %d,detail is: \n%s:' % (len(deck), deck))

f = codecs.open("Pocker.txt", "w", "utf-8")
for card in deck:
    f.write(card)
    f.write('\t')
f.close()
'''
shuffledDeck = []
count = len(deck)
for i in range(count):
    pickedCard = random.choice(deck)
    shuffledDeck.append(pickedCard)
    deck.remove(pickedCard)
'''
shuffledDeck=copy.copy(deck)
random.shuffle(shuffledDeck)

print('shuffledDeck cards is %d,detail is: \n%s:'
      % (len(deck), deck))
print('new deck cards is %d,detail is: \n%s:'
      % (len(shuffledDeck), shuffledDeck))

f = codecs.open("poker_new.txt", "w", "utf-8")
for card in shuffledDeck:
    f.write(card)
    f.write('\t')
f.close()

nums_Players=2
Player=int(len(shuffledDeck)/nums_Players)
print('%d players,%d cards'% (nums_Players, Player))

player1=[]
for i in range(Player):
    picked=random.choice(shuffledDeck)
    player1.append(picked)
    shuffledDeck.remove(picked)
print('player1 %d,detail is: \n%s:'
      % (len(deck), deck))
print( 'player1 new deck cards is %d,detail is: \n%s:'
      % (len(shuffledDeck), shuffledDeck))

player2=[]
for i in range(Player):
    picked=random.choice(shuffledDeck)
    player2.append(picked)
    shuffledDeck.remove(picked)
print('player2 %d,detail is: \n%s:'
      % (len(deck), deck))
print( 'player2 new deck cards is %d,detail is: \n%s:'
      % (len(shuffledDeck), shuffledDeck))
