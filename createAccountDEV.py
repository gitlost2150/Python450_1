from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

chrome_options = Options()  
chrome_options.add_argument("--headless")  

randPref = random.randint(10000, 99999)
css_for_checkbox = "#registration-form > form > div.row.row-md.row-middle.row-gutter.group-buttons-indent > div > div > div.col-xs-2.col-md-1 > div > label"
css_for_home = '#desktop-header > nav > a:nth-child(1)'
driver = webdriver.Chrome()

driver.get("https:///signup")


def field_fill(idName, valueAdd):
    elem = driver.find_element_by_id(idName)
    elem.send_keys(valueAdd)
    if idName == "userName":
        f = open('resultsDEV.txt', 'a')
        f.write(str(valueAdd) + '\n')
        f.close()


def click_button(idName):
    elem = driver.find_element_by_id(idName)
    elem.click()


def drop_down_select(value2):
    all_options = driver.find_elements_by_tag_name("option")
    for option in all_options:
        if option.text == value2:
            option.click()


field_fill("firstName", "mustangFirstName")
field_fill("lastName", "mustangLastName")

drop_down_select("Miss")
drop_down_select("15")
drop_down_select("Jan")
drop_down_select("1995")

field_fill("postcodeUk", "321321")
field_fill("address", "mustangAdress")
field_fill("city", "mustangCity")
field_fill("mobile", "7777777")
field_fill("email", "test@test.com")
field_fill("emailVerify", "test@test.com")

click_button("nextStep")

field_fill("userName", ("mustangUsername_" + str(randPref)))
field_fill("userPassword", "123123")
field_fill("passwordVerify", "123123")

drop_down_select("No Limit")

checkbox = driver.find_element_by_css_selector(css_for_checkbox)
checkbox.click()

submitFin = driver.find_element_by_id("submit")
submitFin.click()


def waiter_for_class(className):
    wait = WebDriverWait(driver, 30)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, className)))
    element.click()


waiter_for_class('redirect-button')
waiter_for_class('btn-secondary')

elem = driver.find_element_by_css_selector(css_for_home)
elem.click()

driver.close()
