from selenium.webdriver.common.by import By
from lib.helpers import Helper

class PracticePage(Helper):

    sign_in_btn = (By.XPATH, "(//a[@href='/login'])[1]")
    alert_btn = (By.XPATH, "//*[@id='alertbtn']")
    hide_btn = (By.XPATH, "//*[@id='hide-textbox']")
    hide_show_text = (By.XPATH, "//*[@id = 'displayed-text']")
    mouse_btn = (By.XPATH, '//button[text()="Mouse Hover"]')
    mouse_top_locator = (By.XPATH, '//a[text()="Top"]')
    footer_locator = (By.XPATH, '//p[@class="small dynamic-text jqCopyRight"][1]')

    def hide_element_check(self):
        self.find_and_click(self.hide_btn)
        hide_attr = self.get_attribute(self.hide_show_text, "style")
        self.test_logger.info(f'Hidden attribute is - {hide_attr}')
        return hide_attr
    
    def mouse_hover_check(self):
        self.find_and_click(self.mouse_btn)
        self.find_and_click(self.mouse_top_locator)
        self.test_logger.info('Mouse hover check passed')


    def footer_text(self):
        footer_elem = self.browser.find_element(*self.footer_locator)
        self.move_to_element(footer_elem)
        f_text = self.get_text(self.footer_locator)
        self.test_logger.info(f'Footer text is - {f_text}')
        return f_text

    def get_sign_in_btn(self):
        sign_in_elem = self.browser.find_element(*self.sign_in_btn)
        self.move_to_element(sign_in_elem)
        self.find_and_click(self.sign_in_btn)
        self.test_logger.info('Clicked sign in button')