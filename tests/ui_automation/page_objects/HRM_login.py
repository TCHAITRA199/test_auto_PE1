from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.ui_automation.page_objects.base_page import Base_Page


class Login(Base_Page):

    # init constructor
    def __init__(self, driver, shadow):
        super().__init__(driver, shadow)

    user_name_UI = lambda self: WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    password_UI = lambda self: WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']")))
    login_button = lambda self: WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

    def login(self, username, password):
        """
            Creator: Chaitra
            Description:This function is used to login to the application
            ICP-685	Verify that the user is able to login to OMNI portal with valid username and valid password

        """
        # entering the username
        self.enter_value_send_keys(self.user_name_UI(),username)
        self.enter_value_send_keys(self.password_UI(), password)
        self.click_element(self.login_button())
