# This module is used to communicate with peerflix
import importlib
from bridger.settings import config
from bridger.storage import Torrent, Track
from bridger.torrent.peerflix import get_track_dict


search_engines = dict()

def load_engines():
    if search_engines:
        return
    apis = config['DEFAULT']['used_apis'].split(" ")

    for api in apis:
        search_engines[api] = importlib.import_module(api).search

class SearchResult(object):

    def __init__(self, **args):
        self.location = args['location']
        self.name = args['name']
        self.seeders = args['seeders']
        self.leechers = args['leechers']
        self.size = args['size']
        self.source = args['source']

    def get_tracks(self):
        return get_track_dict(self.location)

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
            t.save()
        torrent.save()

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name


def search(term):
    load_engines()
    results_per_api = int(config['DEFAULT']['results_per_api'])
    for name, search_engine in search_engines.items():
        try:
            nr = 0
            for result in search_engine(term):
                nr += 1
                if nr >= results_per_api:
                    break
                yield SearchResult(**result)
        except:
            continue
