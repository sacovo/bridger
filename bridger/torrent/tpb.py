# This is the api for thepiratebay.se

from bs4 import BeautifulSoup as bs
import requests
from api import SearchResult

factor_table = {
    'KiB': 1024,
    'MiB': 1024 * 1024,
    'GiB': 1024 * 1024 * 1024,
    'TiB': 1024 * 1024 * 1024 * 1024
}

def search_page(term, page):
    bs_doc = bs(requests.get("http://thepiratebay.se/search/" + term + "/" + str(page) + "/7/101/").text)
    trs = bs_doc.select('table#searchResult tr')


    for tr in trs:
        columns = tr.find_all('td')
        if len(columns) != 4:
            continue

        torrent_name = columns[1].a.text
        magnet_link = columns[1].find_all('a')[1]['href']
        seeders = int(columns[2].text)
        leechers = int(columns[3].text)

        detDesc_text = columns[1].font.text
        size_str= detDesc_text.split(',')[1].replace('Size', '').strip()
        factor = factor_table[size_str[-3:]]
        size = int(float(size_str[:-3])*factor)

        yield SearchResult(location=magnet_link, name=torrent_name, seeders=seeders, leechers=leechers, size=size)

def search(term):
    page = 0
    results = []
    while 1:
        torrents = list(search_page(term, page))
        page+=1
        if len(results) > 0:
            if results[0].location == torrents[0].location:
                break
        results += torrents
    return results

print(len(search('Nickelback')))
