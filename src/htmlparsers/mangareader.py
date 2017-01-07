# BeautifulSoup -> MangaInfoDict
BASE_URL = 'http://www.mangareader.net'

def get_info(soup):
    property_titles = soup.select('.propertytitle')
    property_tags = [i.next_sibling.next_sibling for i in property_titles]
    return {
        'name': property_tags[0].select('.aname')[0].text,
        'author': property_tags[4].text,
        'artist': property_tags[5].text,
        'genres': [i.text for i in property_tags[7].select('.genretags')],
        'year': property_tags[2].text,
        'status': property_tags[3].text,
        'summary': soup.find(id = 'readmangasum').find('p').text,
    }

# BeautifulSoup -> ChapterList
def get_chapter_list(soup):
    def value(raw_chapter):
        i = raw_chapter.find(':') + 2
        return raw_chapter[i:]
    data = soup.find('table', id = 'listing').find_all('td')
    chapters = data[::2]
    dates = data[1::2]
    return [(value(chapters[i].text), dates[i].text) for i in range(len(chapters))]

# BeautifulSoup -> UrlString
def get_page(soup):
    return soup.find('img', id = 'img')['src']

# BeautifulSoup -> Integer
def get_chapter_length(soup):
    pass