# This module is used to find torrents on pirate bay and so on...
from torrent import get_track_dict
from bridger.storage import Torrent, Track

class SearchResult(object):

    def __init__(self, **args):
        self.location = args['location']
        self.name = args['name']
        self.seeders = args['seeders']
        self.leechers = args['leechers']
        self.size = args['size']

    def save_torrent(self, track_nrs=[]):
        torrent = Torrent(self.location)
        track_dict = get_track_dict(self.location)
        if track_nrs:
            filtered_tracks = dict()
            for nr in track_nrs:
                filtered_tracks[nr] = track_dict[nr]
            track_dict = filtered_tracks
        for nr, name in track_dict.items():
            t = Track(torrent, nr, name)
