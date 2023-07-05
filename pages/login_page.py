# from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id="password"]"
    remaind_password_hyperlink_xpath = "//*[text()="Remind password"]"
    language_listbox_xpath = "//*[@id="__next"]/form/div/div[2]/div/div"
    sign_in_button_xpath = "//*[text()="Sign in"]"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
