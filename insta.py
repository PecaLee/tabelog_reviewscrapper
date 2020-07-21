from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

path = "..\chromedriver\chromedriver.exe"
URL = "https://www.instagram.com/accounts/login/?source=auth_switcher"

driver = webdriver.Chrome(path)


ID = input("input ID :")
PASS = input("input Password :")
keyword = input("input searching keyword :")
keyword = "#" + keyword
print(f"fetching {keyword}")


def get_html(url):
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
        "._65Bje,.coreSpriteRightPaginationArrow")
    for n in range(0, 9):
        next_btn.click()
        time.sleep(1)

    recent_image_div = driver.find_element_by_css_selector(
        ".M9sTE.L_LMM.JyscU.ePUX4")

    return recent_image_div.get_attribute('innerHTML')


'''
    source = driver.page_source
    soup = BeautifulSoup(source, "lxml")
    return soup
'''

print(get_html(URL))
