from pages.CommonPage import CommonPage

class CommonSteps:
    def __init__(self, page):
        self.page = page
        self.common_page = CommonPage(page)

    def open_url(self, url):
        self.page.goto(url)
    
    def open_signup(self):
        self.page.locator(self.common_page.SIGNUP_BUTTON).click()
    