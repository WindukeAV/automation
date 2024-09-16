import random
import time

import pytest
import allure

from base.base_test import BaseTest

@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.home_page.click_user_panel_link()
        self.home_page.click_user_settings_link()
        self.account_page.click_data_editing_button()
        self.account_page.change_name(f"Test {random.randint(1, 100)}")
        self.account_page.save_changes()
        self.account_page.is_changes_saved()
        self.home_page.click_home_button()