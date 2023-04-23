from playwright.sync_api import Page, expect, sync_playwright
from pageObject.main_page import MainPage
from pageObject.login_page import LoginPage


def test_main_page_has_title_and_URL():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        main_page = MainPage(page)
        main_page.navigate()
        main_page.check_URL()
        main_page.search_for_item("Рай")
        main_page.check_page_URL()
        main_page.click_login_button()
        login_page = LoginPage(page)
        login_page.check_URL()
