import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators
from selenium.webdriver.common.by import By

import urls


def test_registration(driver, registrate_new_user, get_test_credentials):
    name, email, password = get_test_credentials
    driver.get(urls.Urls.REGISTER_PAGE)
    registrate_new_user(name, email, password)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.LOG_IN_PAGE_TITLE)))
    current_url = driver.current_url

    assert current_url == urls.Urls.LOGIN_PAGE
    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.SIGN_IN_BUTTON_LOG_IN_PAGE)))
    driver.quit()


def test_registration_show_error_incorrect_password(driver, get_test_credentials, registrate_new_user):
    driver.get(urls.Urls.REGISTER_PAGE)
    name, email, _ = get_test_credentials
    incorrect_password = '123'
    registrate_new_user(name, email, incorrect_password)

    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.WRONG_PASSWORD_ERROR_HIGHLIGHT))
    )
    driver.quit()

