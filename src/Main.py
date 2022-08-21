import pygame
import planets.pygame_settings as setting

from planets.Planet import Planet

pygame.init()

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, setting.yellow, 1.98892 * 10**30, 'elyria MS6', 'Você')
    sun.sun = True

    arges = Planet(0.387 * Planet.au, 0, 8, setting.dark_grey, 3.30 * 10**23, 'arges', 'Aceita')
    arges.y_vel = -47.4 * 1000

    mimas = Planet(0.623 * Planet.au, 0, 14, setting.white, 4.8685 * 10**24, 'mimas', 'Sair')
    mimas.y_vel = -35.02 * 1000

    nyctimus = Planet(-1.1 * Planet.au, 0, 16, setting.purple, 5.9742 * 10**24, 'nyctimus', 'Comigo')
    nyctimus.y_vel = 29.783 * 1000

    styx = Planet(-1.234 * Planet.au, 0, 11, setting.green, 7.67 * 10**24, 'styx', '<3')
    styx.y_vel = 30.645 * 1000

    ceyx = Planet(-1.524 * Planet.au, 0, 12, setting.red, 6.39 * 10**23, 'ceyx', '?')
    ceyx.y_vel = 24.077 * 1000


    planets = [sun, nyctimus, ceyx, arges, mimas, styx]

    while run:
        clock.tick(60)
        setting.win.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(setting.win)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()