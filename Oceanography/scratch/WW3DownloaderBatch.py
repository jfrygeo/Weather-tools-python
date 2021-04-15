#downloads a list of ww3 files

import os.path
import urllib.request

links = open('C://Users//john6807//Documents//GitHub//Weather-tools-python//Oceanography//urlwinds.txt', 'r')
for link in links:
    link = link.strip()
    name = link.rsplit('/', 1)[-1]
    filename = os.path.join('C://Users//john6807//Documents//GitHub//Weather-tools-python//Oceanography//filesdownloaded//', name)

    if not os.path.isfile(filename):
        print('Downloading: ' + filename)
        try:
            urllib.request.urlretrieve(link, filename)
        except Exception as inst:
            print(inst)
            print('  Encountered unknown error. Continuing.')