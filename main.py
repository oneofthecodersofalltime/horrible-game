import pygame
import os

pygame.init()
pygame.font.init()
pygame.display.set_caption("The game of the secret")


font = pygame.font.SysFont("Comic sans", 20)
ho1_talk = font.render('I like monster trucks and firetrucks', True, (0, 0, 0))
ho2_talk = font.render('FACKH OFF BLOKE!', True, (0, 0, 0))
ho3_talk = font.render('Mitäh? Saatana jättäh ruhaan', True, (0, 0, 0))
ho4_talk = font.render('GIVE ME CALCIUM', True, (0, 0, 0))
bookshelf_slander = font.render('You try to read a book, but you cant read.', True, (0, 0, 0))
tv_slander = font.render('Nothing on the TV', True, (0, 0, 0))


FPS = 60
SPEED = 5


HEIGHT, WIDTH = 1280, 720
screen = pygame.display.set_mode((HEIGHT, WIDTH))


MAP_IMAGE = pygame.image.load(os.path.join("Assets", "map.png"))
MAP = pygame.transform.scale(MAP_IMAGE, (HEIGHT, WIDTH))

MAP_NO_GROUND_IMAGE = pygame.image.load(os.path.join("Assets", "mapnoground.png"))
MAP_NO_GROUND = pygame.transform.scale(MAP_NO_GROUND_IMAGE, (HEIGHT, WIDTH))


POND_IMAGE = pygame.image.load(os.path.join("Assets", "pong.png"))
POND = pygame.transform.scale(POND_IMAGE, (HEIGHT, WIDTH))


ICON_SIZE = 80


QUESTION_IMAGE = pygame.image.load(os.path.join("Assets", "thisisno.png"))
QUESTION = pygame.transform.scale(QUESTION_IMAGE, (ICON_SIZE, ICON_SIZE))

CHECK_IMAGE = pygame.image.load(os.path.join("Assets", "no.png"))
CHECK = pygame.transform.scale(CHECK_IMAGE, (ICON_SIZE, ICON_SIZE))

QUESTS_BACKGROUND_IMAGE = pygame.image.load(os.path.join("Assets", "thisiscorkboard.png"))
QUESTS_BACKGROUND = pygame.transform.scale(QUESTS_BACKGROUND_IMAGE, (ICON_SIZE, ICON_SIZE))

INVENTORY_BACKGROUND_IMAGE = pygame.image.load(os.path.join("Assets", "inventorylist.png"))
INVENTORY_BACKGROUND = pygame.transform.scale(INVENTORY_BACKGROUND_IMAGE, (ICON_SIZE, ICON_SIZE*2))

QUESTS_ICON_IMAGE = pygame.image.load(os.path.join("Assets", "corkboard.png"))
QUESTS_ICON = pygame.transform.scale(QUESTS_ICON_IMAGE, (ICON_SIZE, ICON_SIZE))

INVENTORY_ICON_IMAGE = pygame.image.load(os.path.join("Assets", "bag.png"))
INVENTORY_ICON = pygame.transform.scale(INVENTORY_ICON_IMAGE, (ICON_SIZE, ICON_SIZE))


# main character set up
MC_HEIGHT, MC_WIDTH = 100, 150
MC_FRONT_IMAGE = pygame.image.load(os.path.join("Assets", "mc front.png"))
MC_FRONT = pygame.transform.scale(MC_FRONT_IMAGE, (MC_HEIGHT-20, MC_WIDTH-60))

MC_BACK_IMAGE = pygame.image.load(os.path.join("Assets", "mc back.png"))
MC_BACK = pygame.transform.scale(MC_BACK_IMAGE, (MC_HEIGHT, MC_WIDTH))

MC_LEFT_IMAGE = pygame.image.load(os.path.join("Assets", "mc side.png"))
MC_LEFT = pygame.transform.scale(MC_LEFT_IMAGE, (MC_HEIGHT, MC_WIDTH))
MC_LEFT_IMAGE2 = pygame.image.load(os.path.join("Assets", "mc side2.png"))
MC_LEFT2 = pygame.transform.scale(MC_LEFT_IMAGE2, (MC_HEIGHT, MC_WIDTH))

MC_RIGHT_IMAGE = pygame.image.load(os.path.join("Assets", "mc side flipped.png"))
MC_RIGHT = pygame.transform.scale(MC_RIGHT_IMAGE, (MC_HEIGHT, MC_WIDTH))
MC_RIGHT_IMAGE2 = pygame.image.load(os.path.join("Assets", "mc side flipped2.png"))
MC_RIGHT2 = pygame.transform.scale(MC_RIGHT_IMAGE2, (MC_HEIGHT, MC_WIDTH))
# main character set up over


