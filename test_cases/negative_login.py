import os
import time
import unittest
from selenium import webdriver
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class NegativeLogin(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_try_negative_login(self):
        negative_log = LoginPage(self.driver)
        negative_log.type_in_email('user07@getnada.com')
        negative_log.type_in_password('Test-123')
        negative_log.click_on_the_sign_in_button()
        negative_log.compare_warning_text()
        #negative_log.taking_text()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()