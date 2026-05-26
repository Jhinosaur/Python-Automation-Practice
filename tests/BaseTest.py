from steps.CommonSteps import CommonSteps
from steps.RegisterSteps import RegisterSteps

class BaseTest:

    def setup_method(self, method):

        self.common_steps = None
        self.register_steps = None

    def setup_steps(self, page):
        self.common_steps = CommonSteps(page)
        self.register_steps = RegisterSteps(page)