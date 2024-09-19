import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import HtmlTestRunner


class EcomTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # Initialize Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")

        # Initialize Chrome service
        service = ChromeService(executable_path="E:/Newfolder/Yashas/drivers/chromedriver.exe")

        # Initialize WebDriver with the service and options
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        cls.driver.implicitly_wait(10)

    def test_login_purchase(self):
        driver = self.driver
        driver.get('https://crio-qkart-frontend-qa.vercel.app/')
        wait = WebDriverWait(driver, 10)

        # Read login credentials from a file
        with open('E:/Newfolder/Yashas/credentials.txt', 'r') as file:
            credentials = file.read().splitlines()
            username = credentials[0]
            password = credentials[1]

        # Click 'Login'
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]")))
        login_button.click()

        # Login with the provided user credentials
        wait.until(EC.visibility_of_element_located((By.NAME, 'username'))).send_keys(username)
        driver.find_element(By.NAME, 'password').send_keys(password)

        # Click 'Login to QKart'
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login to QKart')]").click()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="E:/Newfolder/Yashas/Reports"))
