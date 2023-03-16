import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("-incognito")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('http://10.15.1.204:3000/')
    driver.maximize_window()
    problem3Menu = driver.find_element(By.CSS_SELECTOR, "#ftco-nav > ul > li:nth-child(4) > a")
    problem3Menu.click()
    time.sleep(1)
    return driver

def test_correct_total():
    driver = setup_driver()
    driver.execute_script("window.scrollBy(0, 450);")
    time.sleep(1)
    buttons = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button[class="btn btn-primary btnPlus"]')))

    #random_indices = random.sample(range(len(buttons)), 6)
    #random_indices = [0, 1, 3, 2, 9, 10, 11]
    random_numbers = random.sample(range(4), 4) + random.sample(range(9, 12), 2)
    for i, index in enumerate(random_numbers):
        buttons[index].click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#listaItema li:nth-child(' + str(i + 1) + ')')))
        if i == len(random_numbers) - 1:
            buttons[index].click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#listaItema li:nth-child(' + str(i + 1) + ')')))
            time.sleep(2)

    price_list = []
    for i in random_numbers:
        price_filed = driver.find_elements(By.CSS_SELECTOR, '.price')[i]
        price = int(price_filed.text[1:])
        price_list.append(price)
    price_list.append(price_list[-1])

    total_price_list = sum(price_list)
    total_cart = driver.find_elements(By.CSS_SELECTOR, '#ukupno')

    assert total_price_list == int(total_cart[0].text)

    driver.quit()

def test_incorrect_total():
    driver = setup_driver()
    driver.execute_script("window.scrollBy(0, 450);")
    time.sleep(1)
    buttons = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button[class="btn btn-primary btnPlus"]')))
    #random_indices = random.sample(range(len(buttons)), 6)
    random_numbers = random.sample(range(4), 3) + random.sample(range(9, 12), 2)
    for i, index in enumerate(random_numbers):
        buttons[index].click()
        if i == len(random_numbers) - 1:
            buttons[index].click()

    price_list = []
    for i in random_numbers:
        price_filed = driver.find_elements(By.CSS_SELECTOR, '.price')[i]
        price = int(price_filed.text[1:])
        price_list.append(price)
    price_list.append(price_list[-1])

    total_price_list = sum(price_list)
    total_cart = driver.find_elements(By.CSS_SELECTOR, '#ukupno')

    assert total_price_list == int(total_cart[0].text)

    driver.quit()

