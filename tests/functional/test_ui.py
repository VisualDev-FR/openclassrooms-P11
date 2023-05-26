from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep


def test_user_login(driver: Chrome, base_url):

    driver.get(base_url + "/")

    assert driver.title == "GUDLFT Registration"

    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("john@simplylift.co")
    email_field.submit()
    sleep(2)

    assert driver.current_url == base_url + "/showSummary"
    assert "Welcome, john@simplylift.co" in driver.page_source
