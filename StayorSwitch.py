#Stay or Switch game

import random

class StayorSwitch:

    def __init__(self):

        self.cards = Cards()
        self.UI = UserInterface()
        self.stats = Stats()

    def playGame(self):
        
        self.UI.printIntro()
        pick = self.cards.cardPick()
        X = self.UI.inputStrategy()
    
        for char in X:
            
            pick = self.cards.cardPick()
            if char == 'S':
                self.cards.cardList.remove("Lose")
                
                
            
            elif char == 'W':
                self.cards.cardList.remove("Lose")
                if pick == "Win":
                    pick = "Lose"
                    
            
                else:
                    pick = "Win"
                    
                    
            
            if pick == "Win":
                self.stats.win += 1
            elif pick == "Lose":
                self.stats.loss += 1
            self.stats.gamesPlayed += 1
            self.cards.cardList.append("Lose")
            

        
        self.UI.displayStats(self.stats.gamesPlayed,  self.stats.win,self.stats.loss, )


class UserInterface:

    def printIntro(self):
        print("""There are 3 cards, 1 winning card and 2 losing cards. The
game simulates a pick and the dealer reveals a losing card and gives you the 
option to switch your card. S is stay, W is switch. Enter your strategy across multiple games. Ex: SSSSSWWSWSWS""")

    def inputStrategy(self):
        switchCard = input("Enter your strategy: ")
        switchCard = switchCard.upper()

        return switchCard
          

    def displayStats(self,gamesplayed,win,lose):
        print ("Games played:",gamesplayed)
        print ("Games won/loss:", win, lose)
        print ("Win Percentage: ",win/gamesplayed *100,"%")
        

class Cards:

    def __init__(self):
        self.cardA = "Win"
        self.cardB = "Lose"
        self.cardC = "Lose"
        self.cardList = [self.cardA, self.cardB, self.cardC]
    def shuffleCards(self):
        
        cardList = random.shuffle(self.cardList)

        return cardList

    def cardPick(self):
        pick = random.choice(self.cardList)

        return pick

    def __str__(self):
        return str(self.cardList)
    
    
class Stats:

    def __init__(self):
        self.win = 0
        self.loss = 0
        self.gamesPlayed = 0

    def gamesPlayed(self):
        return self.gamesPlayed

    def winLoss(self):
        return ("Wins: ",self.win, "Losses: ", self.loss)
        return ("Win Percentage: ", self.win/self.loss *100,"%")


def main():
    game = StayorSwitch()
    game.playGame()

main()
