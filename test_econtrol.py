import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
 
def test_econtrol():
    options = webdriver.ChromeOptions()
    options.add_arguments("--no-sandbox");
    options.add_arguments("--disable-dev-shm-usage");
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_driver = webdriver.Chrome(options=options)
    
    chrome_driver.get('http://192.168.10.44:8080/econtrol/login')
    chrome_driver.maximize_window()
 
    username = "admin"
    password = "econtrol"

    username_text_field= chrome_driver.find_element(By.ID, "login")
    username_text_field.send_keys(username)

    password_text_field= chrome_driver.find_element(By.ID, "passe")
    password_text_field.send_keys(password)

    sleep(5)
 
    chrome_driver.find_element(By.XPATH, "//button[@type='submit']").click()
    sleep(5)
 
    chrome_driver.close()
