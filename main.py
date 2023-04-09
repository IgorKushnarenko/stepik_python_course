import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from string import ascii_lowercase
from random import sample
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


def calc(value):
  return str(math.log(abs(12*math.sin(int(value)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.implicitly_wait(5)
try:
    browser.get(link)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.ID, 'solve').click()
finally:
    time.sleep(10)
    browser.quit()

"""def calc(value):
  return str(math.log(abs(12*math.sin(int(value)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
finally:
    time.sleep(10)
    browser.quit()

def calc(value):
  return str(math.log(abs(12*math.sin(int(value)))))


link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
finally:
    time.sleep(5)
    browser.quit()

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    field_for_first_name = browser.find_element(By.NAME, 'firstname')
    field_for_first_name.send_keys('Igor')
    field_for_last_name = browser.find_element(By.NAME, 'lastname')
    field_for_last_name.send_keys('Kushnarenko')
    field_for_email = browser.find_element(By.NAME, 'email')
    field_for_email.send_keys('i@mail.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    button_for_file = browser.find_element(By.ID, 'file')
    button_for_file.send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
finally:
    time.sleep(5)
    browser.quit()

def calc(value):
  return str(math.log(abs(12*math.sin(int(value)))))


link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    result_x = calc(x)
    input_for_answer = browser.find_element(By.ID, 'answer')
    browser.execute_script('return arguments[0].scrollIntoView(true);', input_for_answer)
    input_for_answer.send_keys(result_x)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
finally:
    time.sleep(5)
    browser.quit()



link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    a = int(browser.find_element(By.ID, 'num1').text)
    b = int(browser.find_element(By.ID, 'num2').text)
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(a + b))
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
finally:
    time.sleep(5)
    browser.quit()

def calc(value):
  return str(math.log(abs(12*math.sin(int(value)))))


link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    image = browser.find_element(By.ID, 'treasure')
    x = image.get_attribute('valuex')
    input_for_answer = browser.find_element(By.ID, 'answer')
    input_for_answer.send_keys(calc(x))
    time.sleep(1)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    attr_checkbox = checkbox.get_attribute('checked')
    assert attr_checkbox is None, 'Чек-бокс уже установлен'
    time.sleep(1)
    checkbox.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    attr_radiobutton = radiobutton.get_attribute('checked')
    assert attr_radiobutton is None, 'Радиобаттон уже в активном состоянии'
    time.sleep(1)
    radiobutton.click()
    button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button_attr = button_submit.get_attribute('disabled')
    assert button_attr is None, 'Кнопка неактивна'
    time.sleep(1)
    button_submit.click()
finally:
    time.sleep(5)
    browser.quit()

def calc(value):
  return str(math.log(abs(12*math.sin(int(value)))))


link = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    input_for_answer = browser.find_element(By.CLASS_NAME, 'form-control')
    input_for_answer.send_keys(calc(x))
    check_box = browser.find_element(By.ID, 'robotCheckbox')
    check_box.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button_submit.click()

finally:
    time.sleep(5)
    browser.quit()

link = 'http://suninjuly.github.io/registration2.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    input_for_first_name = browser.find_element(By.CSS_SELECTOR, '.form-control.first')
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
    assert 'Congratulations! You have successfully registered!' == welcome_text

finally:
    time.sleep(10)
    browser.quit()


link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()

try:
    browser.get(link)
    founded_link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    founded_link.click()
    field_for_first_name = browser.find_element(By.TAG_NAME, 'input')
    field_for_first_name.send_keys('Igor')
    field_for_last_name = browser.find_element(By.NAME, 'last_name')
    field_for_last_name.send_keys('Kushnarenko')
    field_for_city = browser.find_element(By.CLASS_NAME, 'city')
    field_for_city.send_keys('Novopolotsk')
    field_for_country = browser.find_element(By.ID, 'country')
    field_for_country.send_keys('Belarus')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(5)

finally:
    browser.quit()

link = 'http://suninjuly.github.io/huge_form.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    inputs = browser.find_elements(By.TAG_NAME, 'input')
    print(inputs)
    for key in inputs:
        key.send_keys(''.join(sample(ascii_lowercase, 5)).capitalize())
    browser.find_element(By.CLASS_NAME, 'btn').click()
finally:
    time.sleep(5)
    browser.quit()

link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()

try:
    browser.get(link)
    field_for_first_name = browser.find_element(By.TAG_NAME, 'input')
    field_for_first_name.send_keys('Igor')
    field_for_last_name = browser.find_element(By.NAME, 'last_name')
    field_for_last_name.send_keys('Kushnarenko')
    field_for_city = browser.find_element(By.CLASS_NAME, 'city')
    field_for_city.send_keys('Novopolotsk')
    field_for_country = browser.find_element(By.ID, 'country')
    field_for_country.send_keys('Belarus')
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()
    time.sleep(5)

finally:
    browser.quit()"""