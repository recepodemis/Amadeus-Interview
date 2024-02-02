import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from constants.global_constants import *
from data.get_data import get_data


class Test_Search():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(FRONTEND_URL)
        self.driver.maximize_window()
    
    def teardown_method(self):
        self.driver.quit()
    
    @pytest.mark.parametrize('city', get_data())
    def test_from_to_same_place(self,city):
        from_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,FROM_BUTTON_PATH)))
        from_button.click()
        from_button.send_keys(city)
        from_button.send_keys(Keys.ENTER)
        
        to_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,TO_BUTTON_PATH)))
        to_button.click()
        to_button.send_keys(city)
        to_button.send_keys(Keys.ENTER)
        
        # Beklenen durum: "From" ve "To" alanlarının aynı şehri seçmesi beklenmeyen bir durumdur
        # Test raporunda bu durumun belirtilmesi için AssertionError fırlatılır
        assert from_button.get_attribute('value') != to_button.get_attribute("value"), "Aynı şehir hem 'From' hem de 'To' olarak seçilmemelidir."
        