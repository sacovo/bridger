# This is the api for kickass.to

from bs4 import BeautifulSoup as bs
from bridger.settings import get_proxy_for
import requests

factor_table = {
    'KB': 1000,
    'MB': 1000 * 1000,
    'GB': 1000 * 1000 * 1000,
    'TB': 1000 * 1000 * 1000 * 1000
}

def search_page(term, page):
    root_url = "http://kickass.to/usearch/{term}%20category%3Amusic/{page}/"
    bs_doc = bs(requests.get(root_url.format(term=term, page=page),
                proxies=get_proxy_for('kickass')).text)

    trs = bs_doc.select('table.data tr')[1:]
    source = "kickass.to"

    for tr in trs:
        torrent_name =  " ".join(tr.select('a.cellMainLink')[0].stripped_strings)
        magnet_link = tr.select('a.imagnet')[0]['href']
        seeders = int(tr.select('td.green')[0].string)
        leechers = int(tr.select('td.red')[0].string)

        nbr, factor = tr.select('td.nobr')[0].stripped_strings

        size = int(float(nbr)*factor_table[factor])

        yield dict(location=magnet_link, name=torrent_name, seeders=seeders, leechers=leechers, size=size, source=source)

def search(term):
    page = 1
    first_result = None

    while 1:
        for result in search_page(term, page):
            if first_result:
                if first_result['location'] == result['location']:
                    print(result['name'])
                    return
            else:
                first_result = result
            yield result
        page += 1
