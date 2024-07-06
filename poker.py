# just poker. I made cuz gambling is cool and totally risk free and you should try it :)
# btw if you dont get that to be satire then you probably will loose all your money anyways!

#note: the code could easily be divided into multiple files, however this was just ment as a tiny project
import random, sys, tkinter as tk, os
from tkinter import *
from tkinter import ttk
from collections import Counter # so that i dont have to write a ton of loops for evaluating hands which is boring
from PIL import Image, ImageTk
from threading import Timer

raiseby = None
class Game:
    def __init__(self, board, moneydisps): # 3 bots, 1 human
        self.playerTurn = 0
        self.botsDisplay = moneydisps
        self.board = board
        self.deck = self.deck()
        self.hands = [Hand(self.deck), Hand(self.deck), Hand(self.deck), Hand(self.deck)]
        self.outs = [False, False, False, False]
        self.money = [100,100,100,100]
        self.round = 'flop'
        self.gameOver = True
        self.turn = 1
        self.counts = 0
        self.winner = str
        self.otherThanCheck = None
        self.dealer = 0
        self.playerhasbet = False
        self.ranking = ["High Card", "Pair", "Two Pair", "Three of a Kind", "Full House", "Straight", "Flush", "Four of a Kind", "Straight Flush", "Royal Flush"]
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
            self.round = 'turn'

            for x in range(2):
                y = Image.open(Card(self.deck[random.randint(1, len(self.deck)-1)]).img).resize((140, 200))
                img1 = ImageTk.PhotoImage(y)
                panel = Label(playerspot, width=140, height=200)
                panel.image=img1
                panel.configure(image=img1)
                panel.place(x=150*x, y=50)
            self.betBlinds()
        elif self.round == 'turn':
            self._turn()
            self.round = 'river'
        elif self.round == 'river':
            self.river()
            self.round = 'over'

             # antee/blinds
       
        self.bettinground(1)
        self.bettinground(2)
        self.bettinground(3)

        self.gameOver = False
        if not self.gameOver and self.playerhasbet: 
            self.playerhasbet = False
            if self.round != 'river':
                self.playGame()
        else:
            # end game
            pass
            
           # self.display("Game Over! Winner: " + self.winner)
    def overGetWinner():
        for x in self.money:
            if x <= 0 and not self.winner(self.money.index(x)):
                pass
    def bettinground(self, x):
        self.counts+=1
        if not self.turn == 0:
            botHand = self.evalHand(self.fullHand(self.hands[self.turn])) # what hand does the bot have determines how it plays
            self.botThink(botHand,x,False)
            self.changeTurn()
    def display(txt):
        t.config(text=txt)

    def changeTurn(self):
        if self.turn != 3:
            self.turn+=1
        else: 
            self.turn = 0
    def changeDealer(self):
        if self.dealer != 3:
            self.dealer+=1
        else: 
            self.dealer = 0
    def bet(self, m, t):
        print(self.money[t])
        self.botsDisplay[t].config(text="Money: $" + str(self.money[t])) 
        #t = Timer(3, party_time, args=None, kwargs=None) 
     
    def fullHand(self, x):
        a = []
        a.extend(x)
        a.extend(self.center)

        return a
    def nextd(self, n):
         if not self.dealer == 3:
            return self.dealer+1
         else:
            return 0
    def betBlinds(self):
        for x in range(self.nextd(1), self.nextd(2)):
            self.money[x]-=2
            self.botsDisplay[x].config(text="Money: $" + str(self.money[self.turn]))
    def flop(self):
        for x in range(3):
            r = random.randint(0, len(self.deck)-1)
            e = Card(self.deck[r])
            self.deck.remove(e.orig)
            self.center.append(e)
        self.place()
    def _turn(self):
         self.counts = 0
         r = random.randint(0, len(self.deck)-1)
         e = Card(self.deck[r])
         self.deck.remove(e.orig)
         self.center.append(e)
         self.place()
    def river(self):
         self.counts = 0
         print(self.center)
         r = random.randint(0, len(self.deck)-1)
         e = Card(self.deck[r])
         self.deck.remove(e.orig)
         self.center.append(e)
         self.place()
    def place(self):
         for x in range(len(self.center)):
            y = Image.open(self.center[x].img).resize((140, 200))
            img1 = ImageTk.PhotoImage(y)
            panel = Label(self.board, width=140, height=200)
            panel.image=img1
            panel.configure(image=img1)
            panel.place(x=150*x, y=40)
    def displayHand(self):
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
    def handSum(self, hand): 
        pass
    def callOrFold(self, player):
        pass
    def botThink(self, hand, x, raiseRound): # simple betting stratagies: not that great either. I will come back and updtate them eventually but just wanted a playable game
        ranking = self.ranking.index(hand)
        mon = random.randint(1, 10) + ranking
        if raiseRound:
            return
        self.money[self.turn]-=mon
        ### each bot has a different behavior, kind of like the pacman ghosts (WILL EVENTUALLY HAVE)
        if self.turn == 1:
            if 1-self.dealer == 0:
                pass # possibility of check
            addition = random.randint(1, 4) # fluctuaction in bet
        elif self.turn == 2:
            pass
        elif self.turn == 3:
            pass

          #  self.outs[self.turn] = True
        #doRaise = None   # fold logic
        t=Timer(x, function=initbet, args=[mon, self.turn])
        t.start()
        
