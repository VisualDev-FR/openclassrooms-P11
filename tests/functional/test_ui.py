from selenium.webdriver import Chrome


def test_login(driver: Chrome, base_url):

    driver.get(base_url + "/")

    assert driver.title == "GUDLFT Registration"
