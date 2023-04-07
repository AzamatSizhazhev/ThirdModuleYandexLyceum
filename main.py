import os
import sys

import pygame
import requests

map_request = 'http://static-maps.yandex.ru/1.x/?ll=29.024635,60.079834&spn=1,1&l=map&pt=29.906775,59.881227,' \
              'pmwtm1~30.312814,59.940082,pmwtm2&pl=w:3,30.274108,59.929946,30.264108,59.917787,30.206192,59.917277,' \
              '30.149341,59.893557,29.914771,59.891098'
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
