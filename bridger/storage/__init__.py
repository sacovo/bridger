# -*- coding: utf-8 -*-
# In this module the classes that are used to store the torrents and songs are defined
from bridger.torrent.peerflix import open_stream
from bridger.settings import config

class TorrentStorage(object):

    def __init__(self):
        self.torrents = {}

    def get_torrent(self, id):
        return self.torrents[id]

    def add_torrent(self, torrent):
        self.torrents[torrent.uuid] = torrent


class MusicStorage(object):

    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)


class Torrent(object):

    def __init__(self, location):
        self.location = location
        self.uuid = hash(location)

    def save(self):
        torrent_storage.add_torrent(self)

    def __str__(self):
        return self.location


class Track(object):

    def __init__(self, torrent, nr, name):
        self.torrent = torrent.uuid
        self.nr = nr
        self.name = name
        self.path = ''

    def play(self):
        if self.path:
            pass
        else:
            open_stream(torrent_storage.get_torrent(self.torrent).location, self.nr)

    def save(self):
        track_storage.add_track(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


global torrent_storage, track_storage

track_storage = MusicStorage()
torrent_storage = TorrentStorage()


def load_storage():
    storage = config['DEFAULT']['storage_location']
    open(storage)
