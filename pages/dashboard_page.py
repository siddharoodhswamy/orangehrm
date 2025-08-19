from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from utils.base import BasePage

class DashboardPage(BasePage):
    # Locators
    PIM_MENU = (By.XPATH, "//span[normalize-space()='PIM']")

    def mouseClickOnPim(self):
        """Navigate to PIM menu from dashboard"""
        el = self.visible(self.PIM_MENU)
        ActionChains(self.driver).move_to_element(el).click().perform()
        print("Navigated to PIM page")
