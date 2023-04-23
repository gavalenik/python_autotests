from playwright.sync_api import expect


class BasePage:
    def check_URL(self, link):
        expect(self.page).to_have_url(link)