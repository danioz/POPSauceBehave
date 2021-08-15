import allure

from features.config.config import Test_Data
from features.pages.BasePage import BasePage
from features.pages.Login.elements import Elements


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Test_Data.BASE_URL)

    @allure.step("Getting title of the Login Page")
    def get_login_page_title(self):
        return self.get_title()

    @allure.step("Providing username: '{1}'")
    def input_username(self, username):
        self.do_send_keys(Elements.INPUT_USERNAME, username)

    @allure.step("Providing password: '{1}'")
    def input_password(self, password):
        self.do_send_keys(Elements.INPUT_PASSWORD, password)

    @allure.step("Clicking login button")
    def click_login(self):
        self.do_click(Elements.BTN_LOGIN)

    @allure.step("Getting error message")
    def get_error_message(self):
        return self.get_element_text(Elements.ERROR_MSG)

    @allure.step("Getting all inputs from the Login page")
    def get_inputs(self):
        list = []
        inputs = self.get_elements(Elements.INPUTS_PAGE)
        for input in inputs:
            attribute = self.get_element_attribute(input)
            list.append(attribute)
        return list

    @allure.step("Logging with the provided username: '{1}' and password: '{2}'")
    def do_login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login()
        from features.pages.Inventory.InventoryPage import InventoryPage
        return InventoryPage(self.driver)
