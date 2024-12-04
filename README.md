# Software Testing Project

## Project Overview
This project automates the testing of an e-commerce website, [QKart](https://crio-qkart-frontend-qa.vercel.app/), using Selenium and Python. The test script covers user actions including registering a new account, logging in, searching for a product, adding it to the cart, providing an address, and completing the checkout process.

The results of the test cases are captured in an HTML report generated using the `HtmlTestRunner` library.

---

## Features
- **Automated Registration:** Creates a new account with a randomly generated username and password.
- **Automated Login:** Logs in with the newly created credentials.
- **Product Search and Add to Cart:** Searches for a specific product and adds it to the cart.
- **Checkout Process:** Automates the addition of a new address, selection of the address, and placement of an order.
- **HTML Report Generation:** Generates a detailed report of the test execution with pass/fail status.

---

## Technologies Used
- **Programming Language:** Python
- **Framework:** Selenium WebDriver, unittest
- **Reporting Tool:** HtmlTestRunner
- **Browser:** Google Chrome

---

## Prerequisites
1. **Python 3.x** installed on your system.
2. **Google Chrome** browser installed.
3. **Chromedriver** compatible with the installed Chrome version.
4. Required Python Libraries:
   - Selenium
   - HtmlTestRunner

Install the libraries using:
```bash
pip install selenium HtmlTestRunner
```

---

## Folder Structure
```
Project Directory
│
├── address.txt                 # Contains the address to be entered during checkout.
├── chromedriver.exe            # ChromeDriver executable.
├── Reports/                    # Generated HTML reports.
└── ecom_test.py                # Main test script.
```

---

## Usage
1. Clone or download the repository.
2. Update the path of `chromedriver.exe` in the script:  
   `E:/Newfolder/Yashas/drivers/chromedriver.exe`
3. Place the `address.txt` file containing the delivery address in the same directory.
4. Run the script:
   ```bash
   python ecom_test.py
   ```
5. The test report will be generated in the `Reports` folder.

---

## Test Report
A sample test report is shown below:

![Test Report](https://raw.githubusercontent.com/Yashas-DR/Software-Testing-project/refs/heads/main/image.png)

---

## Future Improvements
- Add more test cases for different product categories.
- Implement Page Object Model (POM) for better code organization.
- Include more browsers for cross-browser testing.

---

