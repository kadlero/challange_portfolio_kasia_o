from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import time


class Dashboard (BasePage):
    expected_title = "Scouts Panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en/'
    main_page_field_xpath = "//*[@id='__next']/form/div/div[2]/div/div"
    main_page_logo_field_xpath = "//*[contains(@title, 'Logo')]"
    add_player_button_xpath = "//*[text()='Add player']"
    add_player_email_field_xpath = "//*[@name='email']"
    add_player_left_leg_listbox_xpath = "//*[@role='option' and @data-value='left']"
    add_player_district_mazovia_listbox_xpath = "//*[@role='option' and @data-value='mazowieckie']"
    players_show_column_club_checkbox_xpath = "//*[@type='checkbox' and @value='club']"
    players_add_match_date_xpath = "//*[@name='date' and @type='date']"
    main_page_logo_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[1]"
    sign_out_button_xpath = "//*[text()='Sign out']"
    players_print_icon_xpath = "//*[@type='button' and @title='Print']"

def title_of_page(self):
    time.sleep(5)
    assert self.get_page_title(self.login_url) == self.expected_title

#Subtask 5
def assert_element_text(self, driver, xpath, expected_text):
   """Comparing expected text with observed value from web element

       :param driver: webdriver instance
       :param xpath: xpath to element with text to be observed
       :param expected_text: text what we expecting to be found
       :return: None
   """
   element = driver.find_element(by=By.XPATH, value=xpath)
   element_text = element.text
   assert expected_text == element_text