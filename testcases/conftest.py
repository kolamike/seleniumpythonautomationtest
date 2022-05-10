import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='class')
def setup(request):
    driver_service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.yatra.com")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close