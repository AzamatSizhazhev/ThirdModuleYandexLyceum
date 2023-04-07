import os
import sys

import pygame
import requests

map_request = 'http://static-maps.yandex.ru/1.x/?ll=37.697984,55.748103&spn=0.25,0.25&l=map&pt=37.439194,55.817820,' \
              'pmwtm1~37.559388,55.791248,pmwtm2~37.552166,55.715677,pmwtm3'
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
