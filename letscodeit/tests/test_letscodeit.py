import config
import pytest
from pages.practice_page import PracticePage
from pages.google_page import GooglePage
from pages.sign_in_page import SignIn
from testdata import test_data


def test_lets(get_browser, test_logger):
    practice_page_obj = PracticePage(get_browser, test_logger)
    sign_in_page_obj = SignIn(get_browser, test_logger)
    google_page_obj = GooglePage(get_browser, test_logger)

    practice_page_obj.navigate_to_page(config.main_url)
    practice_page_obj.find_and_click(practice_page_obj.alert_btn)
    alert_text = practice_page_obj.accept_alert()
    practice_page_obj.append_text_to_file(config.file_name, f'Alert text - {alert_text}')

    hide_attr = practice_page_obj.hide_element_check()
    practice_page_obj.append_text_to_file(config.file_name, f"Hidden attribute - {hide_attr}")

    practice_page_obj.mouse_hover_check()
    f_text = practice_page_obj.footer_text()
    practice_page_obj.append_text_to_file(config.file_name, f"Footer text - {f_text}")

    practice_page_obj.get_sign_in_btn()
    validation_msg = sign_in_page_obj.sign_in()
    practice_page_obj.append_text_to_file(config.file_name, f'Sign in validation message - {validation_msg}')

    assert validation_msg == test_data.validation_msg
    
    google_page_obj.open_google_page()