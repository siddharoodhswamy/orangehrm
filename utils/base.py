from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        """Wait until element is clickable and then click"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        """Clear existing text and type new text if provided"""
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        if text:  # checks for None or empty string
            el.send_keys(text)

    def get_text(self, locator):
        """Get visible element text"""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def visible(self, locator):
        """Return element if visible"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_displayed(self, locator):
        """Check if element is displayed (returns True/False instead of raising exception)"""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False

    def get_attribute(self, locator, attribute):
        """Fetch attribute value of an element"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute)
