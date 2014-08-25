# Torrent api for torrentdownload.me
from bs4 import BeautifulSoup as bs
import requests

user_agent = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36"}

def search_page(term, page):
    root_url = "http://www.torrentdownloads.me/rss.xml?type=search&cid=5&search={term}"
    bs_doc = bs(requests.get(root_url.format(term=term, page=page)).text)

    trs = bs_doc.select('table.data tr')[1:]
    source = "kickass.to"

    for tr in trs:
        torrent_name =  "".join(tr.select('a.cellMainLink')[0].stripped_strings)
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
        results = list(search_page(term, page))
        page+=1
        if first_result:
            if first_result == results[0]['location']:
                break
        else:
            first_result = results[0]
        for result in results:
            yield result
