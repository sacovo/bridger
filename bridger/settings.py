# This module is used to load/store settings

import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {
    'storage_location':'~/.bridger.storage',
    'used_apis': 'bridger.torrent.tpb bridger.torrent.kickass bridger.torrent.bitsnoop',
    'results_per_api': '50',
    'proxy_server': '',
    'proxy_port': '',
    'download_dir': '~/music',
}

config['tpb'] = {}

config['kickass'] = {}

config['bitsnoop'] = {
    'proxy_server': '188.241.141.112',
    'proxy_port': '3127',
}


def get_proxy_for(pagename):
    if config[pagename]['proxy_server'] and config[pagename]['proxy_port']:
        return {
        'http': "{ip}:{port}".format(ip=config[pagename]["proxy_server"],
                                     port=config[pagename]["proxy_port"])
        }
    else:
        return None


def load_settings(location):
    config.read(location)


def store_settings(location):
    with open(location, 'w') as configfile:
        config.write(configfile)
