from selenium import webdriver
from bs4 import BeautifulSoup
import time

path = "..\chromedriver\chromedriver.exe"
URL = input("input tabelog review URL : ")
tabelog = "https://tabelog.com"

# test link https://tabelog.com/tokyo/A1301/A130101/13110478/dtlrvwlst/

driver = webdriver.Chrome(path)


def get_html(url):
    driver.get(url)
    source = driver.page_source
    soup = BeautifulSoup(source, "lxml")
    return soup


def max_page():
    soup = get_html(URL)
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


def get_post_url():
    page_urls = load_page()
    post_urls = []
    for num, page in enumerate(page_urls):
        soup = get_html(page)
        find_post_urls = soup.find_all("div", class_="rvw-item")
        print(f"{num + 1}page done")
        for post in find_post_urls:
            post_url = post.get("data-detail-url")
            post_urls.append(tabelog + post_url)
    return post_urls


print(len(get_post_url()))
