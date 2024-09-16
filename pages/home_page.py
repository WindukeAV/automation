import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    PAGE_URL = Links.HOME_PAGE

    USER_PANEL_BUTTON = ('xpath', '//button[@aria-controls="simple-menu"]')
    USER_SETTING_BUTTON = ('xpath', '//p[contains(text(), "Мой профиль")]')
    HOME_BUTTON = ('xpath', '//*[@id="scrollContainer"]/div/div/div[1]/nav/ol/li[1]/a')


    @allure.step("Click to 'UserPanel' link")
    def click_user_panel_link(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_PANEL_BUTTON)).click()

    @allure.step("Click to 'UserSettings' link")
    def click_user_settings_link(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_SETTING_BUTTON)).click()

    def click_home_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HOME_BUTTON)).click()