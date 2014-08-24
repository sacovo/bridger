# This module is used to communicate with peerflix

from subprocess import check_output
from pkg_resources import resource_filename

peerflix_bin = resource_filename(__name__, 'node_modules/peerflix/app.js')

def run_peerflix(args):
    return check_output(['node', peerflix_bin] + args)


def get_track_dict(torrent_url):
    output = run_peerflix([torrent_url, '-l']).decode()
    lines = output.split('\n')
    lines = [l.split(':') for l in lines if len(l.split(':'))==2]
    return dict([(int(l[0]), l[1]) for l in lines])

test_torrent = "magnet:?xt=urn:btih:59d4476a4247fb5f1494972bd229838243f37f2d&dn=Nickelback+-+Here+And+Now+%282011%29+320kbps&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&tr=udp%3A%2F%2Fopen.demonii.com%3A1337"

get_track_dict(test_torrent)
