import os


def human_read_format(size):
    names = ['Б', 'КБ', 'МБ', 'ГБ']
    counter = 0
    while size >= 1024:
        size /= 1024
        counter += 1
    return f'{round(size)}{names[counter]}'


# start_file = input()  # по условию задачи не говорится какой именно путь файла, поэтому я предположил, что его будет
# # лучше ввести пользователю. Вводится полный путь до папки
start_file = 'C:\\Users\\Azamat\\PycharmProjects'
os.chdir(start_file)

all_dirs = []
counter = {
    os.getcwd(): 0
}
dict_name = os.getcwd()
for currentdir, dirs, files in os.walk(start_file):
    if currentdir == start_file:
        for elem in dirs:
            counter[os.path.abspath(elem)] = 0
        all_dirs = dirs
    for item in all_dirs:
        if item in currentdir:
            dict_name = os.path.abspath(item)
            break
    for el in files:
        if currentdir == start_file:
            counter[el] = os.path.getsize(currentdir + '\\' + el)
        else:
            counter[dict_name] += os.path.getsize(currentdir + '\\' + el)

sorted_counter = dict()
sorted_keys = sorted(counter, key=counter.get, reverse=True)
for elem in sorted_keys:
    sorted_counter[elem] = counter[elem]

for key, value in sorted_counter.items():
    sorted_counter[key] = human_read_format(value)

keys = list(sorted_counter.keys())[:10]
max_len = max(list(len(e) for e in keys))
print(max_len)
for key in keys:
    print(key + ' ' * (max_len - len(key)) + ' - ' + sorted_counter[key])
