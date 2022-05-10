import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class Demoexplicitwait():
    def demo_explicit_wait(self):
        driver_service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com")
        wait = WebDriverWait(driver, 20)
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)

        going_to = self.wait.driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.click()
        going_to.send_keys("New York")
        going_to.send_keys(Keys.ENTER)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()

        all_dates = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[@id='30/05/2022']"))).find_element(By.XPATH, "//td[@id='30/05/2022']")
        all_dates.click()

        driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()

        # driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']").click()
        # time.sleep(4)
        # driver.find_element(By.XPATH, "//td[@id='30/05/2022']").click()
        # time.sleep(4)

        # search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        # print(len(search_results))
        # for results in search_results:
        #     print(results.text)
        #     if "New York (JFK)" in results.text:
        #         results.click()
        #         break
        # wait = WebDriverWait(driver, 10)
        # wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']").click())).find_element((By.XPATH, "//td[@id='30/05/2022']").click())

        # driver.find_element(By.XPATH, "//td[@id='30/05/2022']").click()
        # driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
        # all_dates = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='monthwrapper']//tbody//td[@class!='inActiveTD']"))).find_elements(By.XPATH,"//div[@id='monthwrapper']//tbody//td[@class!='inActiveTD']")
        # # all_dates = driver.find_elements(By.XPATH, "//div[@id='monthwrapper']//tbody//td[@class!='inActiveTD']")
        # for date in all_dates:
        #     if date.get_attribute("data-date") == "30/06/2022":
        #         date.click()
        #         break

        # driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']").click()
        # time.sleep(4)
        # driver.find_element(By.XPATH, "//td[@id='10/06/2022']").click()

        # time.sleep(4)
        # # time.sleep(4)


suggest = Demoexplicitwait()
suggest.demo_explicit_wait()