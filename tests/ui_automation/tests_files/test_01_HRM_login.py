from tests.ui_automation.page_objects.HRM_login import Login
from tests.ui_automation.tests_files.test_base import BaseTestLogin


class Test_HRM_login(BaseTestLogin):
    """This class is used for login python file"""

    def test_01_login(self):
        obj_login = Login(self.driver, self.shadow)
        print(self.driver.title)
        assert self.driver.title == "OrangeHRM"


