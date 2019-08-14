from test import Tester
from player import Player

class Board(object):
    def __init__(self, players, nameP, turn, end):
        self.players = players
        self.nameP = nameP
        self.turn = turn
        self.end = end
    
if __name__ == "__main__":
    player1 = Player("", "")
    player2 = Player("", "")
    player1.name = input("Ingrese nombre de Jugador1 ")
    player2.name = input("Ingrese nombre de Jugador2 ")
    tester1 = Tester("Dark", "Flawrous", 620, 234, 142)
    tester2 = Tester("Mage", "Siren", 700, 254, 102)
    player1.usIa = tester1
    player2.usIa = tester2
    while((player1.usIa.hp > 0) and (player2.usIa.hp > 0)):
        print("Start\n A = Attak")
        
        