#plans for game
#  1. up/down movement??
#  2. mouse tracking
#  3. speed of movement changes

#homeowrk 2/20/24
#find heart empyt / full image
#find laser image
#find asetroid images
    #small asteroid
    #big damage asteroid
#finc background image

#MAYBE work on class defining




import pygame
import random
import time


pygame.init()
clock = pygame.time.Clock()
count = 0
screen_width = 500
screen_height = 750
isshot = False
time_ = 0

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooter")

black = (0, 0, 0)
gray = (50, 50, 50)


rocket = pygame.transform.rotate(pygame.image.load(r"C:\Users\talun\Downloads\rocket.png"), -45)
asteroid1 = pygame.image.load(r"C:\Users\talun\Downloads\asteroid1.png")
asteroid2 = pygame.transform.rotate(pygame.image.load(r"C:\Users\talun\Downloads\asteroid2.png"), 50)
laser = pygame.transform.rotate(pygame.image.load(r"C:\Users\talun\Downloads\laser.jpg"), 90)
background = pygame.image.load(r"C:\Users\talun\Downloads\space.jpg").convert()
background = pygame.transform.smoothscale(background, screen.get_size())
heart = pygame.transform.rotate(pygame.image.load(r"C:\Users\talun\Downloads\life.png"), 360)
#pygame.image.load(r"C:\Users\talun\Downloads\space.jpg")
screen.fill(black)


font_name = pygame.font.match_font('comic sans ms')
class Text():
    def __init__(self, surface, text, size, color, x, y):
        font_name = pygame.font.match_font('arial')
        self.surface = surface
        self.text = text
        self.size = size
        self.font = pygame.font.Font(font_name, self.size)
        self.color = color
        self.x = x
        self.y = y
    def draw(self):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (self.x, self.y)
        self.surface.blit(text_surface, text_rect)

#def draw_text(surf, text, size, x, y):
#  font = pygame.font.Font(font_name, size)
#  text_surface = font.render (text, True, black)
#  text_rect = text_surface.get_rect()
#  text_rect.midtop = (x, y)
#  surf.blit(text_surface, text_rect)
        
#game loop 
  
class Asteroid(pygame.sprite.Sprite):
  def __init__(self, image, scale, x, y, lives):
    pygame.sprite.Sprite.__init__(self)
    width = image.get_width()  
    height = image.get_height()
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.lives = lives
    self.rect.center = (x, y)
  def fall(self, speed):
    self.rect.y += speed

class life(pygame.sprite.Sprite):
  def __init__(self, image, scale, x, y):
    pygame.sprite.Sprite.__init__(self)
    width = image.get_width()  
    height = image.get_height()
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
  def fall(self, speed):
    self.rect.y += speed

