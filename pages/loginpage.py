import pytest
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

class TestLoginPage:
  
  # URL
  URL = 'https://ectest.somone.fr/econtrol/login/'

  def __init__(self,driver):
        self.driver = driver

  def test_simple_authentification(self):
      print("Authentification test")
      self.driver.get('https://ectest.somone.fr/econtrol/login/')
    
      username = "admin"
      password = "econtrolsomone2023"
  
      username_text_field= self.driver.find_element(By.ID, "login")
      username_text_field.send_keys(username)
  
      password_text_field= self.driver.find_element(By.ID, "passe")
      password_text_field.send_keys(password)
    
      self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
