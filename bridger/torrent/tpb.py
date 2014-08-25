# This is the api for thepiratebay.se

from bs4 import BeautifulSoup as bs
import requests

factor_table = {
    'KiB': 1024,
    'MiB': 1024 * 1024,
    'GiB': 1024 * 1024 * 1024,
    'TiB': 1024 * 1024 * 1024 * 1024
}

def search_page(term, page):
    bs_doc = bs(requests.get("http://thepiratebay.se/search/" + term + "/" + str(page) + "/7/101/").text)
    trs = bs_doc.select('table#searchResult tr')

    source = "thepiratebay.se"


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

        yield dict(location=magnet_link, name=torrent_name, seeders=seeders, leechers=leechers, size=size, source=source)

def search(term):
    page = 0
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
