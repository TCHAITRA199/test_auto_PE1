import pytest
from time import sleep
from pyshadow.main import Shadow
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from tests.ui_automation.configuration.basic_config import TestData
from tests.ui_automation.page_objects.HRM_login import Login


@pytest.fixture(params=["chrome"], scope='class')
def init_driver_all(request):
    """This fixture is used to test the all the other test functionality.
   """

    web_driver = None
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option('useAutomationExtension', False)
    # options.add_argument("--headless")
    options.add_argument("--test-type")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")

    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=service, options=options)

    request.cls.driver = web_driver
    web_driver.implicitly_wait(7)
    shadow = Shadow(web_driver)
    request.cls.shadow = shadow

    web_driver.delete_all_cookies()
    web_driver.maximize_window()

    web_driver.delete_all_cookies()
    web_driver.maximize_window()
    web_driver.get(TestData.login_URL)
    sleep(5)
    obj_login = Login(web_driver, shadow)
    obj_login.login("Admin", "admin123")
    sleep(10)
    yield
    web_driver.close()
