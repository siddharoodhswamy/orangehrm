from selenium.webdriver.common.by import By
from utils.base import BasePage

class LoginPage(BasePage):

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    USER_DROPDOWN = (By.CSS_SELECTOR, "p.oxd-userdropdown-name")
    LOGOUT_LINK = (By.XPATH, "//a[normalize-space()='Logout']")

    def login(self, username: str, password: str):

        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click_element(self.LOGIN_BTN)
        print(f" Login attempted with user: {username}")

    def logout(self):

        self.click_element(self.USER_DROPDOWN)
        self.click_element(self.LOGOUT_LINK)
        print(" Logout successful")
