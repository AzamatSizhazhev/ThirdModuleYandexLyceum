from zipfile import ZipFile


def human_read_format(size):
    names = ['Б', 'КБ', 'МБ', 'ГБ']
    counter = 0
    while size >= 1024:
        size /= 1024
        counter += 1
    return f'{round(size)}{names[counter]}'


with ZipFile('input.zip') as myzip:
    for elem in myzip.filelist:
        if elem.filename[-1] == '/':
            print('  ' * (elem.filename.count('/') - 1) + elem.filename.split('/')[-2])
        else:
            print('  ' * elem.filename.count('/') + elem.filename.split('/')[-1] + ' ' + human_read_format(
                elem.file_size))
