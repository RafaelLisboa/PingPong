import pygame as pg
import random as rd


class Player(object):

    def __init__(self, pos_x, pos_y, up, down):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.fill = 10
        self.size = 100
        self.up = up
        self.down = down

    def move(self, event):

        try:
            if event.type == pg.KEYDOWN:
        
                if event.key is self.up and (self.pos_y + 5 > 0):
                    self.pos_y -= 25

                if event.key is self.down and (self.pos_y < 410):
                    self.pos_y += 25
        except:
            pass

    def position(self):
        return self.pos_x, self.pos_y, self.fill, self.size

class Bot(Player):

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.fill = 10
        self.size = 100
        self.b_y = 0
    
    def move(self, ball_position):
        try:
            self.b_x = ball_position[0]
            self.b_y = ball_position[1]
            if self.b_y > self.pos_y + 50 and self.b_x > 500:
                self.pos_y += 10
            elif self.b_y < self.pos_y and self.b_x > 500:
                self.pos_y -= 10
        except:
            pass    

class Game(object):

    def __init__(self, player):

        self.player1 = player[0]
        self.player2 = player[1]
        self.width = 900
        self.height = 500
        self.size = (self.width, self.height)
        self.screen = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.player1_score = self.player2_score = 0
        pg.display.set_caption('Ping Pong')
        end = False
        pg.font.init()
        self.font = pg.font.get_default_font()
        self.sys_font = pg.font.SysFont(self.font, 45)

        #Ball
        self.ball = pg.Rect(457, 257, 20, 20 )
        self.ball0 = [self.ball.x, self.ball.y]
        self.init_ball = rd.choice ([2, -2])
        self.b_velx = self.init_ball+self.init_ball
        self.b_vely = self.init_ball

        while not end:
            self.paddle1 = pg.Rect(self.player1.position())
            self.paddle2 = pg.Rect(self.player2.position())
            self.players = [self.paddle1, self.paddle2]

            if self.ball.y >= self.height - 20 or self.ball.y < 0:
                self.b_vely *= -1
                if self.b_vely < 0:
                    self.b_vely -= 0.5
                    self.b_velx -= 0.5
                else:
                    self.b_vely += 0.5
                    self.b_velx += 0.5

            #Ball to initial stats
            if self.ball.x >= self.width - 20 or self.ball.x < -20:
                if self.ball.x >= self.width - 20:
                    self.player1_score += 1

                elif self.ball.x < self.width - 20:
                    self.player2_score += 1
                    
                self.ball.x = self.ball0[0]
                self.ball.y = self.ball0[1]
                self.init_ball = rd.choice ([2, -2])
                self.b_velx = self.init_ball
                self.b_vely = self.init_ball

            if self.ball.colliderect(self.paddle1) or self.ball.colliderect(self.paddle2):
                self.b_velx *= -1.10

            self.ball.x += round(self.b_velx)
            self.ball.y += round(self.b_vely)
            

            self.score_txt = self.sys_font.render(f'{self.player1_score}    {self.player2_score}', False, self.WHITE)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    end = True
                self.player2.move(event)
                self.player1.move(event)
            self.player2.move([self.ball.x, self.ball.y])
            #Elements
            self.screen.fill(self.BLACK)
            for paddle in self.players:
                pg.draw.rect(self.screen,self.WHITE,paddle)
            pg.draw.ellipse(self.screen, self.WHITE, self.ball)
            pg.draw.aaline(self.screen, self.WHITE, (self.width/2, 0), (self.width/2, self.height))
            self.screen.blit(self.score_txt, (422, 10))
            pg.display.flip()
            pg.display.update()
            self.clock.tick(60)

bot = Bot(855, 200)
player1 = Player(885, 200, pg.K_i, pg.K_k)
player2 = Player(0, 200, pg.K_w, pg.K_s)

print('-'*45)
print('\n\nPlayer 1 UP = w/ Down = s\nPlayer 2 UP = i/ Down = k\n ')
selection = int(input('[1] == Player vs Computer\n' +
                  '[2] == Player 1 vs Player 2\n'
                   '>>: '  ))

if selection == 1:
    players = [player2, bot]
    game = Game(players)
if selection == 2:
    players = [player2 , player1]
    game = Game(players)
