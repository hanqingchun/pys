#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


options = webdriver.FirefoxOptions()
options.add_argument('-headless')
#browser = webdriver.Firefox(options=options)

browser = webdriver.Firefox()

try:


    browser.get("http://120.26.69.228/rand.php")
    input_all=browser.find_element_by_id("all")
    input_all.send_keys("100000")
    #input.send_keys(Keys.ENTER)
    input_count=browser.find_element_by_id("count")
    input_count.send_keys("100000")
    #input.send_keys(Keys.ENTER)

    submit = browser.find_element_by_xpath("//input[@id='Button1']")
    submit.click()

    wait=WebDriverWait(browser,10)
    wait.until(EC.presence_of_element_located((By.ID,"content_left")))
    print(browser.current_url)
    #print(browser.get_cookies())
    #print(browser.page_source)
    time.sleep(10)
finally:
    browser.close()