movement = 0
class Player(pygame.sprite.Sprite):
  
  def __init__(self, image, scale, x, y):
    pygame.sprite.Sprite.__init__(self)
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(image, (int(width*scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    
  def update(self):
    global movement
    #if keystate[pygame.K_w]:
    #  self.rect.y -= 2.5
    #if keystate[pygame.K_s]:
    #  self.rect.y += 2.5
    if self.rect.x < -50 or self.rect.x > 375:
      movement = 0 - movement
    if self.rect.x < -50:
      self.rect.x += 1
    if self.rect.x > 375:
      self.rect.x -= 1
    if keystate[pygame.K_d]:
      movement += 0.25
    if keystate[pygame.K_a]:
      movement -= 0.25
    elif movement < 0:
      movement += 0.1
    elif movement > 0:
      movement -= 0.1
    self.rect.x += movement
    
    if keystate[pygame.K_SPACE]:
      global isshot
      isshot = True


class lasers(pygame.sprite.Sprite):
  def __init__(self, image, scale, x, y):
    pygame.sprite.Sprite.__init__(self)
    width = image.get_width()  
    height = image.get_height()
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
  def shot(self):
    self.rect.y -= 4
    


player = Player(rocket, 0.05, 150, 650)
#laser1 = lasers(laser, 0.25, 150, 150)

Asteroid1 = Asteroid(asteroid1, 0.25, random.randint(25, 475), -50, 2)
Asteroid2 = Asteroid(asteroid2, 0.25, random.randint(25, 475), -50, 3)

lifedrop = life(heart, 0.15, random.randint(25, 475), -50)

player_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()
lives_group = pygame.sprite.Group()
Asteroid1_group = pygame.sprite.Group()
Asteroid2_group = pygame.sprite.Group()

player_group.add(player)
lives_group.add(lifedrop)
Asteroid1_group.add(Asteroid1)
Asteroid2_group.add(Asteroid2)


lives = 3
speed = 1
spawnrate1 = 200
spawnrate2 = 750
laserrate = 25

while True:
  

  screen.blit(background, (0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()

  keystate = pygame.key.get_pressed()

  if pygame.sprite.spritecollide(player, Asteroid1_group, True):
    lives -= 1
  if pygame.sprite.spritecollide(player, Asteroid2_group, True):
    lives -= 2
  if pygame.sprite.spritecollide(player, lives_group, True):
    lives += 1

  collision1 = pygame.sprite.groupcollide(laser_group, Asteroid1_group, True, False)
  collision2 = pygame.sprite.groupcollide(laser_group, Asteroid2_group, True, False)
  
  for asteroidlifelist in collision1.values():
    if len(asteroidlifelist) > 0:
      asteroid_ = asteroidlifelist[0]
      asteroid_.lives -= 1
      if asteroid_.lives <= 0:
        asteroid_.kill()

  for asteroidlifelist in collision2.values():
    if len(asteroidlifelist) > 0:
      asteroid_ = asteroidlifelist[0]
      asteroid_.lives -= 1
      if asteroid_.lives <= 0:
        asteroid_.kill()
        




  clock.tick(60)
  time_ = int(pygame.time.get_ticks()/1000-2)
  if speed < 10:
    speed += 0.001
  
  if spawnrate1 > 75:
    spawnrate1 -= 0.05
  if random.randint(0, int(spawnrate1)) == 22:
    Asteroid1_group.add(Asteroid(asteroid1, 0.25, random.randint(25, 475), -50, 3))

  if spawnrate2 > 200:
    spawnrate2 -= 0.0005
  if random.randint(0, int(spawnrate2)) == 22:
    Asteroid2_group.add(Asteroid(asteroid2, 0.25, random.randint(25, 475), -50, 3))
  if random.randint(0, int(spawnrate2)) == 23:
    lives_group.add(life(heart, 0.15, random.randint(25, 475), -50))
  
  for i in Asteroid1_group:
    i.fall(speed)
  for i in Asteroid2_group:
    i.fall(speed)
  for i in lives_group:
    i.fall(speed)


  laserrate -= 1
  

  if lives <= 0:
    died = True
    #endscore = time
    
    screen.fill([25, 25, 25])
    #time = endscore
    game_text.draw()
    pygame.display.update()
    time.sleep(3)
    pygame.quit()

  if laserrate <= 0:
    if isshot == True:
      laser_group.add(lasers(laser, 0.005, player.rect.x+83, player.rect.y+5))
      isshot = False
      #print("shooting")
      laserrate = 25
  for i in laser_group:
    i.shot()







  game_text = Text(screen, "Score: " + str(time_), 25, (255, 255, 255), 75, 15)
  lives_text = Text(screen, "Lives: " + str(lives), 25, (255, 255, 255), 200, 15)

  
  game_text.draw()
  lives_text.draw()
  lives_group.draw(screen)
  Asteroid1_group.draw(screen)
  Asteroid2_group.draw(screen)
  laser_group.draw(screen)
  player_group.draw(screen)
  lives_group.update()
  Asteroid1_group.update()
  Asteroid2_group.update()
  laser_group.update()
  player_group.update()
  pygame.display.update()