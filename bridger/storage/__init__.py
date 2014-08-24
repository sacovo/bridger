# -*- coding: utf-8 -*-
# In this module the classes that are used to store the torrents and songs are defined


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

    def __init__(self, torrent, nr, **metadata):
        self.torrent = torrent.uuid
        self.nr = nr
        self.metadata = metadata


def read_torrent(torrent_location):
    """
    Runs peerflix to extract all files that are located in the given torrent.

    returns: A tuple with lenght 2, the first element is a torrent object,
             the second is a list with all tracks inside the torrent.
    """
    pass
