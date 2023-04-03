import shutil
import datetime


def make_reserve_arc(source, dest):
    now = datetime.datetime.now()
    date = str(now.date())
    time = str(now.hour).rjust(2, '0') + '-' + str(now.minute).rjust(2, '0') + '-' + str(now.second).rjust(2, '0')
    date_time = date + time
    shutil.make_archive(date_time, 'zip', root_dir=source)
    shutil.move(date_time + '.zip', dest)


make_reserve_arc(input(), input())
