import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

ORGANIZER = 'Maja'
ORGANIZER_FULL_NAME = 'Maja '
B_PERSON = 'Nikola'
B_PERSON_FULL_NAME = 'Nikola'
AGE1 = '3'
AGE_REAL = '38'
DATE = '2023-05-23'
REAL_DATE = '2023-05-20'
TIME = '08:20PM'
REAL_TIME = '08:00PM'
PERSON21 = '21+'
PERSON11 = '11-20'
ALLERGIES_YES = 'Yes'
ALLERGIES_MAYBE = 'Maybe'
ALLERGIES_NO = 'No'
ALERGY_TYPES_W = 'Wallnuts'
ALERGY_TYPES_C = 'Chestnuts'


def test_save_metod():
    #no confirmation for type of allergy
    options = webdriver.ChromeOptions()
    options.add_argument("-incognito")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('http://10.15.1.204:3000/')
    driver.maximize_window()
    problemOrganize = driver.find_element(By.CSS_SELECTOR, "#ftco-nav > ul > li:nth-child(2) > a")
    problemOrganize.click()
    organizerName = driver.find_element(By.CLASS_NAME, 'form-control.org')
    birthdayName = driver.find_element(By.CSS_SELECTOR, "input[class='form-control bp']")
    age = driver.find_element(By.ID, "age")
    when = driver.find_element(By.ID, "date")
    time_party = driver.find_element(By.ID, "time")
    persons21 = driver.find_element(By.CSS_SELECTOR, "#persons > option:nth-child(5)")
    persons11 = driver.find_element(By.CSS_SELECTOR, "#persons > option:nth-child(4)")
    alergiesNo = driver.find_element(By.ID, "alg_n")
    alergiesMaybe = driver.find_element(By.ID, "alg_m")
    alergiesYes = driver.find_element(By.ID, "alg_y")
    wallnutsAlergies = driver.find_element(By.ID, "alg1")
    chestnutsAlergies = driver.find_element(By.ID, "alg2")
    btnOrganize = driver.find_element(By.CSS_SELECTOR, "body > section.ftco-section.ftco-no-pt.ftco-no-pb > div > div > div.col-md-7.ftco-animate.makereservation.p-4.p-md-5.fadeInUp.ftco-animated > form > div > div.col-md-12.mt-3 > div > p > a")

    organizerName.send_keys(ORGANIZER)
    birthdayName.send_keys(B_PERSON)
    age.send_keys(AGE1)
    for i in range(5):
        when.send_keys(Keys.UP)
    when.send_keys(Keys.RIGHT)
    for i in range(23):
        when.send_keys(Keys.UP)
    when.send_keys(Keys.RIGHT)
    when.send_keys(Keys.UP)
    time_party.send_keys(TIME)
    persons21.click()
    alergiesMaybe.click()
    btnOrganize.click()

    confirmOrganizerName = driver.find_element(By.ID, "orr")
    confirmBirthdayName = driver.find_element(By.ID, "cbr")
    confirmAge = driver.find_element(By.ID, "agr")
    confirmWhen = driver.find_element(By.ID, "dtr")
    confirmTime = driver.find_element(By.ID, "tmr")
    dt = datetime.strptime(TIME, '%I:%M%p')
    TIME_24h = dt.strftime('%H:%M')
    confirmPersons = driver.find_element(By.ID, "gur")
    confirmAlergies = driver.find_element(By.ID, "alr")

    assert confirmOrganizerName.text == ORGANIZER
    assert confirmBirthdayName.text == B_PERSON
    assert confirmAge.text == AGE1
    assert confirmWhen.text == DATE
    assert confirmTime.text == TIME_24h
    assert confirmPersons.text == PERSON21
    assert confirmAlergies.text == ALLERGIES_MAYBE

