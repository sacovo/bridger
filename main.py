#!/usr/bin/env python3

from bridger.torrent import search
from bridger.storage import track_storage

nr = 0
l = []
for i in search('Queen'):
    nr += 1
    print("{}: {}".format(nr, i))
    l.append(i)

nr = int(input('Input a number:\n'))
print(l[nr].location)
l[nr].save_torrent()
track = track_storage.tracks[10]
track.play()
for track in track_storage.tracks:
    print(track)

