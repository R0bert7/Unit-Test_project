import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class TestNotificationAlerts(unittest.TestCase):
    NOTIFICATION_BANNER_SELECTOR = (By.ID, "webpushrpromptbuttons2")
    DENY_BUTTON_SELECTOR = (By.ID, "webpush-deny-button")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.cargus.ro/")

    def test_notification_deny(self):
        try:
            # Așteaptă până când bannerul pop-up devine vizibil
            notification_banner = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.NOTIFICATION_BANNER_SELECTOR)
            )

            # Găsește butonul de respingere a notificărilor în interiorul bannerului
            deny_button = notification_banner.find_element(*self.DENY_BUTTON_SELECTOR)
            deny_button.click()

            # Verifică dacă butonul a fost apăsat cu succes
            self.assertTrue(deny_button.is_enabled(), "Butonul de respingere a notificărilor nu a putut fi apăsat!")
        except NoSuchElementException:
            self.fail("Bannerul de notificări sau butonul de respingere nu au fost găsite!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()