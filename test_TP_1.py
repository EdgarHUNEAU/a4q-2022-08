import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_css_correction():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")
    time.sleep(2)
    close_cookies = driver.find_element(By.CSS_SELECTOR, ".banner-actions-container > button")
    close_cookies.click()
    category_button = driver.find_element(By.ID, "data-rayons")
    category_button.click()
    epicerie_salé = driver.find_element(By.ID, "data-rayons")
    time.sleep(5)
    driver.quit()