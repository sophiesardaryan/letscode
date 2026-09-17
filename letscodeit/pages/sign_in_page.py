from selenium.webdriver.common.by import By
from lib.helpers import Helper
from testdata import test_data

class SignIn(Helper):
    email_input = (By.XPATH, '//input[@id="email" and @placeholder="Email Address"]')
    password_input = (By.XPATH, '//input[@id="login-password"]')
    login_btn = (By.XPATH, '//button[@id="login"]')
    email_validation_msg = (By.XPATH, '//span[text()="The email must be a valid email address."]')

    def sign_in(self):
        self.find_and_send_keys(self.email_input, test_data.email)
        self.find_and_send_keys(self.password_input, test_data.password)
        self.find_and_click(self.login_btn)
        validation_msg = self.get_text(self.email_validation_msg)
        self.test_logger.info(f'Validation Message is - {validation_msg}')
        return validation_msg