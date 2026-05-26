from steps.CommonSteps import CommonSteps
from pages.RegisterPage import RegisterPage

class RegisterSteps(CommonSteps):

    def __init__(self, page):
        super().__init__(page)
        self.register_page = RegisterPage(page)

    def type_name(self, name):
        self.page.locator(
            self.register_page.SIGNUP_NAME_INPUT
        ).fill(name)

    def type_email(self, email):
        self.page.locator(
            self.register_page.SIGNUP_EMAIL_INPUT
        ).fill(email)

    def click_signup(self):
        self.page.locator(
            self.register_page.REGISTER_SIGNUP_BUTTON
        ).click()