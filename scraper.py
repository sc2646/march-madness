import requests

def connect_url (url, response):
    user_agent = 'python-requests/4.8.2/ (Compatible; Nana; mailto: nanaC@gmail.com)'
    r = requests.get(url, headers={'User-Agent': user_agent}, timeout=10)
    if response:
        print("Status code {} returned for url:".format(r.status_code), url)

print_response=1

url='https://www.gdax.com/'
connect_url(url,print_response)

url_robot='https://www.gdax.com//robots.txt'
connect_url(url_robot,print_response)
