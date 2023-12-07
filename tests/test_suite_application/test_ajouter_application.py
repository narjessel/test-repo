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
      login_page = TestLoginPage()
      login_page.load()

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
