import requests
from bs4 import BeautifulSoup


URL_LIST = ['https://www.gdax.com/', 'https://www.nasdaq.com/markets/indices/major-indices.aspx', 'http://www.google.com', 'https://docs.python.org/2/library/pprint.html']

def connect_url(url):
    user_agent = 'python-requests/4.8.2/ (Compatible; Nana; mailto: nanaC@gmail.com)'
    r = requests.get(url, headers={'User-Agent': user_agent}, timeout=10)
    if r and r.status_code==200:
        # print "Status code {} returned for url:".format(r.status_code), url
        print r.status_code
        print url + " allowed access"
        # print r.text
        return r


def find_links(response):
    soup = bs(response.content, "html.parser")
    for a in soup.find_all('a'):
        try:
            print "====="
            if a.get('href').startswith('https://') or a.get('href').startswith('http://'):
                print a.text
                print a.get('href')
        except AttributeError:
            pass


def scrape_list(list):
    for url in URL_LIST:
        connect_url(url)



scrape_list(URL_LIST)

# url='https://www.gdax.com/'
# connect_url(url)
#
# url_robot='https://www.gdax.com//robots.txt'
# connect_url(url_robot)