def test_passed_local_storage_changes():
    options = webdriver.ChromeOptions()
    options.add_argument("-incognito")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('http://10.15.1.204:3000/')
    driver.maximize_window()
    problemOrganize = driver.find_element(By.CSS_SELECTOR, "#ftco-nav > ul > li:nth-child(2) > a")
    problemOrganize.click()
    organizerName = driver.find_element(By.CLASS_NAME, 'form-control.org')
    birthdayName = driver.find_element(By.CSS_SELECTOR, "input[class='form-control bp']")
    age = driver.find_element(By.ID, "age")
    when = driver.find_element(By.ID, "date")
    time_party = driver.find_element(By.ID, "time")
    persons21 = driver.find_element(By.CSS_SELECTOR, "#persons > option:nth-child(5)")
    persons11 = driver.find_element(By.CSS_SELECTOR, "#persons > option:nth-child(4)")
    alergiesNo = driver.find_element(By.ID, "alg_n")
    alergiesMaybe = driver.find_element(By.ID, "alg_m")
    alergiesYes = driver.find_element(By.ID, "alg_y")
    wallnutsAlergies = driver.find_element(By.ID, "alg1")
    chestnutsAlergies = driver.find_element(By.ID, "alg2")
    btnOrganize = driver.find_element(By.CSS_SELECTOR, "body > section.ftco-section.ftco-no-pt.ftco-no-pb > div > div > div.col-md-7.ftco-animate.makereservation.p-4.p-md-5.fadeInUp.ftco-animated > form > div > div.col-md-12.mt-3 > div > p > a")

    organizerName.send_keys(ORGANIZER)
    birthdayName.send_keys(B_PERSON)
    age.send_keys(AGE1)
    for i in range(5):
        when.send_keys(Keys.UP)
    when.send_keys(Keys.RIGHT)
    for i in range(23):
        when.send_keys(Keys.UP)
    when.send_keys(Keys.RIGHT)
    when.send_keys(Keys.UP)
    time_party.send_keys(TIME)
    persons21.click()
    alergiesMaybe.click()
    wallnutsAlergies.click()

    storage_org = driver.execute_script(f'return localStorage.getItem("Organizer")')
    assert storage_org == ORGANIZER
    storage_bp = driver.execute_script(f'return localStorage.getItem("Birthday_Person")')
    assert storage_bp == B_PERSON
    storage_age = driver.execute_script(f'return localStorage.getItem("Age")')
    assert storage_age == AGE1
    storage_date = driver.execute_script(f'return localStorage.getItem("Date")')
    assert storage_date == DATE
    storage_time = driver.execute_script(f'return localStorage.getItem("Time")')
    dt = datetime.strptime(TIME, '%I:%M%p')
    TIME_24h = dt.strftime('%H:%M')
    assert storage_time == TIME_24h
    storage_pers = driver.execute_script(f'return localStorage.getItem("Number_Of_People")')
    assert storage_pers == PERSON21
    storage_allergies = driver.execute_script(f'return localStorage.getItem("alergy")')
    assert storage_allergies == ALLERGIES_MAYBE
    storage_which_allergies = driver.execute_script(f'return localStorage.getItem("alergies")')
    assert storage_which_allergies == ALERGY_TYPES_W

