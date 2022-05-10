import pytest

@pytest.mark.usefixtures("setup")
class TestSearchFlightResults:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    def filter_flights(self):
        self.driver.find_element(By.XPATH, )
        allstops1 = self.wait.until(EC.presence_of_all_elements_located)

    lp = LaunchPage(self.driver)
    lp.searchFlights("New Delhi", "New York", "24/08/2022")