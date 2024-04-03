import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class TestCookiesButton(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.cargus.ro/")

    def test_cookies_button_exists(self):
        try:
            # Așteaptă până când bannerul cookie-urilor devine vizibil
            banner = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "onetrust-banner-sdk"))
            )

            # Găsește butonul de acceptare a cookie-urilor în interiorul bannerului
            cookies_button = banner.find_element(By.ID, "onetrust-accept-btn-handler")
            self.assertIsNotNone(cookies_button, "Butonul de cookies nu a fost găsit pe pagină!")
        except NoSuchElementException:
            self.fail("Butonul de cookies nu a fost găsit pe pagină!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()