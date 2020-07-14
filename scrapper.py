from selenium import webdriver
from bs4 import BeautifulSoup
import time

path = "..\chromedriver\chromedriver.exe"
URL = "https://tabelog.com/tokyo/A1301/A130101/13110478/dtlrvwlst/"
tabelog = "https://tabelog.com"

driver = webdriver.Chrome(path)


def get_html():
    driver.get(URL)
    source = driver.page_source
    soup = BeautifulSoup(source, "lxml")
    return soup


def max_page():
    soup = get_html()
    try:
        find_pagination = soup.find("ul", class_="c-pagination__list")
        find_pages = find_pagination.find_all("li")
        pages = []
        for page in find_pages:
            pages.append(page.text)
    except:
        pages = None

    if pages != None:
        del pages[-1]
    driver.close()
    return pages


def load_page():
    pages = max_page()
    page_urls = []
    if pages != None:
        for page in pages:
            page_url_form = f"COND-0/smp1/?smp=1&lc=0&rvw_part=all&PG={page}"
            page_URL = URL + page_url_form
            page_urls.append(page_URL)
    else:
        page_urls.append(URL)
    return page_urls


print(load_page())
