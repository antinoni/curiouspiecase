import random
import os
# import keyboard
import pygame


########################################### SETUP STUFF ###########################################
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")

WIDTH = 800
HEIGHT = 600
FPS = 30

i = 0

########################################### PLAYER CLASS ###########################################


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # animation
        self.left = [pygame.image.load(
            os.path.join(img_folder, "ml1.png")), pygame.image.load(
            os.path.join(img_folder, "ml2.png")), pygame.image.load(
            os.path.join(img_folder, "ml3.png"))]
        self.right = [pygame.image.load(
            os.path.join(img_folder, "mr1.png")), pygame.image.load(
            os.path.join(img_folder, "mr2.png")), pygame.image.load(
            os.path.join(img_folder, "mr3.png"))]
        self.up = [pygame.image.load(
            os.path.join(img_folder, "mb1.png")), pygame.image.load(
            os.path.join(img_folder, "mb2.png")), pygame.image.load(
            os.path.join(img_folder, "mb3.png"))]
        self.down = [pygame.image.load(
            os.path.join(img_folder, "mf1.png")), pygame.image.load(
            os.path.join(img_folder, "mf2.png")), pygame.image.load(
            os.path.join(img_folder, "mf3.png"))]
        self.curr_sprite = 0
        self.image = self.down[self.curr_sprite]

        # movement
        self.rect = self.image.get_rect()
        self.rect.center = (420, 2*HEIGHT/3)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and self.rect.left > 170:
            if self.rect.top < 400:
                self.speedx = -5
                self.curr_sprite += 0.4
                if self.curr_sprite > 2:
                    self.curr_sprite = 0
                self.image = self.left[int(self.curr_sprite)]
        if keystate[pygame.K_RIGHT] and self.rect.right < 720:
            self.speedx = 5
            self.curr_sprite += 0.4
            if self.curr_sprite > 2:
                self.curr_sprite = 0
            self.image = self.right[int(self.curr_sprite)]
        if keystate[pygame.K_UP] and self.rect.top > 200:
            self.speedy = -5
            self.curr_sprite += 0.4
            if self.curr_sprite > 2:
                self.curr_sprite = 0
            self.image = self.up[int(self.curr_sprite)]
        if keystate[pygame.K_DOWN] and self.rect.bottom < 450:
            self.speedy = 5
            self.curr_sprite += 0.4
            if self.curr_sprite > 2:
                self.curr_sprite = 0
            self.image = self.down[int(self.curr_sprite)]
        self.rect.x += self.speedx
        self.rect.y += self.speedy

########################################## SUSPECTS CLASS #########################################


