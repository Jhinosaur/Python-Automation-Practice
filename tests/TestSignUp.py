from playwright.sync_api import expect
from steps.CommonSteps import CommonSteps
from steps.RegisterSteps import RegisterSteps
from tests.BaseTest import BaseTest
from data import Constants

class TestSignUp(BaseTest):
    def test_registration(self,page):
        self.setup_steps(page)
        self.common_steps.open_url(Constants.BASE_URL)

        self.common_steps.open_signup()
        self.register_steps.type_name("nika")
        self.register_steps.type_email("nika@mail.ru")
        self.register_steps.click_signup()