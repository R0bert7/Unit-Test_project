import unittest
from Test_Notifications import TestNotificationAlerts
from Test_Cookies import TestCookiesButton
from Test_Cargus_Website import TestCargusWebsite
import xmlrunner


def run_tests_with_report():
    # Creează un obiect TestLoader pentru a încărca toate testele
    loader = unittest.TestLoader()

    # Încarcă clasele de test din fiecare fișier
    test_classes = [TestCookiesButton, TestNotificationAlerts, TestCargusWebsite]

    # Creează o suită de teste pentru fiecare clasă de test
    suites = [loader.loadTestsFromTestCase(tc) for tc in test_classes]

    # Creează o suită de teste globală care conține toate celelalte suite
    all_tests_suite = unittest.TestSuite(suites)

    # Rulează toate testele și afișează rezultatele
    with open("test_report.xml", "wb") as report_file:
        runner = xmlrunner.XMLTestRunner(
            output=report_file,
            verbosity=2
        )
        runner.run(all_tests_suite)


if __name__ == "__main__":
    run_tests_with_report()
