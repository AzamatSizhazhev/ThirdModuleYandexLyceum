import os
import sys

import pygame
import requests

map_request = 'http://static-maps.yandex.ru/1.x/?ll=133.276419,-24.763952&spn=20,20&l=sat'
response = requests.get(map_request)

if not response:
    print('Ошибка выполнения запроса')
    print(map_request)
    print('Http статус', response.status_code, '(', response.reason, ')')
    sys.exit('You did something wrong')

map_file = 'map.png'
with open(map_file, 'wb') as file:
    file.write(response.content)

if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 450
    screen = pygame.display.set_mode(size)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
os.remove(map_file)