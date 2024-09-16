import time

import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class AccountPage(BasePage):


    NAME = ('xpath', '//input[@id="firstName-field"]')
    SURNAME = ('xpath', '//input[@id="lastName-field"]')
    DATA_EDITING_BUTTON = ('xpath', '//button[@title="Редактирование личных данных"]')
    SAVE_BUTTON = ('xpath' , "(//button[span[text()='Сохранить']])")

    def click_data_editing_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DATA_EDITING_BUTTON)).click()

    def change_name(self, new_name):
        with allure.step(f"Change name on '{new_name}'"):
            name_field = self.wait.until(EC.element_to_be_clickable(self.NAME))
            name_field.click()
            name_field.send_keys(Keys.CONTROL, 'a')
            name_field.send_keys(Keys.CONTROL, 'DELETE')
            time.sleep(1)
            name_field.send_keys(new_name)
            self.name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Changes has been saved succesfully")
    def is_changes_saved(self):
        self.wait.until(EC.text_to_be_present_in_element_value(self.NAME, self.name))