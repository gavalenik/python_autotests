from playwright.sync_api import expect
from .base_page import BasePage


link = "http://pizzeria.skillbox.cc/my-account/"

class LoginPage(BasePage):
    def __init__(self, page):
        self.page = page

    def check_URL(self):
        BasePage.check_URL(self, link)
