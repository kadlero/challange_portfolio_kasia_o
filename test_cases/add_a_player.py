import os
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAdAplayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_ad_a_player(self):
        BasePage.setUp(self)
        user_login = LoginPage(self.driver)
        user_login.wait_for_button_will_be_clicable()
        user_login.click_on_the_sign_in_button()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_name('user')
        user_login.type_in_surname('07')
        user_login.type_in_age('01022012')
        user_login.type_in_age('attacker')
        user_login.wait_for_button_will_be_clicable()
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()  # check if the title of the opened page is correct
        time.sleep(10)


    @classmethod
    def tearDown(self):
        self.driver.quit()