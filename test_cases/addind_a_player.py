import  time
import os
import unittest
from selenium import webdriver

from pages.addAMatchForm import AddAMatchForm
from pages.addAPlayer import AddAPlayer
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class Test(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)





    def test_add_a_player(self):
        TestLoginPage.test_log_in_to_the_system(self)

        add_a_player_page = AddAPlayer(self.driver)
        add_a_player_page.click_on_the_add_button()
        add_a_match_form = AddAMatchForm(self.driver)
        add_a_match_form.title_of_page()


    @classmethod
    def tearDown(self):
        self.driver.quit()