HOUSE_IMAGE = pygame.image.load(os.path.join("Assets", "house.png"))
HOUSE = pygame.transform.scale(HOUSE_IMAGE, (HEIGHT, WIDTH))
# Homeowners coming up
HO1_IMAGE = pygame.image.load(os.path.join("Assets", "HO1.png"))
HO1 = pygame.transform.scale(HO1_IMAGE, (MC_HEIGHT, MC_WIDTH))
HO2_IMAGE = pygame.image.load(os.path.join("Assets", "HO2.png"))
HO2 = pygame.transform.scale(HO2_IMAGE, (MC_HEIGHT, MC_WIDTH))
HO3_IMAGE = pygame.image.load(os.path.join("Assets", "HO3.png"))
HO3 = pygame.transform.scale(HO3_IMAGE, (MC_HEIGHT, MC_WIDTH))
HO4_IMAGE = pygame.image.load(os.path.join("Assets", "HO4.png"))
HO4 = pygame.transform.scale(HO4_IMAGE, (MC_HEIGHT, MC_WIDTH))


def screen_printer(mc_facing, mc_player, house, ho1, ho2, ho3, ho4, keys_pressed, house_door, which_house, house_nw,
                   house_sw, house_se, house_ne, town, bookshelf_interact, bookshelf, tv_interact, tv, ho1_time,
                   ho2_time, ho3_time, ho4_time, roof_door, bag, quests):
    if not house and town:
        current_bg = MAP
        house = False
        if mc_player.colliderect(house_door):
            mc_player.y = 50
            town = False
    elif house:
        current_bg = HOUSE
        town = False
        if mc_player.colliderect(house_door) and keys_pressed[pygame.K_e]:
            house = False
            town = True
            current_bg = MAP
            if which_house == "nw":
                mc_player.x, mc_player.y = house_nw.x, house_nw.y + 200
            if which_house == "sw":
                mc_player.x, mc_player.y = house_sw.x, house_sw.y + 125
            if which_house == "se":
                mc_player.x, mc_player.y = house_se.x, house_se.y + 125
            if which_house == "ne":
                mc_player.x, mc_player.y = house_ne.x, house_ne.y + 125
    else:
        current_bg = POND
        if mc_player.colliderect(roof_door):
            town = True
            mc_player.y = 620

    screen.blit(current_bg, (0, 0))
    if not house and town:
        screen.blit(HO1, (ho1.x, ho1.y))
        screen.blit(HO2, (ho2.x, ho2.y))
        screen.blit(HO3, (ho3.x, ho3.y))
        screen.blit(HO4, (ho4.x, ho4.y))

    screen.blit(mc_facing, (mc_player.x, mc_player.y))
    if town:
        screen.blit(MAP_NO_GROUND, (0, 0))
    for x in range(bookshelf_interact):
        screen.blit(bookshelf_slander, (bookshelf.x, bookshelf.y))
    for x in range(tv_interact):
        screen.blit(tv_slander, (tv.x, tv.y))
    for x in range(ho1_time):
        screen.blit(ho1_talk, (ho1.x, ho1.y-20))
    for x in range(ho2_time):
        screen.blit(ho2_talk, (ho2.x, ho2.y-20))
    for x in range(ho3_time):
        screen.blit(ho3_talk, (ho3.x, ho3.y-20))
    for x in range(ho4_time):
        screen.blit(ho4_talk, (ho4.x, ho4.y-20))
    screen.blit(INVENTORY_ICON, (bag.x, bag.y))
    screen.blit(QUESTS_ICON, (quests.x, quests.y))

    pygame.display.update()
    return house, town


def entering_system(mc_player, house_nw, house_sw, house_se, house_ne, ho1, keys_pressed, ho2, ho3, ho4, town):
    # pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(210, 100, 250, 120))
    ho1_time = 0
    ho2_time = 0
    ho3_time = 0
    ho4_time = 0

    if mc_player.colliderect(house_nw) and keys_pressed[pygame.K_e] and town:
        mc_player.x = HEIGHT/2-20
        mc_player.y = WIDTH-200
        house = 1
        which_house = "nw"
        return house, which_house, ho1_time, ho2_time, ho3_time, ho4_time
    # pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(170, 300, 250, 250))
    if mc_player.colliderect(house_sw) and keys_pressed[pygame.K_e] and town:
        mc_player.x = HEIGHT/2-20
        mc_player.y = WIDTH-200
        house = 1
        which_house = "sw"
        return house, which_house, ho1_time, ho2_time, ho3_time, ho4_time
    if mc_player.colliderect(house_se) and keys_pressed[pygame.K_e] and town:
        mc_player.x = HEIGHT/2-20
        mc_player.y = WIDTH-200
        house = 1
        which_house = "se"
        return house, which_house, ho1_time, ho2_time, ho3_time, ho4_time
    if mc_player.colliderect(house_ne) and keys_pressed[pygame.K_e] and town:
        mc_player.x = HEIGHT/2-20
        mc_player.y = WIDTH-200
        house = 1
        which_house = "ne"
        return house, which_house, ho1_time, ho2_time, ho3_time, ho4_time
    if mc_player.colliderect(ho1) and keys_pressed[pygame.K_e] and town:
        ho1_time = 100
    else:
        ho1_time = 0
    if mc_player.colliderect(ho2) and keys_pressed[pygame.K_e] and town:
        ho2_time = 100
    else:
        ho2_time = 0
    if mc_player.colliderect(ho3) and keys_pressed[pygame.K_e] and town:
        ho3_time = 100
    else:
        ho3_time = 0
    if mc_player.colliderect(ho4) and keys_pressed[pygame.K_e] and town:
        ho4_time = 100
    else:
        ho4_time = 0
    which_house = "none"
    house = False
    return house, which_house, ho1_time, ho2_time, ho3_time, ho4_time


