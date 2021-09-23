from .base_page import BasePage
from .locators import BasketPageLocators
class BasketPage(BasePage):

    def basket_empty(self):
         assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS),\
             "Basket is not empty"
         assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MSG),\
             "No 'basket empty' message"