from zipfile import ZipFile

with ZipFile('input.zip') as myzip:
    for elem in myzip.filelist[1:]:
        if elem.filename[-1] == '/':
            print('  ' * (elem.filename.count('/') - 2) + elem.filename.split('/')[-2])
        else:
            print('  ' * elem.filename.count('/') + elem.filename.split('/')[-1])
