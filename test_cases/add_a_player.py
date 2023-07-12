import os
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_player import AddPlayer
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

    def test_add_a_player(self):
        # BasePage.setUp(self)
        # user_login = LoginPage(self.driver)
        # user_login.title_of_page()  # check if the title of the opened page is correct
        # user_login.type_in_email('user07@getnada.com')  # enter user in the email field
        # user_login.type_in_password('Test-1234')  # enter password in the password field
        # user_login.wait_for_button_will_be_clicable()  # wait for the button to be clicable
        # user_login.click_on_the_sign_in_button()  # click on the sign in button
        # dashboard_page = Dashboard(self.driver)
        # dashboard_page.title_of_page()  # check if the title of the opened page is correct
        # time.sleep(10)
        add_player = AddPlayer(self.driver)
        add_player.type_in_email('user07@getnada.com')
        add_player.type_in_name('user')
        add_player.type_in_surname('aa')
        add_player.type_in_age('01022012')
        add_player.type_in_main_position('attacker')
        add_player.wait_for_button_will_be_clicable()
        add_player.click_on_the_submit_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(10)


    @classmethod
    def tearDown(self):
        self.driver.quit()