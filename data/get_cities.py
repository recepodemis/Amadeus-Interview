from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import csv

from constants.global_constants import *

driver = webdriver.Chrome()
driver.get(FRONTEND_URL)

driver.find_element(By.XPATH,C.LIST_BUTTON_XPATH).click()
cities = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME,"truncate")))

with open("cities.xlsx",mode="w",newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    for city in cities:
       
        text = city.text
        if len(text) > 3:
            writer.writerow([text])

driver.quit()





        
        
