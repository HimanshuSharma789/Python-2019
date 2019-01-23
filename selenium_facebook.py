from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://www.facebook.com")

email = browser.find_element_by_id('email')
pwd = browser.find_element_by_id('pass')
email.send_keys("username")
pwd.send_keys("password")
email.submit()