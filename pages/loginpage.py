import pytest
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

class TestLoginPage:
  
  # URL
  URL = 'https://ectest.somone.fr/econtrol/login/'

  def __init__(self, setup):  #__init__ method, acts like the constructor. It takes in the browser, which will be passed in from the test case.
      self.setup = setup

  def load(self):
      pass

  def test_simple_authentification(self):
      print("Authentification test")
      self.driver.get(self.URL)
    
      username = "admin"
      password = "econtrolsomone2023"
  
      username_text_field= self.driver.find_element(By.ID, "login")
      username_text_field.send_keys(username)
  
      password_text_field= self.driver.find_element(By.ID, "passe")
      password_text_field.send_keys(password)
    
      self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
