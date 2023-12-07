import pytest
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

@pytest.mark.usefixtures("setup")
class TestApplicationPage:
  def test_ajouteruneApplication(self):
      print("Authentification")
      self.driver.get('https://econtrol-dev.somone.fr/econtrol/login/')
    
      username = "narjess"
      password = "narjess"
  
      username_text_field= self.driver.find_element(By.ID, "login")
      username_text_field.send_keys(username)
  
      password_text_field= self.driver.find_element(By.ID, "passe")
      password_text_field.send_keys(password)
    
      self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
      print("Ajouter une application")
      self.driver.get('https://econtrol-dev.somone.fr/econtrol/admin/applications/')
      self.driver.set_window_size(1382, 744)
      
      self.driver.find_element(By.LINK_TEXT, "Administration").click()
      self.driver.find_element(By.CSS_SELECTOR, ".col-lg-3:nth-child(1) > .dashboard-stat").click()
      self.driver.find_element(By.ID, "application_add").click()

      libelle = "AppAuto"
      Description = "Application créée pour les tests automatisés"

      libelle_text_field= self.driver.find_element(By.NAME, 'libelle')
      libelle_text_field.send_keys(libelle)

      description_text_field= self.driver.find_element(By.CSS_SELECTOR, ".ql-editor")
      description_text_field.send_keys(Description)

      nomhyperviseur_text_field= self.driver.find_element(By.NAME, 'nomhyperviseur')
      nomhyperviseur_text_field.send_keys(libelle)

      self.driver.execute_script("window.scrollTo(0,38)")
      self.driver.find_element(By.XPATH, "//a[contains(text(),'Enregistrer')]").click()
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-message").text == "L\\\'application a bien été créée."