def test_failed_local_storage_changes():
    options = webdriver.ChromeOptions()
    options.add_argument("-incognito")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('http://10.15.1.204:3000/')
    driver.maximize_window()
    problemOrganize = driver.find_element(By.CSS_SELECTOR, "#ftco-nav > ul > li:nth-child(2) > a")
    problemOrganize.click()
    organizerName = driver.find_element(By.CLASS_NAME, 'form-control.org')
    birthdayName = driver.find_element(By.CSS_SELECTOR, "input[class='form-control bp']")
    age = driver.find_element(By.ID, "age")
    when = driver.find_element(By.ID, "date")
    time_party = driver.find_element(By.ID, "time")
    persons21 = driver.find_element(By.CSS_SELECTOR, "#persons > option:nth-child(5)")
    persons11 = driver.find_element(By.CSS_SELECTOR, "#persons > option:nth-child(4)")
    alergiesNo = driver.find_element(By.ID, "alg_n")
    alergiesMaybe = driver.find_element(By.ID, "alg_m")
    alergiesYes = driver.find_element(By.ID, "alg_y")
    wallnutsAlergies = driver.find_element(By.ID, "alg1")
    chestnutsAlergies = driver.find_element(By.ID, "alg2")
    btnOrganize = driver.find_element(By.CSS_SELECTOR, "body > section.ftco-section.ftco-no-pt.ftco-no-pb > div > div > div.col-md-7.ftco-animate.makereservation.p-4.p-md-5.fadeInUp.ftco-animated > form > div > div.col-md-12.mt-3 > div > p > a")

    organizerName.send_keys(ORGANIZER)
    birthdayName.send_keys(B_PERSON)
    age.send_keys(AGE1)
    for i in range(5):
        when.send_keys(Keys.UP)
    when.send_keys(Keys.RIGHT)
    for i in range(23):
        when.send_keys(Keys.UP)
    when.send_keys(Keys.RIGHT)
    when.send_keys(Keys.UP)
    time_party.send_keys(TIME)
    persons21.click()
    alergiesMaybe.click()
    wallnutsAlergies.click()

    storage_org = driver.execute_script(f'return localStorage.getItem("Organizer")')
    assert storage_org == ORGANIZER
    storage_bp = driver.execute_script(f'return localStorage.getItem("Birthday_Person")')
    assert storage_bp == B_PERSON
    storage_age = driver.execute_script(f'return localStorage.getItem("Age")')
    assert storage_age == AGE1
    storage_date = driver.execute_script(f'return localStorage.getItem("Date")')
    assert storage_date == DATE
    storage_time = driver.execute_script(f'return localStorage.getItem("Time")')
    dt = datetime.strptime(TIME, '%I:%M%p')
    TIME_24h = dt.strftime('%H:%M')
    assert storage_time == TIME_24h
    storage_pers = driver.execute_script(f'return localStorage.getItem("Number_Of_People")')
    assert storage_pers == PERSON21
    storage_allergies = driver.execute_script(f'return localStorage.getItem("alergy")')
    assert storage_allergies == ALLERGIES_MAYBE
    storage_which_allergies = driver.execute_script(f'return localStorage.getItem("alergies")')
    assert storage_which_allergies == ALERGY_TYPES_W

    organizerName.clear()
    organizerName.send_keys(ORGANIZER_FULL_NAME)
    birthdayName.clear()
    birthdayName.send_keys(B_PERSON_FULL_NAME)
    age.clear()
    age.send_keys(AGE_REAL)
    when.send_keys(Keys.RIGHT)
    for i in range(3):
        when.send_keys(Keys.DOWN)
    time_party.clear()
    time_party.send_keys(REAL_TIME)
    persons11.click()
    alergiesNo.click()

    storage_org = driver.execute_script(f'return localStorage.getItem("Organizer")')
    assert storage_org == ORGANIZER_FULL_NAME
    storage_bp = driver.execute_script(f'return localStorage.getItem("Birthday_Person")')
    assert storage_bp == B_PERSON_FULL_NAME
    storage_age = driver.execute_script(f'return localStorage.getItem("Age")')
    assert storage_age == AGE_REAL
    storage_date = driver.execute_script(f'return localStorage.getItem("Date")')
    assert storage_date == REAL_DATE
    storage_time = driver.execute_script(f'return localStorage.getItem("Time")')
    dt = datetime.strptime(REAL_TIME, '%I:%M%p')
    TIME_24h = dt.strftime('%H:%M')
    assert storage_time == TIME_24h
    storage_pers = driver.execute_script(f'return localStorage.getItem("Number_Of_People")')
    assert storage_pers == PERSON11
    storage_allergies = driver.execute_script(f'return localStorage.getItem("alergy")')
    assert storage_allergies == ALLERGIES_NO
    storage_which_allergies = driver.execute_script(f'return localStorage.getItem("alergies")')
    assert storage_which_allergies != ALERGY_TYPES_W

