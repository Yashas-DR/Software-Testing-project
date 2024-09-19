import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import string
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

    def test_register_login_purchase(self):
        driver = self.driver
        driver.get('https://crio-qkart-frontend-qa.vercel.app/')
        time.sleep(3)

        # Click on 'Register'
        register_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Register')]")
        register_button.click()
        time.sleep(3)

        # Generate random username and password
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        # Fill registration form
        driver.find_element(By.NAME, 'username').send_keys(username)
        driver.find_element(By.NAME, 'password').send_keys(password)
        driver.find_element(By.NAME, 'confirmPassword').send_keys(password)
        time.sleep(3)

        # Click 'Register Now'
        driver.find_element(By.XPATH, "//button[contains(text(), 'Register Now')]").click()
        time.sleep(3)

        # Login with the registered user
        driver.find_element(By.NAME, 'username').send_keys(username)
        driver.find_element(By.NAME, 'password').send_keys(password)
        time.sleep(3)

        # Click 'Login to QKart'
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login to QKart')]").click()
        time.sleep(3)

        # Search for 'YONEX Smash Badminton Racquet'
        search_bar = driver.find_element(By.XPATH, "//input[@placeholder='Search for items/categories']")
        search_bar.send_keys('YONEX Smash Badminton Racquet')
        time.sleep(3)

        # Click on 'ADD TO CART'
        add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add to cart')]")
        add_to_cart_button.click()
        time.sleep(3)

        # Click on 'Checkout' button on the top right
        checkout_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Checkout')]")
        checkout_button.click()
        time.sleep(3)

        # Click 'Add new address'
        add_new_address_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add new address')]")
        add_new_address_button.click()
        time.sleep(3)

        # Read address from a text file and enter it
        with open('E:/Newfolder/Yashas/address.txt', 'r') as file:
            address = file.read()

        address_textbox = driver.find_element(By.XPATH, "//textarea[@placeholder='Enter your complete address']")
        address_textbox.send_keys(address)
        time.sleep(1)

        # Click 'Add'
        driver.find_element(By.XPATH, "//button[contains(text(), 'Add')]").click()
        time.sleep(3)

        # Select the newly added address radio button
        driver.find_element(By.XPATH, "//input[@type='radio']").click()
        time.sleep(1)

        # Click 'Place Order'
        driver.find_element(By.XPATH, "//button[contains(text(), 'PLACE ORDER')]").click()
        time.sleep(3)

        # Click 'Continue Shopping'
        driver.find_element(By.XPATH, "//button[contains(text(), 'Continue Shopping')]").click()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="E:/Newfolder/Yashas/Reports"))