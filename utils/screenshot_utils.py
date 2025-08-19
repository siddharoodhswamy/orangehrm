import os
from datetime import datetime

class ScreenshotUtils:
    @staticmethod
    def take_screenshot(driver, name_prefix="screenshot"):
        folder = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(folder, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name_prefix}_{timestamp}.png"
        filepath = os.path.join(folder, filename)

        driver.save_screenshot(filepath)

        print(f" Screenshot saved at: {filepath}")
        return filepath
