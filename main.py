import pygame
import os
pygame.init()
pygame.display.set_caption("Paraplegic simulator")


FPS = 60
SPEED = 5


HEIGHT, WIDTH = 1280, 720
screen = pygame.display.set_mode((HEIGHT, WIDTH))


MAP_IMAGE = pygame.image.load(os.path.join("Assets", "map.png"))
MAP = pygame.transform.scale(MAP_IMAGE, (HEIGHT, WIDTH))


MC_HEIGHT, MC_WIDTH = 100, 150
MC_FRONT_IMAGE = pygame.image.load(os.path.join("Assets", "mc front.png"))
MC_FRONT = pygame.transform.scale(MC_FRONT_IMAGE, (MC_HEIGHT-20, MC_WIDTH-60))

MC_BACK_IMAGE = pygame.image.load(os.path.join("Assets", "mc back.png"))
MC_BACK = pygame.transform.scale(MC_BACK_IMAGE, (MC_HEIGHT, MC_WIDTH))


def screen_printer(mc_facing, mc_player):
    screen.blit(MAP, (0, 0))
    screen.blit(mc_facing, (mc_player.x, mc_player.y))
    pygame.display.update()


def movement(keys_pressed, mc_player, mc_facing):
    if keys_pressed[pygame.K_w] and mc_player.y - 5 > -20:
        mc_player.y -= SPEED
        mc_facing = MC_BACK
    if keys_pressed[pygame.K_s] and mc_player.y + 5 < WIDTH - 50:
        mc_player.y += SPEED
        mc_facing = MC_FRONT
    if keys_pressed[pygame.K_d] and mc_player.x + 5 < HEIGHT - 50:
        mc_player.x += SPEED
        mc_facing = MC_BACK
    if keys_pressed[pygame.K_a] and mc_player.x - 5 > -10:
        mc_player.x -= SPEED
        mc_facing = MC_FRONT
    return mc_facing


def main():
    mc_player = pygame.Rect(450, 100, MC_WIDTH, MC_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    mc_facing = MC_BACK
    while run:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():  # checks for events or something
            if event.type == pygame.QUIT:
                run = False  # quits from the game
        mc_facing = movement(keys_pressed, mc_player, mc_facing)
        screen_printer(mc_facing, mc_player)


if __name__ == '__main__':
    main()
