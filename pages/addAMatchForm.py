from pages.base_page import BasePage


class AddAMatchForm(BasePage):
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