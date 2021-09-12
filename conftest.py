import pytest
from selenium import webdriver

from Config.TestData import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        # options = webdriver.ChromeOptions()
        # options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--incognito')
        web_driver = webdriver.Chrome(TestData.CHROME_DRIVER_PATH)
        web_driver.maximize_window()
    request.cls.driver = web_driver
    web_driver.get(TestData.SITE_URL)
    yield
    web_driver.close()


@pytest.mark.usefixtures("init_driver")
class InitDriver:
    pass