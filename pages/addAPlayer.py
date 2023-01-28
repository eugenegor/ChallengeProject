from pages.base_page import BasePage


class AddAPlayer(BasePage):
    add_button_xpath = "//*[text()='Add player']"



    def click_on_the_add_button(self):
         self.click_on_the_element(self.add_button_xpath)