def test_failed_local_storage_changes_duple_click_alergies():
    options = webdriver.ChromeOptions()
    options.add_argument("-incognito")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('http://10.15.1.204:3000/')
    driver.maximize_window()
    problemOrganize = driver.find_element(By.CSS_SELECTOR, "#ftco-nav > ul > li:nth-child(2) > a")
    problemOrganize.click()
    organizerName = driver.find_element(By.CLASS_NAME, 'form-control.org')
    birthdayName = driver.find_element(By.CSS_SELECTOR, "input[class='form-control bp']")
    age = driver.find_element(By.ID, "age")
    when = driver.find_element(By.ID, "date")
    time_party = driver.find_element(By.ID, "time")
    persons21 = driver.find_element(By.CSS_SELECTOR, "#persons > option:nth-child(5)")
    persons11 = driver.find_element(By.CSS_SELECTOR, "#persons > option:nth-child(4)")
    alergiesNo = driver.find_element(By.ID, "alg_n")
    alergiesMaybe = driver.find_element(By.ID, "alg_m")
    alergiesYes = driver.find_element(By.ID, "alg_y")
    wallnutsAlergies = driver.find_element(By.ID, "alg1")
    chestnutsAlergies = driver.find_element(By.ID, "alg2")
    btnOrganize = driver.find_element(By.CSS_SELECTOR, "body > section.ftco-section.ftco-no-pt.ftco-no-pb > div > div > div.col-md-7.ftco-animate.makereservation.p-4.p-md-5.fadeInUp.ftco-animated > form > div > div.col-md-12.mt-3 > div > p > a")

    organizerName.send_keys(ORGANIZER)
    birthdayName.send_keys(B_PERSON)
    age.send_keys(AGE1)
    for i in range(5):
        when.send_keys(Keys.UP)
    when.send_keys(Keys.RIGHT)
    for i in range(23):
        when.send_keys(Keys.UP)
    when.send_keys(Keys.RIGHT)
    when.send_keys(Keys.UP)
    time_party.send_keys(TIME)
    persons21.click()
    alergiesMaybe.click()
    wallnutsAlergies.click()

    storage_org = driver.execute_script(f'return localStorage.getItem("Organizer")')
    assert storage_org == ORGANIZER
    storage_bp = driver.execute_script(f'return localStorage.getItem("Birthday_Person")')
    assert storage_bp == B_PERSON
    storage_age = driver.execute_script(f'return localStorage.getItem("Age")')
    assert storage_age == AGE1
    storage_date = driver.execute_script(f'return localStorage.getItem("Date")')
    assert storage_date == DATE
    storage_time = driver.execute_script(f'return localStorage.getItem("Time")')
    dt = datetime.strptime(TIME, '%I:%M%p')
    TIME_24h = dt.strftime('%H:%M')
    assert storage_time == TIME_24h
    storage_pers = driver.execute_script(f'return localStorage.getItem("Number_Of_People")')
    assert storage_pers == PERSON21
    storage_allergies = driver.execute_script(f'return localStorage.getItem("alergy")')
    assert storage_allergies == ALLERGIES_MAYBE
    storage_which_allergies = driver.execute_script(f'return localStorage.getItem("alergies")')
    assert storage_which_allergies == ALERGY_TYPES_W

    organizerName.clear()
    organizerName.send_keys(ORGANIZER_FULL_NAME)
    birthdayName.clear()
    birthdayName.send_keys(B_PERSON_FULL_NAME)
    age.clear()
    age.send_keys(AGE_REAL)
    when.send_keys(Keys.RIGHT)
    for i in range(3):
        when.send_keys(Keys.DOWN)
    time_party.clear()
    time_party.send_keys(REAL_TIME)
    persons11.click()
    alergiesYes.click()
    for i in range(5):
        wallnutsAlergies.click()
    chestnutsAlergies.click()
    storage_org = driver.execute_script(f'return localStorage.getItem("Organizer")')
    assert storage_org == ORGANIZER_FULL_NAME
    storage_bp = driver.execute_script(f'return localStorage.getItem("Birthday_Person")')
    assert storage_bp == B_PERSON_FULL_NAME
    storage_age = driver.execute_script(f'return localStorage.getItem("Age")')
    assert storage_age == AGE_REAL
    storage_date = driver.execute_script(f'return localStorage.getItem("Date")')
    assert storage_date == REAL_DATE
    storage_time = driver.execute_script(f'return localStorage.getItem("Time")')
    dt = datetime.strptime(REAL_TIME, '%I:%M%p')
    TIME_24h = dt.strftime('%H:%M')
    assert storage_time == TIME_24h
    storage_pers = driver.execute_script(f'return localStorage.getItem("Number_Of_People")')
    assert storage_pers == PERSON11
    storage_allergies = driver.execute_script(f'return localStorage.getItem("alergy")')
    assert storage_allergies == ALLERGIES_YES
    storage_which_allergies = driver.execute_script(f'return localStorage.getItem("alergies")')
    assert storage_which_allergies == ALERGY_TYPES_C