def indoor_system(mc_player, bookshelf, keys_pressed, tv, house):
    if mc_player.colliderect(bookshelf) and keys_pressed[pygame.K_e] and house:
        bookshelf_interact = 100
    else:
        bookshelf_interact = 0
    if mc_player.colliderect(tv) and keys_pressed[pygame.K_e] and house:
        tv_interact = 100
    else:
        tv_interact = 0
    return bookshelf_interact, tv_interact


def movement(keys_pressed, mc_player, mc_facing, anim):
    if keys_pressed[pygame.K_w] and mc_player.y - 5 > -20:
        mc_player.y -= SPEED
        mc_facing = MC_BACK
    if keys_pressed[pygame.K_s] and mc_player.y + 5 < WIDTH - 50:
        mc_player.y += SPEED
        mc_facing = MC_FRONT
    if keys_pressed[pygame.K_d] and mc_player.x + 5 < HEIGHT - 50:
        anim = anim + 1
        mc_player.x += SPEED
        if anim % 2 == 0:
            mc_facing = MC_RIGHT
        else:
            mc_facing = MC_RIGHT2
    if keys_pressed[pygame.K_a] and mc_player.x - 5 > -10:
        anim = anim + 1
        mc_player.x -= SPEED
        if anim % 2 == 0:
            mc_facing = MC_LEFT
        else:
            mc_facing = MC_LEFT2
    return mc_facing, anim


def mouse_and_icons(bag, buttons_pressed):
    if buttons_pressed[pygame.K_q]:
        while True:
            screen.blit()


def main():
    anim = 0
    mc_player = pygame.Rect(600, 50, MC_WIDTH, MC_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    mc_facing = MC_BACK
    house_nw = pygame.Rect(300, 0, 150, 150)
    house_sw = pygame.Rect(250, 370, 150, 100)
    house_se = pygame.Rect(860, 370, 150, 80)
    house_ne = pygame.Rect(820, 50, 150, 80)
    house_door = pygame.Rect(500, WIDTH, 200, 50)
    roof_door = pygame.Rect(500, 0, 200, 50)
    ho1 = pygame.Rect(house_nw.x+150, house_nw.y+150, MC_WIDTH, MC_HEIGHT)
    ho2 = pygame.Rect(house_ne.x-75, house_ne.y+100, MC_WIDTH, MC_HEIGHT)
    ho3 = pygame.Rect(house_sw.x+160, house_sw.y+140, MC_WIDTH, MC_HEIGHT)
    ho4 = pygame.Rect(house_se.x-150, house_se.y+100, MC_WIDTH, MC_HEIGHT)
    bag = pygame.Rect(10, 650, WIDTH-50, HEIGHT-50)
    quests = pygame.Rect(1200, 10, ICON_SIZE, ICON_SIZE)
    bookshelf = pygame.Rect(125, 25, 250, 125)
    tv = pygame.Rect(50, 300, 300, 200)
    which_house = "none"
    house = False
    town = True
    tv_interact = 0
    bookshelf_interact = 0
    ho1_time = 0
    ho2_time = 0
    ho3_time = 0
    ho4_time = 0
    while run:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():  # checks for events or something
            if event.type == pygame.QUIT:
                run = False  # quits from the game
        mc_facing, anim = movement(keys_pressed, mc_player, mc_facing, anim)
        if not house:
            house, which_house, ho1_time, ho2_time, ho3_time, ho4_time = entering_system(mc_player, house_nw, house_sw,
                                                                                         house_se, house_ne, ho1,
                                                                                         keys_pressed, ho2, ho3, ho4,
                                                                                         town)
        if house:
            bookshelf_interact, tv_interact = indoor_system(mc_player, bookshelf, keys_pressed, tv, house)
        house, town = screen_printer(mc_facing, mc_player, house, ho1, ho2, ho3, ho4, keys_pressed, house_door,
                                     which_house, house_nw, house_sw, house_se, house_ne, town, bookshelf_interact,
                                     bookshelf, tv_interact, tv, ho1_time, ho2_time, ho3_time, ho4_time, roof_door, bag,
                                     quests)


if __name__ == '__main__':
    main()
