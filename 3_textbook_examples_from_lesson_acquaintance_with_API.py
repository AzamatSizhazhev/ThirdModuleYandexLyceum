import os
import sys
# import pygame
import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

# Выполнение запроса get
# response = requests.get(
#     'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Якутск&format=json')
# print(response, type(response))

# Простейшая программа, выполняющая запрос к серверу, анализирующая код ответа и в случае успешного запроса
# печатающая полученную страницу # Правильный geocoder_request =
# 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Якутск&format=json' #
# Неправильный # geocoder_request = 'http://geocode-maps.yandex.ru/1.x.1/?apikey=40d1649f-0493-4b70-98ba-98533de7710b
# &geocode=Якутск&format=json' response = requests.get(geocoder_request) if response: print(response.content) else:
# print('Ошибка выполнения запроса') print(geocoder_request) print('Http статус', response.status_code, '(',
# response.reason, ')')

# # Получить json запроса geocoder_request =
# "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Якутск&format=json"
# response = requests.get(geocoder_request) if response: # Преобразуем ответ в json-объект json_response =
# response.json()
#
#     # Получаем первый топоним из ответа геокодера.
#     # Согласно описанию ответа, он находится по следующему пути:
#     toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
#     # Полный адрес топонима:
#     toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
#     # Координаты центра топонима:
#     toponym_coodrinates = toponym["Point"]["pos"]
#     # Печатаем извлечённые из ответа поля:
#     print(toponym_address, "имеет координаты:", toponym_coodrinates)
# else:
#     print("Ошибка выполнения запроса:")
#     print(geocoder_request)
#     print("Http статус:", response.status_code, "(", response.reason, ")")

# # Static API на окне Pygame
# map_request = 'http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map'
# response = requests.get(map_request)
#
# if not response:
#     print('Ошибка выполнения запроса')
#     print(map_request)
#     print('Http статус', response.status_code, '(', response.reason, ')')
#     sys.exit(1)
#
# map_file = 'map.png'
# with open(map_file, 'wb') as file:
#     file.write(response.content)
#
# if __name__ == '__main__':
#     pygame.init()
#     size = width, height = 600, 450
#     screen = pygame.display.set_mode(size)
#     screen.blit(pygame.image.load(map_file), (0, 0))
#     pygame.display.flip()
#     while pygame.event.wait().type != pygame.QUIT:
#         pass
#     pygame.quit()
# os.remove(map_file)

# # Static API в окне PyQt
# SCREEN_SIZE = [600, 450]
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.getImage()
#         self.initUi()
#
#     def getImage(self):
#         map_request = 'http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map'
#         response = requests.get(map_request)
#
#         if not response:
#             print("Ошибка выполнения запроса:")
#             print(map_request)
#             print("Http статус:", response.status_code, "(", response.reason, ")")
#             sys.exit(1)
#
#         self.map_file = 'map.png'
#         with open(self.map_file, 'wb') as file:
#             file.write(response.content)
#
#     def initUi(self):
#         self.setGeometry(100, 100, *SCREEN_SIZE)
#         self.setWindowTitle('Отображение карты')
#
#         self.pixmap = QPixmap(self.map_file)
#         self.image = QLabel(self)
#         self.image.move(0, 0)
#         self.image.resize(*SCREEN_SIZE)
#         self.image.setPixmap(self.pixmap)
#
#     def closeEvent(self, event):
#         os.remove(self.map_file)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     ex.show()
#     sys.exit(app.exec())
