import json
from zipfile import ZipFile

counter = 0
with ZipFile('input.zip') as myzip:
    data = myzip.namelist()
    for elem in data:
        if elem[-1] != '/' and '.json' in elem:
            with myzip.open(elem) as file:
                info = json.load(file)
            if info['city'] == 'Москва':
                counter += 1
print(counter)
