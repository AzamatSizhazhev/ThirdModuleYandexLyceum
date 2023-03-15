# Модули os и os.path
# import os
#
# # print(dir(os))  # Функции
# #
# # print(os.name)  # содержит строковое значение с типом операционной системы, в которой выполняется наша программа
# # # posix - Linux и macOS
# # # nt — для операционных систем семейства Windows
# # # java — для систем, работающих в виртуальной Java-машине (например, Android)
# #
# # print(os.getcwd())  # имя текущего каталога
# #
# # os.chdir('files')  # Для смены текущего каталога
# # print(os.getcwd())
# #
# # os.chdir('..')
# # print(os.getcwd())
# #
# # # Проверка файла и папки в данной директории
# # print(os.access('main.py', os.F_OK))  # Существует
# # print(os.access('main.py', os.W_OK))  # Доступен для записи
# # print(os.access('main.py', os.R_OK))  # Доступен для чтения
# #
# # print(os.access('files', os.F_OK))  # Существует
# # print(os.access('files', os.W_OK))  # Доступен для записи
# # print(os.access('files', os.R_OK))  # Доступен для чтения
# #
# # print(os.listdir())  # Для получения списка файлов и вложенных каталогов в текущей папке
# # print(os.listdir('files'))  # В указанной папке
# #
# # # функция рекурсивного прохода по всем папкам в заданной папке
# # for current_dir, dirs, files in os.walk('files'):
# #     print(current_dir, dirs, files)
# #
# # print(dir(os.path))  # Функции
#
# # print(os.path.exists('files/3'))  # Првоерка на существование
# # print(os.path.isfile('files/3'))  # Проверка на файл
# # print(os.path.isdir('files/3'))  # Проверка на папку
#
# # print(os.path.abspath('uaebrae'))  # абсолютный путь по относительному (существование не обязательно)
# # print(os.path.dirname('files\3\files\csvs\дthrthgf'))  # полное имя каталога, в котором находится файл(необязательно
# # существующий)
########################################################################################################################
# Модуль shutil (shell utilities)
# import shutil
#
# # shutil.copy('files/3/Описание.txt', 'files/Копия.txt')  # Копирование из файла источника в приемник
# # shutil.rmtree('files/new')  # удаление папки
# # print(shutil.get_archive_formats())  # Система архивов
# # shutil.make_archive('archive', 'zip', root_dir='files')
########################################################################################################################
# Модуль Zip-архивы
# from zipfile import ZipFile
#
# # with ZipFile('archive.zip') as myzip:
# #     myzip.printdir()  # Выводит содержиние архива
# #     print()
# #     info = myzip.infolist()  # Информация о файлах в виде списка
# #     print(info[0].orig_filename)
# #     print()
# #     print(myzip.namelist())  # Имена файлов в виде списка
#
# # Вывести содержимое файла
# # with ZipFile('archive.zip') as myzip:
# #     with myzip.open('1.txt', 'r') as file:
# #         print(file.read().decode('utf-8'))
#
# # Перезапись архива, существующим файлом из папки, в которой сейчас
# # with ZipFile('archive.zip', 'w') as myzip:
# #     myzip.write('test.txt')
# #     print(myzip.namelist())  # Должен вывести ['test.txt']
#
# # Добавить файл в существующий архив, существующим файлом из папки, в которой сейчас
# # with ZipFile('archive.zip', 'a') as myzip:
# #     myzip.write('test.txt')
# #     print(myzip.namelist())
#
# # # Вытаскивает из рхива все содержимое в указанную папку
# # with ZipFile('archive.zip') as myzip:
# #     myzip.extractall(path='unpack_zip', members=None, pwd=None)
# # # Если указать path=None, то скопируется в текущую папку
########################################################################################################################
# Формат JSON
#
# # # pickle превращает любой объект Python в байтовую структуру и обратно
# # from pickle import loads, dumps
# # s = {'Иван': 24, 'Сергей': 11}
# #
# # d = dumps(s)
# # print(d)
# #
# # print()
# #
# # d = loads(d)
# # print(d)
#
# import json
#
# # Читает файл json и выводит содержимое полученного словоря
# # with open('cats_json.json') as cat_file:
# #     data = json.load(cat_file)
# #
# # for key, value in data.items():
# #     if type(value) == list:
# #         print(f'{key}: {", ".join(value)}')
# #     else:
# #         print(f'{key}: {value}')
#
# # Создание json из представленного файла
#
# # s = 'He Json'  # Некоректный json: json.decoder.JSONDecodeError
# # json.loads(s)
#
# # with open('cats_2.json') as cat_file:
# #     f = cat_file.read()
# #     data = json.loads(f)
# # for item in data:
# #     for key, value in item.items():
# #         if type(value) == list:
# #             print(f'{key}: {", ".join(value)}')
# #         else:
# #             print(f'{key}: {value}')
# #     print()
#
# # Cоздадим словарь, в котором коту добавим хозяев, а затем полученную информацию сохраним в файле
# # cats_dict = {
# #     'name': 'Pushin',
# #     'age': 1,
# #     'maels': [
# #         'Purina', 'Cat Show', 'Hills'
# #     ],
# #     'owners': [
# #         {
# #             'first_name': 'Bill',
# #             'last_name': 'Gates'
# #         },
# #         {
# #             'first_name': 'Melinda',
# #             'last_name': 'Gates'
# #         }
# #     ]
# # }
# #
# # with open('cats_3.json', 'w') as cats_file:
# #     json.dump(cats_dict, cats_file)
#
# # Преобраование объекта в строку формата json
# # weekdays = {i: day
# #             for i, day in enumerate(['Sunday',
# #                                      'Monday',
# #                                      'Tuesday',
# #                                      'Wednesday',
# #                                      'Thursday',
# #                                      'Friday',
# #                                      'Saturday'])}
# # data = json.dumps(weekdays)
# # print(data)
# # print(type(data))
#
# # Дополнительные парметры методов записи
# # data = [
# #     {
# #         "name": "\u0411\u0430\u0440\u0441\u0438\u043a",
# #         "age": 7,
# #         "toys": [
# #             "\u041c\u044b\u0448\u043a\u0430",
# #             "\u041f\u0440\u0443\u0442\u0438\u043a",
# #             "\u0411\u0430\u043d\u0442\u0438\u043a",
# #             "\u0421\u0432\u043e\u0439 \u0445\u0432\u043e\u0441\u0442"
# #         ]
# #     },
# #     {
# #         "name": "\u041c\u0443\u0440\u0437\u0438\u043a",
# #         "age": 3,
# #         "toys": [
# #             "\u0420\u0443\u043a\u0430 \u0445\u043e\u0437\u044f\u0439\u043a\u0438",
# #             "\u0428\u043d\u0443\u0440 \u043e\u0442 \u0442\u0435\u043b\u0435\u0432\u0438\u0437\u043e\u0440\u0430",
# #             "\u041e\u0431\u043e\u0438 \u043d\u0430 \u0441\u0442\u0435\u043d\u0435"
# #         ]
# #     }
# # ]
# #
# # with open('cats.json', 'w') as file:
# #     json.dump(data, file, ensure_ascii=False, indent=2, sort_keys=True)
