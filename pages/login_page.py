from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = 'Scouts panel - sign in'
    element_text = '//*[text()="Scouts Panel"]'
    expected_text = 'Scouts Panel'
    warring_text_xpath ="//span[contains(@class, 'MuiTypography-colorError')]"
    expected_warning_text = 'Identifier or password invalid.'




    remind_password_xpath = "//*[contains(@class, 'jss33')]"
    language_button_xpath = "//div[contains(text(),'English')]"
    header_of_box = 'Scouts Panel'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)



    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)


    def click_on_the_sign_in_button(self):
         self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) ==self.expected_title

    def compare_text(self):
        self.assert_element_text(self.driver, self.element_text, self.expected_text)


    def compare_warning_text(self):
        self.assert_element_text(self.driver, self.warring_text_xpath, self.expected_warning_text)



    def taking_text(self):
        self.take_text(self.driver, self.warring_text_xpath)

