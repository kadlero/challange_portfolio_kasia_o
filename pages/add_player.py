from pages.base_page import BasePage


class AddPlayer(BasePage):
    header_of_box = 'Add player'
    title_of_box_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[1]/div/span"
    email_field_xpath = "//*[@name='email']"
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    age_field_xpath = "//*[@name='age']"
    main_position_field_xpath = "//*[@name='mainPosition']"
    submit_button_xpath = "//*[@type='submit']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en/players/add')
    expected_title = "Add player"

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def click_on_the_submit_button(self, submit_button):
        return self.driver.find_element(self.submit_button_xpath, submit_button).click()

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_title_of_header(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.header_of_box)
