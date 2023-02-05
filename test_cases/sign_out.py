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


class SigningOut(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_filling_first_and_second_form(self):
        TestAddingAplayer.test_add_a_player(self)
        signOut = AddAMatchForm(self.driver)
        signOut.signing_out()
        time.sleep(3)
        signOut.screenshoot_method()



    @classmethod
    def tearDown(self):
        self.driver.quit()