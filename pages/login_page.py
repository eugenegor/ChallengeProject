from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    remind_password_xpath = "//*[contains(@class, 'jss33')]"
    language_button_xpath = "//div[contains(text(),'English')]"
    

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
