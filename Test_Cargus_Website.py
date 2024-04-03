import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class TestCargusWebsite(unittest.TestCase):
    COOKIES_ACCEPT_SELECTOR = (By.ID, "onetrust-accept-btn-handler")
    PRETURI_BUTTON_SELECTOR = (By.XPATH, '//a[contains(@class, "kt-blocks-info-box-title") and contains(text(), "Preturi")]')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.cargus.ro/")
        self.driver.maximize_window()

    def test_accept_cookies_and_click_preturi_button(self):
        try:
            cookies_accept_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.COOKIES_ACCEPT_SELECTOR)
            )
            cookies_accept_button.click()
        except NoSuchElementException:
            self.fail("Butonul de acceptare a cookies nu a fost găsit!")

        try:
            preturi_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.PRETURI_BUTTON_SELECTOR)
            )
            preturi_button.click()
            # Aici puteți adăuga alte acțiuni sau verificări după ce faceți clic pe butonul "Preturi"
        except NoSuchElementException:
            self.fail("Butonul 'Preturi' nu a fost găsit!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
