#!/usr/bin/python

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.baidu.com/')


data = browser.title
print (data)