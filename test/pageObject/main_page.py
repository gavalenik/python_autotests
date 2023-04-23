from playwright.sync_api import expect
from .base_page import BasePage


link = "http://pizzeria.skillbox.cc/"

class MainPage(BasePage):

    def __init__(self, page):
        self.page = page
        self.login_link = page.locator(".account")
        self.search_field = page.locator(".search-field")
        self.search_button = page.locator(".search-form .searchsubmit")

    def navigate(self):
        self.page.goto(link)

    def check_URL(self):
        # expect(self.page).to_have_url(link)
        BasePage.check_URL(self, link)

    def check_page_URL(self):
        expect(self.page).to_have_url(link + "product/%d0%bf%d0%b8%d1%86%d1%86%d0%b0-%d1%80%d0%b0%d0%b9/")

    def click_login_button(self):
        self.login_link.click()

    def search_for_item(self, text):
        self.search_field.fill(text)
        self.search_field.press("Enter")
