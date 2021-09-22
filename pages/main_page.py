from .base_page import BasePage
from .locators import MainPageLocators
#from selenium.webdriver.common.by import By
class MainPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*MainPageLocators.ADD_BASKET)
        add_button.click()

    def go_to_login_page(self):
       login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
       login_link.click()
       return LoginPage(browser=self.browser, url=self.browser.current_url)
       alert = self.browser.switch_to.alert
       alert.accept()


    def should_be_messages(self):
       assert self.is_element_present(*MainPageLocators.ADD_MSG), "No added book message"
       assert self.is_element_present(*MainPageLocators.BASKET_MSG), "No basket sum message"


    def messages_are_right(self):
        x = self.browser.find_element(*MainPageLocators.BASKET_MSG).text
        y = self.browser.find_element(*MainPageLocators.PRICE).text
        assert x == y, "Prices don't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def element_should_be_disappeared(self):
        assert self.is_disappeared(*MainPageLocators.SUCCESS_MESSAGE), \
           "Element has not disappeared, but should have"