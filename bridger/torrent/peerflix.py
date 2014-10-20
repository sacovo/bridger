from subprocess import check_output, call
from pkg_resources import resource_filename

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


def download_file(torrent_url, nr, directory):
    output = run_peerflix([torrent_url, '--index=' + str(nr), '--path='+directory + ''], use_call=True)
    return output

