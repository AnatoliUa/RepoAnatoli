import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(service = Service('chromedriver.exe'))
    driver.get('https://github.com/login')
    login_elem = driver.find_element(By.ID, "login_field")
    login_elem.send_keys("onetwothree")
    pass_elem = driver.find_element(By.ID, "password")
    pass_elem.send_keys("wrongpass")
    btn_elem = driver.find_element(By.NAME, "commit")
    btn_elem.click()
    assert driver.title == "Sign in to GitHub · GitHub"
    driver.close()