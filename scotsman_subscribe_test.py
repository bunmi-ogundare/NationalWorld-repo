import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def setup_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


def test_scotsman_homepage(setup_browser):
    driver = setup_browser
    baseURL = "https://www.scotsman.com/"
    driver.get(baseURL)

    driver.switch_to.frame(1)

    time.sleep(2)

    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#notice > div.message-component.message-row.unstack > button.message-component.message-button.no-children.focusable.sp_choice_type_11.last-focusable-el')))
    element.click()

    driver.switch_to.default_content()

    page_title = driver.title
    assert "Latest News | The Scotsman" in page_title, f"Expected 'Latest News | The Scotsman' in title, but got {page_title}"

    time.sleep(7)

    subscribe_button_selector = "div[class='Header__PrimaryTopMenu-sc-1vz791g-12 bSkENH'] span[class='ProfileOptions__Subscribe-sc-1x2z2a7-2 iXvHqf']"
    subscribe_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, subscribe_button_selector)))
    subscribe_button.click()

    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.title_contains("Subscribe | The Scotsman"))

    time.sleep(2)

    driver.switch_to.frame(0)

    buy_now_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "card-checkout-digital-plus-a"))
    )
    buy_now_button.click()

    time.sleep(5)

    driver.switch_to.default_content()

    driver.quit()

