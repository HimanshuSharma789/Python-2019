from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()
browser.get("chrome://dino/")
space = browser.find_element_by_tag_name('body')
space.send_keys(Keys.SPACE)
space.send_keys(Keys.SPACE)
time.sleep(2)
for i in range(100):
	space.send_keys(Keys.ARROW_DOWN)
