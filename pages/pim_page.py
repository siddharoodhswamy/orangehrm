import time
from selenium.webdriver.common.by import By
from utils.base import BasePage

class PimPage(BasePage):
    # Tabs
    ADD_EMPLOYEE_TAB = (By.XPATH, "//a[normalize-space()='Add Employee']")
    EMPLOYEE_LIST_TAB = (By.XPATH, "//a[normalize-space()='Employee List']")

    # Add Employee fields
    FIRSTNAME = (By.NAME, "firstName")
    MIDDLENAME = (By.NAME, "middleName")
    LASTNAME = (By.NAME, "lastName")
    EMP_ID = (By.XPATH, "//label[normalize-space()='Employee Id']/../following-sibling::div//input")
    SAVE_BTN = (By.XPATH, "//button[@type='submit']")  # first visible submit

    # Employee search fields
    EMP_NAME_FILTER = (By.XPATH, "//label[normalize-space()='Employee Name']/../following-sibling::div//input")
    SEARCH_BTN = (By.XPATH, "//button[normalize-space()='Search']")
    TABLE_ROWS = (By.XPATH, "//div[contains(@class,'oxd-table-body')]/div[@role='row']")

    """Navigate to Add Employee tab"""
    def open_add_employee(self):
        self.click_element(self.ADD_EMPLOYEE_TAB)

    """Add a new employee"""
    def add_employee(self, first, middle, last, emp_id):
        self.open_add_employee()
        self.enter_text(self.FIRSTNAME, first)
        self.enter_text(self.MIDDLENAME, middle)
        self.enter_text(self.LASTNAME, last)

        emp = self.wait_until_element_visible(self.EMP_ID)
        emp.clear()
        if emp_id:
            emp.send_keys(str(emp_id))

        self.click_element(self.SAVE_BTN)
        print(f"Employee Added: {first} {last} ({emp_id})")
        time.sleep(2)

    """Navigate to Employee List tab"""
    def open_employee_list(self):
        self.click_element(self.EMPLOYEE_LIST_TAB)

    """Search for employee by name and return True if found"""
    def search_employee_by_name(self, full_name: str) -> bool:
        self.enter_text(self.EMP_NAME_FILTER, full_name)
        self.click_element(self.SEARCH_BTN)
        time.sleep(2)

        rows = self.driver.find_elements(*self.TABLE_ROWS)
        for r in rows:
            if full_name.lower() in r.text.lower():
                print(f" Found employee in list: {full_name}")
                return True
        print(f" Employee not found: {full_name}")
        return False
