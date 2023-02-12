import unittest

from unittest.loader import makeSuite


from test_cases.framework import Test
from test_cases.youtube_fill_and_delete import YoutubeFillAndDelete
from test_cases.change_language import ChangeLanguage
from test_cases.negative_login import NegativeLogin
from test_cases.login_to_the_system import TestLoginPage
from test_cases.go_to_a_player_page import GoOnAPlayerPage
from test_cases.filling_form_and_add_player import FillingForm
from test_cases.choose_leg import ChooseLeg
from test_cases.sign_out import SigningOut


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(ChangeLanguage))
   test_suite.addTest(makeSuite(ChooseLeg))
   test_suite.addTest(makeSuite(FillingForm))
   test_suite.addTest(makeSuite(GoOnAPlayerPage))
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(NegativeLogin))
   test_suite.addTest(makeSuite(SigningOut))
   test_suite.addTest(makeSuite(YoutubeFillAndDelete))
   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())