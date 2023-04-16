import pygame
import math

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Hedef Vurma Oyunu")

# oyun alanı
floor = pygame.Surface((width, height / 2))
floor.fill((50, 50, 50))

# hedef
target_color = (255, 0, 0)
target_radius = 50
target_pos = (width / 2, height / 4)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # fare tıklaması algıla
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            distance = math.sqrt((mouse_pos[0] - target_pos[0]) ** 2 + (mouse_pos[1] - target_pos[1]) ** 2)

            # hedefi vur
            if distance < target_radius:
                print("Hedef vuruldu!")

    # oyun alanını çiz
    screen.blit(floor, (0, height / 2))

   
