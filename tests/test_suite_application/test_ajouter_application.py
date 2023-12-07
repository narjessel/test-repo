import pytest
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from pages.loginpage import TestLoginPage

@pytest.mark.usefixtures("setup")
class TestApplicationPage:
  def test_ajouteruneApplication(self):
      print("Authentification")
      login_page = TestLoginPage(self)
      login_page.test_simple_authentification()
    
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
    
      element = self.driver.find_element(By.XPATH, "//a[contains(text(),'Enregistrer')]")
      self.driver.execute_script("arguments[0].click();", element)

      WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".toast-message")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-message").text == "L'application a bien été créée."
