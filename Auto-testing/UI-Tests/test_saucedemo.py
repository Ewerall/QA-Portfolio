import pytest
from login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_credentials("standard_user", "secret_sauce")
    login_page.click_login()
    assert login_page.is_logged_in()