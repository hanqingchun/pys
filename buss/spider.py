#!/usr/bin/python

from selenium import webdriver
driver = webdriver.PhantomJS(executable_path="phantomjs.exe")
driver.get("http://www.baidu.com")
data = driver.title
print (data)