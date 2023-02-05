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


class FillingAForm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_filling_A_Form(self):
        TestAddingAplayer.test_add_a_player(self)
        filling_text = AddAMatchForm(self.driver)
        filling_text.main_button_is_visible()
        filling_text.filling_a_form('trhrht@gmail.com', 'Mihal', 'Zazeckii', '05.09.1996', 'head')
        time.sleep(3)

        #filling_text.screenshoot_method()



    @classmethod
    def tearDown(self):
        self.driver.quit()