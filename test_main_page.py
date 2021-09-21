from pages.main_page import MainPage
from pages.login_page import LoginPage
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)   
    page.open()                      
    page.go_to_login_page().should_be_login_page()
    
#def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
#    page = MainPage(browser, link)
#    page.open()
#    page.should_be_login_link()

#def test_is_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
#    login = LoginPage(browser, link)
#    login.open()
#    login.should_be_login_page()