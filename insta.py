from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from typing import Counter

path = "..\chromedriver\chromedriver.exe"
URL = "https://www.instagram.com/accounts/login/?source=auth_switcher"

driver = webdriver.Chrome(path)


ID = input("input ID :")
PASS = input("input Password :")
keyword = input("input searching keyword :")
keyword = "#" + keyword
print(f"fetching {keyword}")


def get_first_recent_post(url):
    driver.get(url)
    time.sleep(3)
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    login_Btn = driver.find_element_by_css_selector(
        "button.sqdOP")
    username.send_keys(ID)
    password.send_keys(PASS)
    login_Btn.click()
    time.sleep(3)
    later_Btn = driver.find_element_by_css_selector(".cmbtv .sqdOP")
    later_Btn.click()
    time.sleep(3)
    alarm_setting_none = driver.find_element_by_css_selector(".mt3GC .HoLwm")
    alarm_setting_none.click()
    time.sleep(2)
    search_box = driver.find_element_by_css_selector(".XTCLo,.x3qfX")
    search_box.send_keys(keyword)
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    first_click = driver.find_element_by_css_selector(
        ".eLAPa")
    first_click.click()
    next_btn = driver.find_element_by_css_selector(
        "._65Bje.coreSpriteRightPaginationArrow")
    for n in range(0, 9):
        next_btn.click()
        time.sleep(1)


def listing_post():
    get_first_recent_post(URL)
    how_much = input("how much do you scraping? :")
    next_btn = driver.find_element_by_css_selector(
        "._65Bje.coreSpriteRightPaginationArrow")
    hashtag_list = []
    scraped = 1

    try:
        for n in range(0, int(how_much)):
            recent_image_div = driver.find_element_by_css_selector(
                ".M9sTE.L_LMM")
            post_html = recent_image_div.get_attribute('outerHTML')
            soup = BeautifulSoup(post_html, "lxml")
            try:
                image_alt = soup.find("div", class_="KL4Bh")
                image_alt = image_alt.find("img").get("alt")
                text = soup.find("div", class_="C4VMK")
                text = text.select_one("h2 ~ span")
                text = text.find_all("a")
                for t in text:
                    hashtag_list.append(t.text)
                scraped = scraped + 1
            except:
                print("video post scraping failed.")
                pass
            next_btn.click()
            time.sleep(1)

    except:
        print(f"{scraped} post scraped.")
        pass

    return hashtag_list


def make_dict_for_insta():
    post_list = listing_post()
    count = Counter(post_list)
    words_counted = count.most_common()
    words_counted = dict(tuple(words_counted))

    return words_counted
