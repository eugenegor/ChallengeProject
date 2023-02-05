import os
import time
import unittest
from selenium import webdriver
from pages.addAMatchForm import AddAMatchForm
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from test_cases.addind_a_player import TestAddingAplayer
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class ChangeLanguage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_changing_language(self):
        TestAddingAplayer.test_add_a_player(self)
        language = AddAMatchForm(self.driver)
        language.language_change()
        language.screenshoot_method()





    @classmethod
    def tearDown(self):
        self.driver.quit()