import time
from pages.base_page import BasePage



class LoginPage(BasePage):
    header_of_box = 'Scouts Panel'
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    remaind_password_hyperlink_xpath = "//*[text()='Remind password']"
    language_listbox_xpath = "//*[@id="__next"]/form/div/div[2]/div/div"
    sign_in_button_xpath = "//*[text()='Sign in']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en/login')
    expected_title = "Scouts panel - sign in"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        test_title = self.get_page_title(self.login_url)
        time.sleep(5)
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_title_of_header(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.header_of_box)
