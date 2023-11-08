import pytest
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

@pytest.mark.usefixtures("setup")
class TestEcontrolExample:
    def test_econtrol(self):
        print("hereeeeeeeeeee")
        #self.driver.get('http://192.168.10.44:8080/econtrol/login')
        self.driver.get('https://www.google.com/')
        sleep(5)
      
        username = "admin"
        password = "econtrol"
     
        username_text_field= self.driver.find_element(By.ID, "login")
        username_text_field.send_keys(username)
     
        password_text_field= self.driver.find_element(By.ID, "passe")
        password_text_field.send_keys(password)
     
        #sleep(5)
      
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        #sleep(5)
      
        #chrome_driver.close()
