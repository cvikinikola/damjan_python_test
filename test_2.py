import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

summer = None
winter = None
tea = None
coffee = None
white = None
black = None
sweet = None
salty = None
sour = None
hot = None
spoon = None
fork = None
deep = None
shallow = None
fruit = None
vegetables = None
cocktail = None
beer = None
readMyMind = None


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("-incognito")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('http://10.15.1.204:3000/')
    driver.maximize_window()
    problem2 = driver.find_element(By.CSS_SELECTOR, "#ftco-nav > ul > li:nth-child(3) > a")
    problem2.click()
    time.sleep(1)
    return driver

def get_elements(driver):
    global summer
    global winter
    global tea
    global coffee
    global coffee
    global white
    global black
    global sweet
    global salty
    global sour
    global hot
    global spoon
    global fork
    global deep
    global shallow
    global fruit
    global vegetables
    global cocktail
    global beer
    global readMyMind
    summer = driver.find_element(By.ID, "btn1")
    winter = driver.find_element(By.ID, "btn2")
    tea = driver.find_element(By.ID, "btn3")
    coffee = driver.find_element(By.ID, "btn4")
    white = driver.find_element(By.ID, "btn5")
    black = driver.find_element(By.ID, "btn6")
    sweet = driver.find_element(By.ID, "btn7")
    salty = driver.find_element(By.ID, "btn8")
    sour = driver.find_element(By.ID, "btn9")
    hot = driver.find_element(By.ID, "btn10")
    spoon = driver.find_element(By.ID, "btn11")
    fork = driver.find_element(By.ID, "btn12")
    deep = driver.find_element(By.ID, "btn13")
    shallow = driver.find_element(By.ID, "btn14")
    fruit = driver.find_element(By.ID, "btn15")
    vegetables = driver.find_element(By.ID, "btn16")
    cocktail = driver.find_element(By.ID, "btn17")
    beer = driver.find_element(By.ID, "btn18")
    readMyMind = driver.find_element(By.ID, "readmymind")

def test_avocado_o():
    driver = setup_driver()
    get_elements(driver)
    left_button = [summer, tea, white, sweet, sour, spoon, deep, fruit, cocktail]
    right_button = [winter, coffee, black, salty, hot, fork, shallow, vegetables, beer]

    avokado_buttons = right_button[:9]
    for index in avokado_buttons:
        index.click()
    readMyMind.click()
    expectedResult = "Avocado Benedict"
    recommendation = driver.find_element(By.ID, 'recHeader')
    assert recommendation.text == expectedResult



def test_avocado_1():
    driver = setup_driver()

    get_elements(driver)
    left_button = [summer, tea, white, sweet, sour, spoon, deep, fruit, cocktail]
    right_button = [winter, coffee, black, salty, hot, fork, shallow, vegetables, beer]

    avokado_buttons = right_button[:8] + [left_button[-1]]
    for index in avokado_buttons:
        index.click()
    readMyMind.click()
    expectedResult = "Avocado Benedict"
    recommendation = driver.find_element(By.ID, 'recHeader')
    assert recommendation.text == expectedResult

def test_Strawberry_2():
    driver = setup_driver()

    get_elements(driver)
    left_button = [summer, tea, white, sweet, sour, spoon, deep, fruit, cocktail]
    right_button = [winter, coffee, black, salty, hot, fork, shallow, vegetables, beer]

    avokado_buttons = right_button[:7] + left_button[-2:]
    for index in avokado_buttons:
        index.click()
    readMyMind.click()
    expectedResult = "Strawberry Sundae"
    recommendation = driver.find_element(By.ID, 'recHeader')
    assert recommendation.text == expectedResult

def test_Strawberry_3():
    driver = setup_driver()

    get_elements(driver)
    left_button = [summer, tea, white, sweet, sour, spoon, deep, fruit, cocktail]
    right_button = [winter, coffee, black, salty, hot, fork, shallow, vegetables, beer]

    avokado_buttons = right_button[:6] + left_button[-3:]
    for index in avokado_buttons:
        index.click()
    readMyMind.click()
    expectedResult = "Strawberry Sundae"
    recommendation = driver.find_element(By.ID, 'recHeader')
    assert recommendation.text == expectedResult

def test_Soy_4():
    driver = setup_driver()

    get_elements(driver)
    left_button = [summer, tea, white, sweet, sour, spoon, deep, fruit, cocktail]
    right_button = [winter, coffee, black, salty, hot, fork, shallow, vegetables, beer]

    avokado_buttons = right_button[:5] + left_button[-4:]
    for index in avokado_buttons:
        index.click()
    readMyMind.click()
    expectedResult = "Soy Salmon"
    recommendation = driver.find_element(By.ID, 'recHeader')
    assert recommendation.text == expectedResult

def test_Soy_5():
    driver = setup_driver()

    get_elements(driver)
    left_button = [summer, tea, white, sweet, sour, spoon, deep, fruit, cocktail]
    right_button = [winter, coffee, black, salty, hot, fork, shallow, vegetables, beer]

    avokado_buttons = right_button[:4] + left_button[-5:]
    for index in avokado_buttons:
        index.click()
    readMyMind.click()
    expectedResult = "Soy Salmon"
    recommendation = driver.find_element(By.ID, 'recHeader')
    assert recommendation.text == expectedResult

def test_Culiflower_6():
    driver = setup_driver()

    get_elements(driver)
    left_button = [summer, tea, white, sweet, sour, spoon, deep, fruit, cocktail]
    right_button = [winter, coffee, black, salty, hot, fork, shallow, vegetables, beer]

    avokado_buttons = right_button[:3] + left_button[-6:]
    for index in avokado_buttons:
        index.click()
    readMyMind.click()
    expectedResult = "Culiflower Dipper"
    recommendation = driver.find_element(By.ID, 'recHeader')
    assert recommendation.text == expectedResult

def test_Culiflower_7():
    driver = setup_driver()

    get_elements(driver)
    left_button = [summer, tea, white, sweet, sour, spoon, deep, fruit, cocktail]
    right_button = [winter, coffee, black, salty, hot, fork, shallow, vegetables, beer]

    avokado_buttons = right_button[:2] + left_button[-7:]
    for index in avokado_buttons:
        index.click()
    readMyMind.click()
    expectedResult = "Culiflower Dipper"
    recommendation = driver.find_element(By.ID, 'recHeader')
    assert recommendation.text == expectedResult
def test_Blonde_8():
    driver = setup_driver()

    get_elements(driver)
    left_button = [summer, tea, white, sweet, sour, spoon, deep, fruit, cocktail]
    right_button = [winter, coffee, black, salty, hot, fork, shallow, vegetables, beer]

    avokado_buttons = right_button[:1] + left_button[-8:]
    for index in avokado_buttons:
        index.click()
    readMyMind.click()
    expectedResult = "Blonde"
    recommendation = driver.find_element(By.ID, 'recHeader')
    assert recommendation.text == expectedResult

def test_Blonde_9():
    driver = setup_driver()

    get_elements(driver)
    left_button = [summer, tea, white, sweet, sour, spoon, deep, fruit, cocktail]
    right_button = [winter, coffee, black, salty, hot, fork, shallow, vegetables, beer]

    avokado_buttons = left_button[:9]
    for index in avokado_buttons:
        index.click()
    readMyMind.click()
    expectedResult = "Blonde"
    recommendation = driver.find_element(By.ID, 'recHeader')
    assert recommendation.text == expectedResult
