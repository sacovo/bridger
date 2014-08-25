# This is the api - module for bitsnoop

from bs4 import BeautifulSoup as bs
import requests

user_agent = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36"}

def search_page(term, page):
    root_url = "http://bitsnoop.com/search/audio/{term}/c/d/{page}/?fmt=rss"
    bs_doc = bs(requests.get(root_url.format(term=term, page=page), headers=user_agent, timeout=10).text)

    items = bs_doc.select('item')
    source = "bitsnoop.com"

    for item in items:
        torrent_name = item.title.string
        magnet_link = item.torrent.magneturi.string
        seeders = int(item.numseeders.string)
        leechers = int(item.numleechers.string)
        size = int(item.size.string)

        yield dict(location=magnet_link, name=torrent_name, seeders=seeders, leechers=leechers, size=size, source=source)
    return



def search(term):
    page = 1
    first_result = None

    while 1:
        for result in search_page(term, page):
            if first_result:
                if first_result['location'] == result['location']:
                    return
            else:
                first_result = result
            yield result
        page += 1