def initbet(m, t):
    game.bet(m, t)
def hubet():
    if game.turn == 0 and not game.outs[0]:
        money = int(e.get())
        game.money[0] -=money
        game.botsDisplay[0].config(text="Money: $" + str(game.money[0])) 
        game.playerhasbet = True
        game.turn = 1
        game.playGame()
def raiseEveryone():
    for x in range(1, 3):
        game.botThink(game.hands[x], 1, True) # bet again
def fold():
    game.outs[0] = True
    game.playerhasbet = True
    game.turn = 1
    game.playGame()
        
        
class Card:
    def __init__(self, raw):
        self.orig = raw
        self.raw = raw.split("_")
        self.suit = self.raw[2]
        self.rank = self.raw[0]
        self.img = 'Images/' +raw + '.png'
def Hand(deck):
    hand = []
    for x in range(2):
        r = random.randint(0, len(deck)-1)
        e = Card(deck[r])
        hand.append(e)
        deck.remove(e.orig)
    return hand
def playAgain():
    global game
    game = Game(board, [m1, m2, m3, m4])
    for x in board.winfo_children():
        x.destroy()
    game.playGame()
def handwindow():
    win = tk.Toplevel(root)
    win.geometry("500x600")
    win.title("Hands")
    win.resizable(False, False)
    y = Image.open("Images\hands.jpg")
    img1 = ImageTk.PhotoImage(y)
    panel = Label(master=win, width=500, height=600)
    panel.image=img1
    panel.configure(image=img1)
    panel.place(x=0, y=0)
    win.mainloop()

root = Tk()
# menu: Game, Options, Help
menuRoot = Menu(root)
gm = Menu(menuRoot)
om = Menu(menuRoot)
hm = Menu(menuRoot)

om.add_command(label="Hand Reference", command=handwindow)
menuRoot.add_cascade(label="Game", menu=gm)
menuRoot.add_cascade(label="About", menu=om)
menuRoot.add_cascade(label="Help", menu=hm)

gm.add_command(label="New Game", command=playAgain)
gm.add_command(label="Exit", command=root.destroy)

root.state('zoomed')
root.title("Texas Hold'em Poker - Windows Edition")

table = Frame(root, width=1400, height=800, background="green")
table.place(x=100, y=10)
t = Label(table, text="Poker: Start a New Game!", font=("Arial", 17), background="green3", width=110, foreground="black").place(x=0, y=0)
board = Frame(table, width=750, height=270, background="lightgreen")
board.place(x=300, y=230)
bot1, bot2, bot3 = Frame(root, width=200, height=200, background="darkcyan"),Frame(root, width=200, height=200, background="darkcyan"),Frame(root, width=200, height=200, background="darkcyan")
bot1.place(x=140, y=400)
bot2.place(x=650, y=40)
bot3.place(x=1200, y=400)
playerspot = Frame(root, width=350, height=300, background="lime")
playerspot.place(x=600, y=500)
e=Entry(playerspot)
e.place(x=50, y=30)

m1 = Label(playerspot, text="Money: $100", font=("Arial", 16), background="gold")
n1 = Label(playerspot, text="YOU", font=("Arial", 16), background="olive")
m1.place(x=100, y=0)
n1.place(x=50, y=0)


m2 = Label(bot1, text="Money: $100", font=("Arial", 16), background="gold")
n2 = Label(bot1, text="Billy", font=("Arial", 16), background="blue")
m2.place(x=0, y=0)
n2.place(x=0, y=30)


m3 = Label(bot2, text="Money: $100", font=("Arial", 16), background="gold")
n3 = Label(bot2, text="Bobby", font=("Arial", 16), background="blue")
m3.place(x=0, y=0)
n3.place(x=0, y=30)


m4 = Label(bot3, text="Money: $100", font=("Arial", 16), background="gold")
n4 = Label(bot3, text="Barry", font=("Arial", 16), background="blue")
m4.place(x=0, y=0)
n4.place(x=0, y=30)


Button(playerspot, text="Bet", command=hubet).place(x=180, y=30)
Button(playerspot, text="Raise", width=5, command=raiseEveryone).place(x=210, y=30)
Button(playerspot, text="Call", width=5).place(x=250, y=30)
Button(playerspot, text="Fold", width=5, command=fold).place(x=290, y=30)




root.configure(menu=menuRoot)
game = Game(board, [m1, m2, m3, m4])


root.mainloop()


