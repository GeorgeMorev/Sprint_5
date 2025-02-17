import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators
from selenium.webdriver.common.by import By


def test_log_in_from_main_page(driver, registrate_new_user, sign_in_user):
    email, password = 'Robopolk_3907@mail.ru', 'xndYtW'
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAIN_LOGIN_BUTTON)))
    driver.find_element(By.XPATH, locators.Locators.MAIN_LOGIN_BUTTON).click()

    sign_in_user(driver, email, password)

    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAKE_ORDER_BUTTON)))

    driver.quit()


def test_log_in_via_personal_account_button(driver, sign_in_user):
    email, password = 'Robopolk_3907@mail.ru', 'xndYtW'
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(
        (expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.PERSONAL_ACCOUNT_BUTTON))))
    driver.find_element(By.XPATH, locators.Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.LOG_IN_PAGE_TITLE)))

    sign_in_user(driver, email, password)

    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAKE_ORDER_BUTTON)))

    driver.quit()


def test_log_in_via_register_page_button(driver, sign_in_user):
    email, password = 'Robopolk_3907@mail.ru', 'xndYtW'
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, locators.Locators.SIGN_IN_BUTTON_REGISTRATION_PAGE).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.SIGN_IN_BUTTON_LOG_IN_PAGE)))

    sign_in_user(driver, email, password)

    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAKE_ORDER_BUTTON)))

    driver.quit()


def test_log_in_via_password_repair_page_button(driver, sign_in_user):
    email = 'Robopolk_3907@mail.ru'
    password = 'xndYtW'
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(By.XPATH, locators.Locators.SIGN_IN_BUTTON_REGISTRATION_PAGE).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.SIGN_IN_BUTTON_LOG_IN_PAGE)))

    sign_in_user(driver, email, password)

    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAKE_ORDER_BUTTON)))

    driver.quit()
