__author__ = 'Administrator'

# coding=utf-8

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()

print(driver.title)

WebDriverWait(driver, 10).until(EC.title_contains("selenium"))

# You should see "cheese! - Google Search"
print driver.title

# driver.quit()