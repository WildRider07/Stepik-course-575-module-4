from .base_page import BasePage
from .locators import LoginPageLocators, RegisterFormLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This is not a login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*RegisterFormLocators.EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*RegisterFormLocators.PASSWORD)
        password_field.send_keys(password)
        confirm_password = self.browser.find_element(*RegisterFormLocators.CONFIRM_PASSWORD)
        confirm_password.send_keys(password)
        register_button = self.browser.find_element(*RegisterFormLocators.REGISTER)
        register_button.click()