class Suspects(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.names = ['Rose', 'Mona', 'Rian', 'Mark', 'Emma', 'Erik']
        self.culprit = random.choice(self.names)

########################################## OBJECTS CLASSES #########################################


class Couch(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "couch1.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (295, 490)


class Couch2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "couch2.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (307, 391)

########################################## MINIGAMES #########################################


def folder():
    folder = pygame.image.load(
        os.path.join(img_folder, "folder.png"))
    screen.blit(folder, (20, 20))


def hidden_object():
    if suspects.culprit == suspects.names[0] or suspects.culprit == suspects.names[1]:
        couchgame = pygame.image.load(
            os.path.join(img_folder, "couchpink.png"))
    elif suspects.culprit == suspects.names[2] or suspects.culprit == suspects.names[4]:
        couchgame = pygame.image.load(
            os.path.join(img_folder, "couchblue.png"))
    elif suspects.culprit == suspects.names[3] or suspects.culprit == suspects.names[5]:
        couchgame = pygame.image.load(
            os.path.join(img_folder, "couchgreen.png"))

    screen.blit(couchgame, (100, 100))


def differences():
    if suspects.culprit == suspects.names[0] or suspects.culprit == suspects.names[5]:
        game = pygame.image.load(
            os.path.join(img_folder, "white.png"))
    elif suspects.culprit == suspects.names[3] or suspects.culprit == suspects.names[4]:
        game = pygame.image.load(
            os.path.join(img_folder, "brown.png"))
    elif suspects.culprit == suspects.names[2] or suspects.culprit == suspects.names[1]:
        game = pygame.image.load(
            os.path.join(img_folder, "ginger.png"))

    screen.blit(game, (10, 10))

### RIDDLE ###


def riddlegame():
    book = pygame.image.load(os.path.join(img_folder, "bookpage.png"))
    screen.blit(book, (WIDTH/2 - 102, HEIGHT/4))
    if suspects.culprit == 'Rian' or suspects.culprit == 'Rose':
        riddle = ["What is seen in the", "middle of March and",
                  "April that can’t be", "    seen at the     ", "beginning or end of", "   either month?   "]
    elif suspects.culprit == 'Mona' or suspects.culprit == 'Mark':
        riddle = ["What appears once", "in a minute, twice",
                  "in a moment, but", "never in a thousand", "years?", ""]
    elif suspects.culprit == 'Emma' or suspects.culprit == 'Erik':
        riddle = [
            "I am the beginning ", "of eternity,the end", "of time and space.", "The beginning of", "every end, and the", "end of every place."]
    posy = HEIGHT/4 + 30
    for i in range(6):
        riddlesurface = myfont.render(
            riddle[i], False, (65, 10, 10))
        screen.blit(riddlesurface, (WIDTH/2 - 85, posy))
        posy += 20

########################################### CHOOSE THIEF ###########################################


def findsus():
    myfont = pygame.font.SysFont('Courier New', 35)
    bg = pygame.Surface((600, 400))
    bg.fill((0, 0, 0))
    screen.blit(bg, (100, 100))
    names = ['ROSE [1]', 'MONA [2]', 'RIAN [3]',
             'MARK [4]', 'EMMA [5]', 'ERIK [6]']
    i = 0
    for i in range(6):
        namesurface = myfont.render(
            names[i], False, (255, 255, 255))
        if i == 0:
            screen.blit(namesurface, (140, 140))
        elif i == 1:
            screen.blit(namesurface, (470, 140))
        elif i == 2:
            screen.blit(namesurface, (140, 200))
        elif i == 3:
            screen.blit(namesurface, (470, 200))
        elif i == 4:
            screen.blit(namesurface, (140, 260))
        elif i == 5:
            screen.blit(namesurface, (470, 260))
    myfont = pygame.font.SysFont('Courier New', 20)
    msg = 'Hold the number of the person you want to accuse.'
    mesgsurface = myfont.render(msg, False, (255, 255, 255))
    screen.blit(mesgsurface, (110, 400))

########################################### WIN/LOSE GAME ###########################################


def win():
    myfont = pygame.font.SysFont('Courier New', 35)
    bg = pygame.Surface((600, 400))
    bg.fill((0, 0, 0))
    screen.blit(bg, (100, 100))
    msg1 = 'YOU WON!'
    msg1surface = myfont.render(msg1, False, (255, 255, 255))
    screen.blit(msg1surface, (140, 140))
    myfont = pygame.font.SysFont('Courier New', 25)
    msg2 = 'You can now exit the game and'
    msg3 = 'restart it for a new culprit!'
    msg2surface = myfont.render(msg2, False, (255, 255, 255))
    screen.blit(msg2surface, (140, 340))
    msg3surface = myfont.render(msg3, False, (255, 255, 255))
    screen.blit(msg3surface, (140, 370))


def lose():
    myfont = pygame.font.SysFont('Courier New', 35)
    bg = pygame.Surface((600, 400))
    bg.fill((0, 0, 0))
    screen.blit(bg, (100, 100))
    msg1 = 'YOU LOST :('
    msg1surface = myfont.render(msg1, False, (255, 255, 255))
    screen.blit(msg1surface, (140, 140))
    myfont = pygame.font.SysFont('Courier New', 25)
    msg2 = 'Try to check the clues again - '
    msg3 = 'use hints if you want to!'
    msg2surface = myfont.render(msg2, False, (255, 255, 255))
    screen.blit(msg2surface, (140, 340))
    msg3surface = myfont.render(msg3, False, (255, 255, 255))
    screen.blit(msg3surface, (140, 370))


########################################### INITIALISE GAME ###########################################
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Curious Case of the Missing Pie")
icon = pygame.image.load(os.path.join(img_folder, "magnifying-glass.png"))
pygame.display.set_icon(icon)
bg = pygame.image.load(os.path.join(img_folder, "room.png"))
clock = pygame.time.Clock()

pygame.font.init()
myfont = pygame.font.SysFont('Courier New', 15)


########################################### SPRITES ###########################################
all_sprites = pygame.sprite.Group()
objects = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
couch = Couch()
couch2 = Couch2()
all_sprites.add(couch)
all_sprites.add(couch2)
objects.add(couch)
suspects = Suspects()

########################################### GAME LOOP ###########################################
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)

    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update

    all_sprites.update()

    ########################################### BOTTOM MESSAGE ###########################################

    keystate = pygame.key.get_pressed()
    if player.rect.right > 700 and player.rect.top > 220 and player.rect.top < 300:
        text = 'That room is irrelevant. All the action was here.'
    elif player.rect.top > 205 and player.rect.right < 475:
        text = 'The couch... I see some crumbs here.'
        if keystate[pygame.K_SPACE]:
            text = 'I see the thieft left something behind.'
        if keystate[pygame.K_h]:
            text = 'HINT: Which of these items has something in common with some of our suspects?'
    elif player.rect.right < 700 and player.rect.right > 510 and player.rect.top < 200:
        text = 'I don\'t think I should leave an active crime scene.'
    elif player.rect.right > 700 and player.rect.top < 270:
        text = 'I will call the family to give them the thief\'s name when I am ready. Ready? [Hold Y]'
    elif player.rect.right < 300 and player.rect.right > 240 and player.rect.top < 200:
        text = 'This is my case folder, containing all the suspects\' information.'
    elif player.rect.bottom > 420 and player.rect.right > 655:
        text = 'Hmmm... there are two photographs of the pie here.'
        if keystate[pygame.K_h]:
            text = 'HINT: Do you notice any differences between the two photos?'
    elif player.rect.right < 420 and player.rect.right > 340 and player.rect.top < 200:
        text = 'An open book... A note written in it... And a stain from what looks like cherry jam.'
        if keystate[pygame.K_SPACE]:
            text = 'The answer to the riddle will help me find the culprit.'
        if keystate[pygame.K_h]:
            text = 'HINT: Look closely at the given words. Do you notice anything?'
    else:
        text = 'Use ARROWS to move, hold SPACE to interact with objects. Hold \'H\' for a hint.'
    textsurface = myfont.render(text, False, (255, 255, 255))
    text_width, text_height = myfont.size(text)

    ########################################### DRAW ###########################################
    screen.blit(bg, (0, 0))
    screen.blit(textsurface, (WIDTH/2 - text_width /
                              2, HEIGHT - text_height - 30))

    all_sprites.draw(screen)

    if player.rect.top > 205 and player.rect.right < 475:
        if keystate[pygame.K_SPACE] or keystate[pygame.K_h]:
            hidden_object()
    if player.rect.bottom > 420 and player.rect.right > 655:
        if keystate[pygame.K_SPACE] or keystate[pygame.K_h]:
            differences()
    elif player.rect.right < 420 and player.rect.right > 340 and player.rect.top < 200:
        if keystate[pygame.K_SPACE] or keystate[pygame.K_h]:
            riddlegame()
    elif player.rect.right < 300 and player.rect.right > 240 and player.rect.top < 200:
        if keystate[pygame.K_SPACE]:
            folder()
    elif player.rect.right > 700 and player.rect.top < 270:
        if keystate[pygame.K_y]:
            findsus()
        if keystate[pygame.K_1]:
            if suspects.culprit == suspects.names[0]:
                win()
            else:
                lose()
        elif keystate[pygame.K_2]:
            if suspects.culprit == suspects.names[1]:
                win()
            else:
                lose()
        elif keystate[pygame.K_3]:
            if suspects.culprit == suspects.names[2]:
                win()
            else:
                lose()
        elif keystate[pygame.K_4]:
            if suspects.culprit == suspects.names[3]:
                win()
            else:
                lose()
        elif keystate[pygame.K_5]:
            if suspects.culprit == suspects.names[4]:
                win()
            else:
                lose()
        elif keystate[pygame.K_6]:
            if suspects.culprit == suspects.names[5]:
                win()
            else:
                lose()

    pygame.display.update()

pygame.quit()
