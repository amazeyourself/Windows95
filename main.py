import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
run = True

err_img = pygame.image.load("./assets/err.png").convert()

x = 0
y = 0

while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_LEFT]:
    x -= 1
  if pressed[pygame.K_RIGHT]:
    x += 1
  if pressed[pygame.K_UP]:
    y -= 1
  if pressed[pygame.K_DOWN]:
    y += 1

  screen.fill("#018382")
  screen.blit(err_img, (x,y))
  clock.tick(60)
  pygame.display.flip()

pygame.quit()