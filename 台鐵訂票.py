#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome('E:\chromedriver')
driver.get('http://railway.hinet.net/Foreign/TW/etno1.html')
身分證字號 = driver.find_element_by_name('person_id')
身分證字號.send_keys('A123456789')

乘車日期 = Select(driver.find_element_by_name('getin_date'))
乘車日期.select_by_value('2018/08/20-02')

起站代碼 = Select(driver.find_element_by_name('from_station'))
起站代碼.select_by_value('100')

到站代碼 = Select(driver.find_element_by_name('to_station'))
到站代碼.select_by_value('102')

車次代碼 = driver.find_element_by_name('train_no')
車次代碼.send_keys('111')
車次代碼.send_keys(Keys.TAB)

一般車廂 = Select(driver.find_element_by_name('n_order_qty_str'))
一般車廂.select_by_value('1')

車次代碼.submit()
time.sleep(1)

from PIL import Image
driver.save_screenshot('test.png')
location = driver.find_element_by_id('idRandomPic').location
x, y = location['x'] + 5, location['y'] + 5
img = Image.open('test.png')
captcha = img.crop((x, y, x+200, y+60))
captcha.convert("RGB").save('captcha.jpg', 'JPEG')
