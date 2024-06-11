from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Base_Page:

    def __init__(self, driver, shadow):
        self.driver = driver
        self.shadow = shadow

    # defining the common methods for all the pages

    def click_element(self, element):
        sleep(2)
        ActionChains(self.driver).click(element).perform()
        sleep(3)

    def enter_value(self, element, value):
        sleep(2)
        # element.send_keys(value)
        ActionChains(self.driver).send_keys_to_element(element, value).perform()
        sleep(2)

    def enter_value_send_keys(self, element, value):
        sleep(1)
        element.send_keys(value)
        sleep(1)

    def get_text(self, element):
        sleep(1)
        txt_element = element.text
        sleep(1)
        return txt_element

    def check_enabled(self, element):
        bool_element = element.is_enabled()
        return bool_element

    def check_displayed(self, element):
        sleep(1)
        bool_element = element.is_displayed()
        return bool_element

    def check_selected(self, element):
        sleep(1)
        bool_element = element.is_selected()
        return bool_element

    def get_attribute(self, element, attribute_type):
        sleep(1)
        attribute_value = element.get_attribute(attribute_type)
        return attribute_value

    def moveToElement(self, param):
        pass

    def move_to_ele_and_get_tooltip_text(self, hover_element, tool_tip_selector="span[role='tooltip']"):
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_element).perform()
        sleep(1)
        element = self.driver.find_element(By.CSS_SELECTOR, tool_tip_selector)
        text = element.get_attribute("innerText")
        return text

    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def select_dropdown_value(self, element, value):
        """Creator: Neethu
        Description: To select a specific value from a dropdown bases on the inner text"""
        for i in element:
            print(self.get_text(i))
            if self.get_text(i) == value:
                self.click_element(i)
                break
        sleep(2)

    def select_first_dropdown_value(self, element):
        """Creator: Neethu
        Description: To select a first value from a dropdown"""
        for i in element:
            self.click_element(i)
            break
        sleep(2)

    def select_specific_dropdown_values(self, element, attribute, values):
        """Creator: Neethu
        Description: To select specific values from drop down. It selects multiple values"""
        for i in element:
            for j in values:
                if self.get_attr_value(i, attribute) == j:
                    self.click_element(i)
                    sleep(1)
                    break
        sleep(2)

    def select_all_dropdown_values(self, element):
        """Creator: Neethu
        Description: Selects all values from drop down"""
        for i in element:
            self.click_element(i)

    def select_few_dropdown_values(self, element,n):
        """Creator: Neethu
        Description: Selects all values from drop down"""
        j = 1
        for i in element:
            if j <=n:
                self.click_element(i)
                j=+1
            else:
                break
