from selenium import webdriver
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    def open(self):
        self.browser.get(self.url)
main ="http://selenium1py.pythonanywhere.com/en-gb/catalogue/category/books_2/"
oscar =  BasePage(webdriver.Chrome(), main)
oscar.open()