import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators
from selenium.webdriver.common.by import By


def test_navigate_to_personal_account(driver, sign_in_user):
    email, password = 'Robopolk_3907@mail.ru', 'xndYtW'
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAIN_LOGIN_BUTTON)))
    driver.find_element(By.XPATH, locators.Locators.MAIN_LOGIN_BUTTON).click()

    sign_in_user(driver, email, password)

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAKE_ORDER_BUTTON)))

    driver.find_element(By.XPATH, locators.Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.PERSONAL_ACCOUNT_PAGE_TITLE)))

    assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']")))

    driver.quit()


def test_navigate_to_constructor_button(driver, sign_in_user):
    email, password = 'Robopolk_3907@mail.ru', 'xndYtW'
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAIN_LOGIN_BUTTON)))
    driver.find_element(By.XPATH, locators.Locators.MAIN_LOGIN_BUTTON).click()

    sign_in_user(driver, email, password)

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAKE_ORDER_BUTTON)))

    driver.find_element(By.XPATH, locators.Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.PERSONAL_ACCOUNT_PAGE_TITLE)))
    driver.find_element(By.XPATH, locators.Locators.CONSTRUCTOR_BUTTON).click()

    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAKE_ORDER_BUTTON)))

    driver.quit()


def test_navigate_to_logo_button(driver, sign_in_user):
    email, password = 'Robopolk_3907@mail.ru', 'xndYtW'
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAIN_LOGIN_BUTTON)))
    driver.find_element(By.XPATH, locators.Locators.MAIN_LOGIN_BUTTON).click()

    sign_in_user(driver, email, password)

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAKE_ORDER_BUTTON)))

    driver.find_element(By.XPATH, locators.Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.PERSONAL_ACCOUNT_PAGE_TITLE)))
    driver.find_element(By.XPATH, locators.Locators.LOGO_BUTTON).click()

    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAKE_ORDER_BUTTON)))

    driver.quit()


def test_navigate_to_activate_sause_button(driver, sign_in_user):
    email, password = 'Robopolk_3907@mail.ru', 'xndYtW'

    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAIN_LOGIN_BUTTON)))
    driver.find_element(By.XPATH, locators.Locators.MAIN_LOGIN_BUTTON).click()

    sign_in_user(driver, email, password)

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAKE_ORDER_BUTTON)))

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.SAUCE_BUTTON))).click()

    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.SAUCE_BUTTON)))

    driver.quit()


def test_navigate_to_activate_bread_button(driver, sign_in_user):
    email, password = 'Robopolk_3907@mail.ru', 'xndYtW'

    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAIN_LOGIN_BUTTON)))
    driver.find_element(By.XPATH, locators.Locators.MAIN_LOGIN_BUTTON).click()

    sign_in_user(driver, email, password)

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAKE_ORDER_BUTTON)))

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.SAUCE_BUTTON)))
    driver.find_element(By.XPATH, locators.Locators.SAUCE_BUTTON).click()
    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.SAUCE_TITLE)))

    driver.quit()


def test_navigate_to_activate_topping_button(driver, sign_in_user):
    email, password = 'Robopolk_3907@mail.ru', 'xndYtW'

    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAIN_LOGIN_BUTTON)))
    driver.find_element(By.XPATH, locators.Locators.MAIN_LOGIN_BUTTON).click()

    sign_in_user(driver, email, password)

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.MAKE_ORDER_BUTTON)))

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.TOPPING_BUTTON)))
    driver.find_element(By.XPATH, locators.Locators.SAUCE_BUTTON).click()
    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.Locators.ACTIVE_TOPPING_BUTTON)))

    driver.quit()
