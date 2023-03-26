import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en/'
    strona_glowna = "//*[text()='Main page']"
    gracze_button = "//*[text()='Players']"
    english_button = "//*[text()='Polski']"
    wyloguj_button = "//*[text()='Sign out']"
    dodaj_gracza = "//*[text()='Add player']"
    dev_team_contact = "//*[text()='Dev team contact']"
    actywnosc_text = "//*[text()='Activity']"
    konrad_matuszewski_user = "//*[text()='Konrad Matuszewski']"
    zszywacz_biurowy_dziurkacz_user = "//*[text()='Zszywacz biurowy - Dziurkacz']"
    ugly_kid_xpath = "//a[@href='/pl/players/63caf9b0fe4f704d85f59572/edit']"
    pass

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.dev_team_contact)
        assert self.get_page_title(self.dashboard_url) == self.expected_title