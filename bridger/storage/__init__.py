# -*- coding: utf-8 -*-
# In this module the classes that are used to store the torrents and songs are defined

def load_storage():
    pass


class TorrentStorage(object):

    def __init__(self):
        self.torrents = []


class MusicStorage(object):

    def __init__(self):
        self.tracks = []


class Torrent(object):

    def __init__(self, location):
        self.location = location
        self.uuid = hash(location)


class Track(object):

    def __init__(self, torrent, nr, name):
        self.torrent = torrent.uuid
        self.nr = nr
        self.name = name
