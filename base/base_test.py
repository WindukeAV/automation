import pytest

from config.data import Data
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.account_page import AccountPage

class BaseTest:

    data: Data
    login_page: LoginPage
    home_page: HomePage
    account_page: AccountPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.home_page = HomePage(driver)
        request.cls.account_page = AccountPage(driver)
