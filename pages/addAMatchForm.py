import time

from pages.base_page import BasePage


class AddAMatchForm(BasePage):
    expected_title = "Add player"
    add_a_match_form_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    main_page_button = " //*[text()='Main page']"
    add_player_text_xpath = "//*[contains(@class, 'MuiTypography-h5')]"
    date_input_xpath_xpath = "//input[@type='date']"
    email_input_xpath = "//*[@name='email']"
    name_input_css = "input[name=email]"
    input_90min_css = "input[name=web90]"
    facebook_css_css = "input[name=webFB]"
    achievements_css = "input[name=achievements]"
    leg_css = "input[id=leg]"
    district_css = "input[id=district]"
    pass

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.add_a_match_form_url) == self.expected_title