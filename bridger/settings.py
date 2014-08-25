# This module is used to load/store settings

import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {
    'storage_location':'~/.bridger.storage',
    'used_apis': 'bridger.torrent.tpb bridger.torrent.kickass bridger.torrent.bitsnoop',
    'results_per_api': '50',
}

def load_settings(location):
    config.read(location)


def store_settings(location):
    with open(location, 'w') as configfile:
        config.write(configfile)
