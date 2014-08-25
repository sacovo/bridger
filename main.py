#!/usr/bin/env python3

from bridger.torrent import search

for nr, result in enumerate(search("Nickelback")):
    print(nr,result.source, result.name)
