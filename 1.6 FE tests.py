import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class front_end_tests(unittest.TestCase):
    def passed_test(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)
        input_for_first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        input_for_first_name.send_keys('Igor')
        time.sleep(1)
        input_for_last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"')
        input_for_last_name.send_keys('Kushnarenko')
        time.sleep(1)
        input_for_email = browser.find_element(By.CSS_SELECTOR, '.form-control.third')
        input_for_email.send_keys('123@email.mail')
        time.sleep(1)
        button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
        button.click()
        time.sleep(1)
        welcome_text_elem = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elem.text
        expected_result = 'Congratulations! You have successfully registered!'
        self.assertEquals(expected_result, welcome_text, 'Welcome text doesn"t match expected result')


    def failed_test(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)
        input_for_first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your name"]')
        input_for_first_name.send_keys('Igor')
        time.sleep(1)
        input_for_last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"')
        input_for_last_name.send_keys('Kushnarenko')
        time.sleep(1)
        input_for_email = browser.find_element(By.CSS_SELECTOR, '.form-control.third')
        input_for_email.send_keys('123@email.mail')
        time.sleep(1)
        button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
        button.click()
        time.sleep(1)
        welcome_text_elem = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elem.text
        expected_result = 'Congratulations! You have successfully registered!'
        self.assertEquals(expected_result, welcome_text, 'Welcome text doesn"t match expected result')


if __name__ == "__main__":
    unittest.main()