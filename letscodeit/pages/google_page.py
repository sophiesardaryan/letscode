from lib.helpers import Helper
from letscodeit import config

class GooglePage(Helper):
    def open_google_page(self):
        self.navigate_to_page(config.google_url, new_window=True)
        self.switch_window(1)
        self.test_logger.info('Opened Google page')