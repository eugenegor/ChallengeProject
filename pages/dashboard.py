from pages.base_page import BasePage


class Dashboard(BasePage):
    strona_glowna = "//*[text()='Strona główna']"
    gracze_button = "//*[text()='Gracze']"
    english_button = "//*[text()='English']"
    wyloguj_button = "//*[text()='Wyloguj']"
    dodaj_gracza = "//*[text()='Dodaj gracza']"
    dev_team_contact = "//*[text()='Dev team contact']"
    actywnosc_text = "//*[text()='Aktywnosć']"
    konrad_matuszewski_user = "//*[text()='Konrad Matuszewski']"
    zszywacz_biurowy_dziurkacz_user = "//*[text()='Zszywacz biurowy - Dziurkacz']"
    ugly_kid_xpath = "//a[@href='/pl/players/63caf9b0fe4f704d85f59572/edit']"
    pass