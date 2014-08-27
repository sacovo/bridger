# This module is used to communicate with peerflix
import importlib
from bridger.settings import config
from subprocess import check_output, call
from pkg_resources import resource_filename
from bridger.storage import Torrent, Track

peerflix_bin = resource_filename(__name__, 'node_modules/peerflix/app.js')

def run_peerflix(args, use_call=False):
    if use_call:
        call(['node', peerflix_bin] + args)
    else:
        return check_output(['node', peerflix_bin] + args)

def get_track_dict(torrent_url):
    output = run_peerflix([torrent_url, '-l']).decode()
    lines = output.split('\n')
    lines = [l.split(':') for l in lines if len(l.split(':'))==2]
    return dict([(int(l[0]), l[1]) for l in lines])


def open_stream(torrent_url, nr):
    output = run_peerflix([torrent_url, '--index={}'.format(nr), '-m'], use_call=True)
    return output

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
            for nr, result in enumerate(search_engine(term)):
                if nr >= results_per_api:
                    break
                yield SearchResult(**result)
        except:
            continue
