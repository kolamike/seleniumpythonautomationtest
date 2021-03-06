import time


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollheight")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(3)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollheight")
            if lastCount == pageLength:
                match = True

        time.sleep(4)

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self,driver,10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        return list_of_elements

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self,driver,10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        return element

# the ownerr of this work is busy