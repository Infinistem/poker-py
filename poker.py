# just poker. I made cuz gambling is cool and totally risk free and you should try it :)
# btw if you dont get that to be satire you probably will loose all your money anyways
import math, random, sys, tkinter as tk, asyncio, os, time
from tkinter import *
from tkinter import ttk
from collections import Counter # a cool lib i never knew existed. Saved me a tiny bit of time, although counting my own instances wouldnt be that hard
from PIL import Image, ImageTk
'''  2
1          3
     0
'''
rt = "Images/"
class Game:
    def __init__(self, board, moneydisps): # 3 bots, 1 human
        self.playerTurn = 0
        self.botsDisplay = moneydisps
        self.board = board
        self.deck = self.deck()
        self.hands = [Hand(self.deck), Hand(self.deck), Hand(self.deck), Hand(self.deck)]
        self.money = [1000,1000,1000,1000]
        self.round = 'flop'
        self.gameOver = True
        self.turn = 1
        self.counts = 0
        self.lastBet = None
        self.dealer = 0
        self.ranking = ["High Card", "Pair", "Two Pair", "Three of a Kind", "Full House"]
        self.center = [] # card classes
    def deck(self):
        deck = []
        for x in ['hearts', 'spades', 'clubs', 'diamonds']:
            for y in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]:
                deck.append(str(y) + '_of_' + str(x))
        random.shuffle(deck)
        return deck
    def playGame(self):
        if self.round == 'flop':
            self.flop()
            self.betBlinds()
            self.gameOver = False
            self.bettinground()
        if not self.gameOver and self.counts == 4: 
            self.playGame()
    def bettinground(self):
        if not self.turn == 0 and self.counts < 4:
            botHand = self.evalHand(self.fullHand(self.hands[self.turn])) # what hand does the bot have determines how it plays
            print(botHand)
            self.botThink(botHand)
            self.changeTurn()
            self.counts+=1
            self.bettinground() 
    def humanBet(self):
        pass
    def changeTurn(self):
        if not self.turn == 3:
            self.turn+=1
        else:
            self.turn = 0
    def bet(self, money):
        self.money[self.turn]-=money
        self.botsDisplay[self.turn].config(text="Money: $" + str(self.money[self.turn]))
    def fullHand(self, x):
        a = self.center
        a.extend(x)
        return a
    def betBlinds(self):
        pass
    def flop(self):
        for x in range(3):
            r = random.randint(0, len(self.deck)-1)
            e = Card(rt + self.deck[r])
            self.deck.remove(e.orig)
            self.center.append(e)
        for x in range(len(self.center)):
            y = Image.open(self.center[x].img).resize((140, 200))
            img1 = ImageTk.PhotoImage(y)
            panel = Label(self.board, width=140, height=200)
            panel.image=img1
            panel.configure(image=img1)
            panel.place(x=150*x, y=40)
        
    def _turn(self):
        pass
    def river(self):
        pass
    def displayHand():
        pass           
    def evalHand(self,fullHanda): # array of cardclasses
        myHand = ''
        suits = [x.suit for x in fullHanda]
        ranks = [x.rank for x in fullHanda]
        counts = 0
        instance_suits = Counter(suits)
        instance_cards = Counter(ranks) 
        sorted_handc = list()
        for x in fullHanda:
            sorted_handc.append(x.rank)
        sorted_handc.sort()
        print(list(instance_cards.values()))
        if 2 in list(instance_cards.values()):
            myHand = 'Pair'
        if list(instance_cards.values()).count(2) == 2:
            myHand = 'Two Pair'
        if 3 in list(instance_cards.values()):
            myHand = 'Three of a Kind'
        if counts == 5:
            myHand = 'Straight'
        if 5 in instance_suits:
            myHand = 'Flush'
        if 4 in list(instance_cards.values()):
            myHand = 'Four of a Kind'
        if counts == 5 and 5 in list(instance_suits.values()):
            myHand = 'Straight Flush'
        if list(instance_cards.values()).count(1) == len(list(instance_cards.values())):
            myHand = 'High Card'
            
        return myHand
    def makeBet(player, money):
        self.money[player]-=money
    @property
    def getrn(self):
        return self.round
    def getprb(self): # get the probability of a card createing a good hand. For advanced bots
        pass
    def botThink(self, hand):
        ranking = self.ranking.index(hand)
        self.bet(10)
        '''doBluff = random.choice([True, False, False, False])
        doRaise = None
        if doBluff:
            add = random.randint(10,20)'''
class Card():
    def __init__(self, raw):
        self.orig = raw
        self.raw = raw.split("_")
        self.suit = self.raw[2]
        self.rank = self.raw[0]
        self.img = raw + '.png'
def Hand(deck):
    hand = []

    for x in range(2):
        r = random.randint(0, len(deck)-1)
        e = Card(rt + deck[r])
        hand.append(e)
        deck.remove(e.orig)
    return hand
def GETEXDIR():
    try:
        pass
    except Exception:
        sys._MEIPASS()
        pass
def playAgain():
    global game
    game = Game(board, [m1, m2, m3, m4])
    game.playGame()


root = Tk()
# menu: Game, Options, Help
menuRoot = Menu(root)
gm = Menu(menuRoot)
menuRoot.add_cascade(label="Game", menu=gm)
menuRoot.add_cascade(label="Options", menu=gm)
menuRoot.add_cascade(label="Help", menu=gm)

gm.add_command(label="New Game", command=lambda:playAgain())
root.state('zoomed')
root.title("Texas Hold'em Poker - Windows Edition")
table = Frame(root, width=1400, height=800, background="green")
table.place(x=100, y=10)
board = Frame(table, width=750, height=270, background="lightgreen")
Label(table, text="90% of Gamblers Quit before they win big!!", font=("Arial", 17)).place(x=480, y=0)
board.place(x=300, y=230)
bot1, bot2, bot3 = Frame(root, width=200, height=200, background="darkcyan"),Frame(root, width=200, height=200, background="darkcyan"),Frame(root, width=200, height=200, background="darkcyan")
bot1.place(x=140, y=400)
bot2.place(x=650, y=40)
bot3.place(x=1200, y=400)
playerspot = Frame(root, width=350, height=300, background="lime")
playerspot.place(x=600, y=500)
e=Entry(playerspot)
e.place(x=50, y=30)

m1 = Label(playerspot, text="Money: $1000", font=("Arial", 16), background="gold")
m1.place(x=100, y=0)
m2 = Label(bot1, text="Money: $1000", font=("Arial", 16), background="gold")
m2.place(x=0, y=0)
m3 = Label(bot2, text="Money: $1000", font=("Arial", 16), background="gold")
m3.place(x=0, y=0)
m4 = Label(bot3, text="Money: $1000", font=("Arial", 16), background="gold")
m4.place(x=0, y=0)

Button(playerspot, text="Bet").place(x=180, y=30)
Button(playerspot, text="Call", width=9).place(x=210, y=30)
Button(playerspot, text="Fold", width=9).place(x=270, y=30)



root.configure(menu=menuRoot)
game = Game(board, [m1, m2, m3, m4])


root.mainloop()


