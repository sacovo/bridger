#!/usr/bin/env python3

from bridger.torrent import search
from bridger.storage import track_storage
nr = 0
l = []
for i in search('Nickelback'):
    nr += 1
    print(i)
    l.append(i)

nr = int(input('Input a number:\n'))

l[nr].save_torrent()

track_storage.tracks[0].play()

