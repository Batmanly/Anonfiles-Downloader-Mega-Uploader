from mega import Mega
import glob
import os
from anonfile import AnonFile
from login import email, password

# create directory if not exists
if not os.path.exists('downloads'):
    os.makedirs('downloads')

# Get files from anonfiles
with open("url.txt", "r") as f:
    urls = f.read().splitlines()
    print(urls)


anon = AnonFile()
mega = Mega()
for i in urls:
    print(i)
    file_name = anon.download(i, 'downloads')
    print(file_name," :::: Downloaded")


m = mega.login(email, password)
quota = m.get_quota()
print('account quota :::: ' + str(quota))
space = m.get_storage_space(mega=True)
free = space['total'] - space['used']
print('free storage :::: ' + str(free) + ' mb')
files = glob.glob('downloads/*')
for i in files:
    try:
        t = m.upload(i)
        print("uploaded :::: " + str(i) + ' :::: '+ m.get_upload_link(t))
        # delete file after upload
        os.remove(i)
    except:
        print('error uploading file :::: ' + str(i))
