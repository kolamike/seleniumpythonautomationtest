import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from urllib3 import request
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup():
    driver_service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    wait = WebDriverWait(driver,10)
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.yatra.com")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()