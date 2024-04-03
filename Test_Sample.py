import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class TestCourierWebsite(unittest.TestCase):
    def setUp(self):
        self.webdriver = webdriver.Chrome()
        self.webdriver.get("https://www.cargus.ro/")

    def test_cookies_button_exists(self):
        try:
            # Așteaptă până când bannerul cookie-urilor devine vizibil
            banner = WebDriverWait(self.webdriver, 10).until(
                EC.visibility_of_element_located((By.ID, "onetrust-banner-sdk"))
            )

            # Găsește butonul de acceptare a cookie-urilor în interiorul bannerului
            cookies_button = banner.find_element(By.ID, "onetrust-accept-btn-handler")
        except NoSuchElementException:
            self.fail("Butonul de cookies nu a fost găsit pe pagină!")

    def test_accept_cookies_button(self):
        try:
            # Așteaptă până când bannerul de notificări devine vizibil
            notification_banner = WebDriverWait(self.webdriver, 10).until(
                EC.visibility_of_element_located((By.ID, "onetrust-banner-sdk"))
            )
            # Găsește butonul de acceptare a notificărilor în interiorul bannerului
            accept_button = notification_banner.find_element(By.ID, "onetrust-accept-btn-handler")
            # Face clic pe butonul "Acceptă notificări"
            accept_button.click()
            # Aici poți adăuga verificări suplimentare sau acțiuni după ce faci clic pe buton
        except NoSuchElementException:
            self.fail("Butonul de acceptare a notificărilor nu a fost găsit în bannerul de notificări!")


class TestAlerts(unittest.TestCase):
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

            # Face clic pe butonul de respingere a notificărilor
            deny_button.click()

            # Aici puteți adăuga alte acțiuni sau verificări după ce faceți clic pe buton
        except NoSuchElementException:
            self.fail("Bannerul de notificări sau butonul de respingere nu au fost găsite!")

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

    def test_search_bar_exists(self):
        try:
            search_bar = self.driver.find_element(By.CLASS_NAME, "tracking_number")
            self.assertTrue(search_bar.is_displayed(), "Search bar not visible")
        except NoSuchElementException:
            self.fail("Search bar not found")

    def test_search_bar_functionality(self):
        try:
            search_bar = self.driver.find_element(By.CLASS_NAME, "tracking_number")
            search_bar.send_keys("colet")
            search_button = self.driver.find_element(By.CLASS_NAME, "tracking_button")
            search_button.click()
            # Add assertions to verify search results page or expected behavior after clicking
        except NoSuchElementException:
            self.fail("Search bar or search button not found")

    def test_contact_information_exists(self):
        try:
            contact_info_wrap = self.driver.find_element(By.CLASS_NAME, "kt-blocks-info-box-learnmore-wrap")
            contact_info_button = contact_info_wrap.find_element(By.CLASS_NAME, "kt-blocks-info-box-learnmore")
            self.assertTrue(contact_info_button.is_displayed(), "Contact information button not visible")
        except NoSuchElementException:
            self.fail("Contact information button not found")

    def test_contact_form_submission(self):
        try:
            # Find the contact information button and click on it
            contact_info_wrap = self.driver.find_element(By.CLASS_NAME, "kt-blocks-info-box-learnmore-wrap")
            contact_info_button = contact_info_wrap.find_element(By.CLASS_NAME, "kt-blocks-info-box-learnmore")
            contact_info_button.click()

            # Now find the contact form and fill it
            contact_form = self.driver.find_element(By.ID, "contact-form")
            name_field = contact_form.find_element(By.NAME, "persoana-contact")  # Persoana de contact
            email_field = contact_form.find_element(By.NAME, "adresa-email")  # Email
            message_field = contact_form.find_element(By.NAME, "mesaj")  # Mesaj
            submit_button = contact_form.find_element(By.CLASS_NAME, "wpcf7-submit")  # Butonul de submit
            agreement_checkbox = contact_form.find_element(By.NAME, "acceptance-gdpr")  # Caseta de bifat pentru acord GDPR

            name_field.send_keys("John Doe")
            email_field.send_keys("johndoe@example.com")
            message_field.send_keys("This is a test message.")
            agreement_checkbox.click()  # Bifează caseta de acord GDPR

            submit_button.click()

            # Add assertions to verify form submission or expected behavior after clicking
        except NoSuchElementException:
            self.fail("Contact information button or contact form elements not found")

    def test_social_media_links(self):
        try:
            # Găsește toate link-urile către iconurile de social media
            social_media_links = self.driver.find_elements(By.XPATH, "//a[contains(@class, 'facebook')]")

            # Iterează prin fiecare link găsit
            for link in social_media_links:
                # Obține atributul href
                href = link.get_attribute("href")
                # Verifică dacă href este gol sau nu
                if href:
                    print("Link-ul către iconul de social media:", href)
                else:
                    print("Link-ul către iconul de social media nu a fost găsit")
        except Exception as e:
            self.fail("Link-urile către iconurile de social media nu au putut fi găsite sau nu au putut fi accesate!")

    def test_social_media_icons(self):
        try:
            # Găsește toate elementele de tip imagine care conțin src-ul specificat
            social_media_icons = self.driver.find_elements(By.XPATH, "//img[contains(@src, '/wp-content/uploads/cargus-theme/facebook-black.svg')]")

            # Iterează prin fiecare element găsit
            for icon in social_media_icons:
                # Obține atributul href
                href = icon.get_attribute("href")
                # Verifică dacă href este gol sau nu
                if href:
                    print("Link-ul către iconul de social media:", href)
                else:
                    print("Link-ul către iconul de social media nu a fost găsit")
        except Exception as e:
            self.fail(
                "Iconurile de social media nu au putut fi găsite sau link-urile către ele nu au putut fi accesate!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
