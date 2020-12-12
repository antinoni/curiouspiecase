# import random
import os
# import keyboard
import pygame


########################################### SETUP STUFF ###########################################
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")

WIDTH = 800
HEIGHT = 600
FPS = 30
transparent = (0, 0, 0, 0)

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
        self.image.set_colorkey((0, 0, 0))

        # movement
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, 2*HEIGHT/3)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and self.rect.left > 50:
            for item in objects:
                if self.rect.left - item.rect.right >= 0:
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
        if keystate[pygame.K_UP] and self.rect.top > 370:
            self.speedy = -5
            self.curr_sprite += 0.4
            if self.curr_sprite > 2:
                self.curr_sprite = 0
            self.image = self.up[int(self.curr_sprite)]
        if keystate[pygame.K_DOWN] and self.rect.bottom < 510:
            self.speedy = 5
            self.curr_sprite += 0.4
            if self.curr_sprite > 2:
                self.curr_sprite = 0
            self.image = self.down[int(self.curr_sprite)]
        self.rect.x += self.speedx
        self.rect.y += self.speedy

########################################## OBJECTS CLASSES #########################################


class Couch(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "couches.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/5, 2*HEIGHT/3)

    def shooter(self):
        shooterbg = pygame.Surface((300, 100))
        shooterbg.fill((55, 155, 255))
        screen.blit(shooterbg, (WIDTH/2-WIDTH/6 - 10, HEIGHT/3))


def riddlegame():
    # self.image = pygame.image.load(os.path.join(img_folder, "bookpage.png"))
    shooterbg = pygame.Surface((200, 300))
    shooterbg.fill((255, 255, 255))
    screen.blit(shooterbg, (WIDTH/2 - 100, HEIGHT/4))
    riddle = ["What is seen in the", "middle of March and",
              "April that can’t be", "    seen at the     ", "beginning or end of", "   either month?   "]
    posy = HEIGHT/4 + 30
    for i in range(6):
        riddlesurface = myfont.render(
            riddle[i], False, (10, 10, 10))
        screen.blit(riddlesurface, (WIDTH/2 - 85, posy))
        posy += 20


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
all_sprites.add(couch)
objects.add(couch)


########################################### GAME LOOP ###########################################
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)

    key_pressed = False
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                key_pressed = True
            if event.key == pygame.K_ESCAPE:
                key_pressed = False

    # Update
    all_sprites.update()

    touch = pygame.sprite.spritecollide(player, objects, False)

    ########################################### BOTTOM MESSAGE ###########################################

    if player.rect.left - couch.rect.right <= 3:
        text = 'The couch... I see some crumbs here.'
    elif player.rect.right < 700 and player.rect.right > 510 and player.rect.top < 375:
        text = 'I don\'t think I should leave an active crime scene.'
    elif player.rect.right > 700 and player.rect.top > 390 and player.rect.top < 470:
        text = 'That room is irrelevant. All the action is here.'
    elif player.rect.right < 390 and player.rect.right > 310 and player.rect.top < 375:
        text = 'An open book... A note written in it... And a stain from what looks like cherry jam.'
    else:
        text = 'Use ARROWS to move, SPACE to interact with objects'
    textsurface = myfont.render(
        text, False, (255, 255, 255))
    text_width, text_height = myfont.size(text)

    ########################################### DRAW ###########################################
    screen.blit(bg, (0, 0))
    screen.blit(textsurface, (WIDTH/2 - text_width /
                              2, HEIGHT - text_height - 30))

    all_sprites.draw(screen)

    # if keyboard.is_pressed('Space'):
    if player.rect.left - couch.rect.right <= 3:
        couch.shooter()
    elif player.rect.right < 390 and player.rect.right > 310 and player.rect.top < 375:
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            riddlegame()

    pygame.display.update()

pygame.quit()
