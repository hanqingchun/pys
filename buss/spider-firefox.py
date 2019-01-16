#!/usr/bin/python

from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
#browser = webdriver.Firefox(options=options)

browser = webdriver.Firefox()

browser.get('http://www.baidu.com')
element = browser.find_element_by_xpath("//input[@id='kw']")
element.send_keys("python")
submit = browser.find_element_by_xpath("//input[@id='su']")
submit.click()


data = browser.title
print (data)



