import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage
from utils.excel_utils import read_employees
from utils.screenshot_utils import ScreenshotUtils

EXCEL_FILE = r"C:\Users\siddh\OneDrive\Desktop\orangehrm_framework\data\employees.xlsx"
SHEET_NAME = "Sheet1"

class TestAddAndVerifyEmployees:

    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        """Setup method for each test"""
        self.driver = setup
        self.pim_page = PimPage(self.driver)
        self.db_page = DashboardPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.screenshot_utils = ScreenshotUtils()
        self.added_names = []

    def test_add_and_verify_employees(self):
        # 1) Login
        self.login_page.login("Admin", "admin123")

        # 2) Navigate to PIM
        self.db_page.mouse_click_on_pim()

        # 3) Add multiple employees from Excel
        employees = read_employees(EXCEL_FILE, SHEET_NAME)  # list of tuples
        for first, middle, last, emp_id in employees:
            try:
                self.pim_page.add_employee(first, middle, last, emp_id)
                self.added_names.append(f"{first} {last}")
            except Exception:
                self.screenshot_utils.take_screenshot(self.driver, f"add_failed_{first}_{last}")
                raise

        # 4) Verify in Employee
        self.pim_page.open_employee_list()
        for name in self.added_names:
            try:
                assert self.pim_page.search_employee_by_name(name), f"{name} not found in list"
                print(f"Name Verified: {name}")
            except Exception:
                self.screenshot_utils.take_screenshot(self.driver, f"verify_failed_{name}")
                raise

        # 5) Logout
        self.login_page.logout()
