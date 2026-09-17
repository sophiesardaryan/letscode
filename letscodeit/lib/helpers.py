from selenium.webdriver.support.ui import WebDriverWait #explicit wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import logging
import allure

class Helper:
    def __init__(self, browser, test_logger):
        self.browser = browser
        self.test_logger = test_logger

    
    def _error_with_screenshot(self, message):
        logging.error(message)
        os.makedirs(self.test_logger.screenshot_dir, exist_ok=True)
        self.browser.save_screenshot(f"{self.test_logger.screenshot_dir}/{self.test_logger.test_name}.png")
        allure.attach(
            self.browser.get_screenshot_as_png(),
            name=f"{self.test_logger.test_name}_failure",
            attachment_type=allure.attachment_type.PNG,
        )


    def navigate_to_page(self, url, new_window=False):
        try:
            if new_window:
                self.test_logger.info(f"Opens a new page in new window: {url}")
                self.browser.execute_script(f"window.open('{url}');")
            else:
                self.test_logger.info(f'Opening page: {url}')
                self.browser.get(url)
        except Exception as e:
            self._error_with_screenshot(f'Navigate to page failed: {e}')
            raise

    
    def accept_alert(self, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.alert_is_present()
            )
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            alert.accept()
            self.test_logger.info(f'Accepted alert with text: {alert_text}')
            return alert_text
        except Exception as e:
            self._error_with_screenshot(f'Accept alert failed: {e}')
            raise
    

    def find_and_click(self, locator, timeout=5):
        try:
            elem = WebDriverWait(self.browser,timeout).until(
                EC.visibility_of_element_located(locator)
            )
            elem.click()
            self.test_logger.info(f'Clicked element: {locator}')
        except Exception as e:
            self._error_with_screenshot(f'Find and click failed for {locator} : {e}')
            raise


    def find_and_send_keys(self, locator, input_text, timeout=5):
        try:
            elem = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            elem.send_keys(input_text)
            self.test_logger.info(f"The entered text is: {input_text}")
        except Exception as e:
            self._error_with_screenshot(f'Find and send keys failed for {locator} : {e}')
            raise


    def get_text(self, locator, timeout=5):
        try:
            elem = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            text = elem.text
            self.test_logger.info(f"Got text for element {locator}: {text}")
            return text
        except Exception as e:
            self._error_with_screenshot(f'Get text failed for {locator} : {e}')
            raise


    def get_attribute(self, locator, attribute, timeout=5):
        try:
            elem = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(locator)
            )
            value = elem.get_attribute(attribute)
            self.test_logger.info(f'Got attribute {attribute} for element {locator}: {value}')
            return value
        except Exception as e:
            self._error_with_screenshot(f'Get attribute failed for {locator}: {e}')
            raise
    

    def switch_window(self, window_id=0):
        try:
            self.browser.switch_to.window(self.browser.window_handles[window_id])
            self.test_logger.info(f'Switched to window: {window_id}')
        except Exception as e:
            self._error_with_screenshot(f'Switch window failed: {e}')
            raise


    def append_text_to_file(self, file_path, text):
        try:
            with open(file_path, "a+") as file:
                file.write(text + "\n")
            self.test_logger.info(f'Appended text to file {file_path}: {text}')
        except Exception as e:
            self.test_logger.error(f'Append text is failed for {file_path} : {e}')
            raise
    
    
    def move_to_element(self,element):
        try:
            actions = ActionChains(self.browser)
            actions.move_to_element(element).perform()
            self.test_logger.info(f"Move to element: {element}")
        except Exception as e:
            self._error_with_screenshot(f"Move to element failed for {element} : {e}")
            raise