import pygame
import pickle
from network import Network
pygame.font.init()

width = 800
height = 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")

class Button:
    def __init__(self, text, color, x, y):
        self.width = 200
        self.height = 200
        self.text = text
        self.color = color
        self.x = x
        self.y = y
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 50)
        text = font.render(self.text, 1, (255,255,255))
        win. blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

def reDraw(win, game, p):
    win.fill((128,128,128))

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player 2...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Its Your Move", 1, (0, 255,255))
        win.blit(text, (80, 200))

        text = font.render("Opponents Move", 1, (0, 255, 255))
        win.blit(text, (380, 200))

        move1 = game.getPlayerMoves(0)
        move2 = game.getPlayerMoves(1)
        if game.bothWent():
            text1 = font.render(move1, 1, (0,0,0))
            text2 = font.render(move2, 1, (0, 0, 0))
        else:
            if game.p1Move and p == 0:
                text1 = font.render(move1, 1, (0,0,0))
            elif game.p1Move:
                text1 = font.render("Move over", 1, (0, 0, 0))
            else:
                text1 = font.render("Waiting for move...", 1, (0, 0, 0))

            if game.p2Move and p == 1:
                text2 = font.render(move2, 1, (0,0,0))
            elif game.p2Move:
                text2 = font.render("Move over", 1, (0, 0, 0))
            else:
                text2 = font.render("Waiting for move...", 1, (0, 0, 0))
        if p == 1:
            win.blit(text2, (100, 400))
            win.blit(text1, (400, 400))
        else:
            win.blit(text1, (100, 400))
            win.blit(text2, (400, 400))

        for btn in btns:
            btn.draw(win)

    pygame.display.update()

btns = [Button("Rock", 50, 500, (0,0,0)), Button("Scissors", 250, 500, (255,0,0)), Button("Paper", 450, 500, (0,255,0))]


def main():
    clock = pygame.time.Clock()
    run = True
    n = Network()
    player = int(n.getP())
    print("You are player", player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Can not find game")
            break
        
        if game.bothWent():
            reDraw(win, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Can not find game")
                break

            font = pygame.font.SysFont("comicsans", 90)
            if (game.win() == 1 and player == 1) or (game.win() == 0 and player == 0):
                text = font.render("You win!", 1, (255,0,0))
            elif game.win() == -1:
                text = font.render("Game was a tie.", 1, (255,0,0))
            else:
                text = font.render("You lost...", 1, (255,0,0))

            win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1Move:
                                n.send(btn.text)
                        else:
                            if not game.p2Move:
                                n.send(btn.text)

        reDraw(win, game, player)


        
        
        #time delay
        #quit
        #menu screen


