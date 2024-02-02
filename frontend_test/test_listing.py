import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from constants.global_constants import *
from data.get_data import get_data


class Test_Listing():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(FRONTEND_URL)
        self.driver.maximize_window()
        self.all_city = get_data()
    
    def teardown_method(self):
        self.driver.quit()
    
    @pytest.mark.parametrize('cities', get_data())
    def test_found_items(self, cities):
    
        for i in self.all_city:
            from_button = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, FROM_BUTTON_PATH)))
            from_button.clear()
            from_button.send_keys(cities)
            from_button.send_keys(Keys.ENTER)
            
            to_button = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TO_BUTTON_PATH)))
            to_button.clear()
            to_button.send_keys(i)
            to_button.send_keys(Keys.ENTER)

            try:
                WebDriverWait(self.driver, 1).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "overflow-hidden")))
                item_count = len(self.driver.find_elements(By.CLASS_NAME, "overflow-hidden"))
                item_found_text = self.driver.find_element(By.CLASS_NAME, "mb-10").text
                item_found = int(item_found_text.split()[1])
                assert item_count == item_found, f"Number of items found ({item_found}) does not match item count ({item_count})"
            except:
                item_not_found = self.driver.find_element(By.CLASS_NAME,"mt-24")
                assert item_not_found.text == "Bu iki şehir arasında uçuş bulunmuyor. Başka iki şehir seçmeyi deneyebilirsiniz."

