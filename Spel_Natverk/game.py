from sympy import false


class Game:
    def __init__(self, id):
        self.p1Move = False
        self.p2Move = False
        self.ready = False
        self.id = id
        self.move = [None, None]
        self.playerWins = [0,0]
        self.tied = 0

    def getPlayerMoves(self, p):
        return self.move[p]

    def play(self, player, move):
        self.move[player] = move
        if player == 0:
            self.p1Move = True
        else:
            self.p2Move = True

    def connected(self):
        return self.p1Move and self.p2Move

    def bothWent(self):
        return self.p1Move and self.p2Move

    def win(self):
        player1 = self.move[0].upper()[0]
        player2 = self.move[1].upper()[0]

        winner = -1
        if player1 == "R" and player2 == "S":
            winner = 0
        elif player1 == "R" and player2 == "P":
            winner = 1
        elif player1 == "S" and player2 == "R":
            winner = 1
        elif player1 == "S" and player2 == "P":
            winner = 0
        elif player1 == "P" and player2 == "R":
            winner = 0
        elif player1 == "P" and player2 == "S":
            winner = 1

        return winner
    
    def resetMove(self):
        self.p1Move = False
        self.p2Move = False