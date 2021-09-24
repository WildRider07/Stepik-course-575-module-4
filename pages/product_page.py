from .base_page import BasePage
from .main_page import MainPage
from .locators import ProductPageLocators
class ProductPage(MainPage):
    
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()        

    def should_be_messages(self):
       assert self.is_element_present(*ProductPageLocators.ADDED_MSG), "No added book message"
       assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MSG), "No basket sum message"

    def messages_are_right(self):
        name_in_msg = self.browser.find_element(*ProductPageLocators.ADDED_NAME).text
        name_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert name_in_msg == name_on_page, "Names don't match"

        price_in_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        main_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert price_in_message == main_product_price, "Prices don't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_MSG), \
           "Success message is presented, but should not be"

    def element_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_MSG), \
           "Success message has not disappeared, but should have"