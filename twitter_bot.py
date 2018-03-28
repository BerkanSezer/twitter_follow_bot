import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(chrome_options=options)

try:
    twitter_account = sys.argv[1]
    follower_need = int(sys.argv[2])
except Exception:
    print("Arguments not Found")
    sys.exit(-1)

def loginPage():
    url="http://www.twitter.com/login"
    submit_count = 1
    browser.get(url)

    while True:
        if (browser.current_url == "https://twitter.com/"):
            break
        print("Redirecting Page: ", browser.current_url)
        print("trying submit - ",submit_count)
        username_box = browser.find_element_by_class_name("js-username-field")
        username_box.clear()
        username_box.send_keys('YOUR_USERNAME')
        password_box = browser.find_element_by_class_name("js-password-field").clear()
        password_box = browser.find_element_by_class_name("js-password-field").send_keys('<YOUR_PASSWORD>')
        form = browser.find_element_by_class_name('js-signin')
        form.submit()
        submit_count += 1
    redirectPage()

def redirectPage():
    url="http://www.twitter.com/"+ twitter_account + "/followers"
    print("Redirecting Page: ", browser.current_url)
    browser.get(url) #opened followers page
    time.sleep(3) #wait for loading new people
    last_height = browser.execute_script("return document.body.scrollHeight")
    follow_click_counter = 0
    SCROLL_PAUSE_TIME = 5.0
    follow_buttons = []
    total_click_counter = 0
    scroll_count = 1
    print("Looking...")

    while follow_click_counter < follower_need:
        print("Scrolling Page", scroll_count)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = browser.execute_script("return document.body.scrollHeight")
        # scroll_state = browser.execute_script('document.addEventListener("DOMContentLoaded", function() {return true}')
        # print(scroll_state, 'SCROLL_STATE')
        if new_height == last_height:
            break
        last_height = new_height
        print("Scrolled - " , scroll_count)
        scroll_count += 1
        follow_buttons = browser.find_elements_by_class_name("follow-button")
        for follow_button in follow_buttons:
            if follow_button.text == "Follow\nFollow":
                browser.execute_script("arguments[0].click();", follow_button) #click using JS
                follow_click_counter += 1
                print(follow_click_counter, "\tUser Has Been Followed")
                time.sleep(0.5)
            if follow_click_counter == follower_need:
                break
            total_click_counter += 1
        follow_buttons = []
    print("\n\n")
    print(total_click_counter, "\tPeople Has Been Seen")
    print(follow_click_counter, "\tFollower Has Been Followed")

loginPage()
browser.quit()
print("D.O.N.E.")
