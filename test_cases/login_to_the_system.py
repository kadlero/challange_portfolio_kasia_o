import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/login')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()  # check if the title of the opened page is correct
        user_login.type_in_email('user07@getnada.com')  # enter user in the email field
        user_login.type_in_password('Test-1234')  # enter password in the password field
        user_login.wait_for_button_will_be_clicable()  # wait for the button to be clicable
        user_login.click_on_the_sign_in_button()  # click on the sign in button
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()  # check if the title of the opened page is correct
        time.sleep(10)


@classmethod
def tearDown(self):
    self.driver.quit()


def test_print_nice_words(self):
    print("WELL DONE!!!!!!!!!")

# Element of the first task: Try to search the Internet yourself how to get rid of the error:
# "DeprecationWarning: executable_path has been deprecated, please pass in a Service object"
