import string

import pytest
import locators
import random
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def generate_random_name():
    first_parts = [
        "Kiber", "Elektro", "Kosmo", "Nano", "Tehno",
        "Robo", "Giga", "Mega", "Neo", "Bionik",
        "Digit", "Futuro", "Astro", "Gravi", "Genom",
        "Kvark", "Omega", "Sint", "Virto", "Turbo"
    ]

    second_parts = ["slav", "mir", "polk", "grad", "ver"]

    def get_new_name():
        return random.choice(first_parts) + random.choice(second_parts)

    return get_new_name


@pytest.fixture()
def generate_email():
    def get_new_email(name):
        domain = random.choice(["gmail.com", "yandex.ru", "mail.ru"])
        username = f"{name}_{random.randint(2, 9999)}"
        return f"{username}@{domain}"

    return get_new_email


@pytest.fixture()
def generate_password():
    def get_new_password():
        return ''.join(random.choices(string.ascii_letters, k=6))

    return get_new_password


@pytest.fixture()
def get_test_credentials(generate_random_name, generate_email, generate_password):
    name = generate_random_name()
    email = generate_email(name)
    password = generate_password()
    return name, email, password


@pytest.fixture()
def sign_in_user(driver, get_test_credentials):
    def _sign_in(driver, email, password):
        driver.find_element(By.XPATH, locators.Locators.EMAIL_INPUT_LOG_IN).send_keys(email)
        driver.find_element(By.XPATH, locators.Locators.PASSWORD_INPUT_LOG_IN).send_keys(password)
        driver.find_element(By.XPATH, locators.Locators.SIGN_IN_BUTTON_LOG_IN_PAGE).click()

        return driver

    return _sign_in


@pytest.fixture()
def registrate_new_user(driver):
    def _registrate(name, email, password):
        driver.find_element(By.XPATH, locators.Locators.NAME_INPUT_REGISTRATION).send_keys(name)
        driver.find_element(By.XPATH, locators.Locators.EMAIL_INPUT_REGISTRATION).send_keys(email)
        driver.find_element(By.XPATH, locators.Locators.PASSWORD_INPUT_REGISTRATION).send_keys(password)
        driver.find_element(By.XPATH, locators.Locators.REGISTRATION_BUTTON).click()

        return driver

    return _registrate
