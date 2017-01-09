from bs4 import BeautifulSoup
import urllib3
import MySQLdb


# get an http connection
def get_http_conn():
    return urllib3.PoolManager()


# get a soup object
def get_soup(http_conn, url):
    html = http_conn.request('GET', url)
    return BeautifulSoup(html.data, 'html.parser')


def getCategories(baseUri):
    http = get_http_conn()
    soup = get_soup(http, baseUri)
    category_links = soup.find_all('div',{'class':'kategorie_baner'})[0].find_all('a')
    links = []
    for link in category_links:
        links.append(link['href'])
    return links


def getPages(videoSoup):
    return len(videoSoup.find('div',{'class':'szukaj_pagination'}).find_all('a'))-1


def downloadVideos(path):
    http = get_http_conn()
    videoSoup = get_soup(http,baseUri+path)
    pages = getPages(videoSoup)
    print(pages)

baseUri = 'http://www.kronikarp.pl/'
categories = getCategories(baseUri)
downloadVideos(categories[4])
#/szukaj,tag-690141,strona-1#szukaj



