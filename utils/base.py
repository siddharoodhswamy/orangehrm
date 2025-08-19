from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        if text:  # checks for None or empty string
            el.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def wait_until_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_displayed(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False

    def get_attribute(self, locator, attribute):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute)
