# This should define functions to scrape the HTML of websites and the images which are the pages.

import urllib2

# UrlString -> HtmlString
def get_source(url):
    return urllib2.urlopen(url).read()