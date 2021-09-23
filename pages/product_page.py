from .base_page import BasePage
from .main_page import MainPage
from .locators import ProductPageLocators
class ProductPage(MainPage):
    
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        add_button.click()        

    def should_be_messages(self):
       assert self.is_element_present(*ProductPageLocators.ADD_MSG), "No added book message"
       assert self.is_element_present(*ProductPageLocators.BASKET_MSG), "No basket sum message"

    def messages_are_right(self):
        x = self.browser.find_element(*ProductPageLocators.BASKET_MSG).text
        y = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert x == y, "Prices don't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def element_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Element has not disappeared, but should have"