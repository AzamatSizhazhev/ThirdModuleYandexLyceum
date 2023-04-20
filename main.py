import os
import sys

import pygame
import requests

map_files = list()
coordinates = tuple()
map_requests = list()


def make_maps(*args):
    global map_files, coordinates, map_requests

    coordinates = args
    map_requests = [f'http://static-maps.yandex.ru/1.x/?ll={coordinates[0][1]},{coordinates[0][0]}&spn=0.004,0.004&l=sat',
                    f'http://static-maps.yandex.ru/1.x/?ll={coordinates[1][1]},{coordinates[1][0]}&spn=0.004,0.004&l=sat',
                    f'http://static-maps.yandex.ru/1.x/?ll={coordinates[2][1]},{coordinates[2][0]}&spn=0.004,0.004&l=sat']

    for index, elem in enumerate(map_requests):
        response = requests.get(elem)

        if not response:
            print('Ошибка выполнения запроса')
            print(elem)
            print('Http статус', response.status_code, '(', response.reason, ')')
            sys.exit('Не повезло, не фортануло')

        map_files.append(f'map{index}.png')
        with open(map_files[-1], 'wb') as file:
            file.write(response.content)


def main():
    make_maps((55.70311, 37.530887), (59.940082, 30.312814), (38.889922, -77.009927))

    pygame.init()
    size = 600, 480
    screen = pygame.display.set_mode(size)

    screen.fill((200, 200, 200))
    font = pygame.font.Font(None, 20)
    text = font.render(map_requests[0], True, (50, 50, 50))
    screen.blit(text, (5, 5))

    screen.blit(pygame.image.load(map_files[0]), (0, 25))
    pygame.display.flip()

    ind = 0
    running = True
    clock = pygame.time.Clock()
    fps = 60
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                ind += 1
                if ind >= len(coordinates):
                    ind = 0
                screen.fill((200, 200, 200))
                text = font.render(map_requests[ind], True, (50, 50, 50))
                screen.blit(text, (5, 5))
                screen.blit(pygame.image.load(map_files[ind]), (0, 25))
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
    print(map_requests[0])
    for elem in map_files:
        os.remove(elem)
