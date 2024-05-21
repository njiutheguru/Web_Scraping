from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import datetime
import os
import json



CHROME_DRIVER_PATH = os.path.join(os.getcwd(), "chromedriver")
OP = webdriver.ChromeOptions()
OP.add_argument('--headless')
Driver = webdriver.Chrome()

def login():
    with open('config.json') as configfile:
        credentials = json.load(configfile)
        time.sleep(2)
        Driver.find_element(By.LINK_TEXT, value="Log in").click()
        time.sleep(2)
        username = Driver.find_element(By.CSS_SELECTOR, value="input[name='username']")
        username.clear()
        username.send_keys(credentials["USERNAME"])
        time.sleep(2)
        Driver.find_element(By.ID, "login-submit").click()
        time.sleep(2)
        password = Driver.find_element(By.ID, "password")
        time.sleep(2)
        password.send_keys(credentials["PASSWORD"])
        time.sleep(2)
        Driver.find_element(By.ID, "login-submit").click()
        time.sleep(2)

def add_new_task():
    Driver.find_element(By.LINK_TEXT, "Robot board").click()
    # time.sleep(7)
    # add_task = Driver.find_element(By.XPATH,value="//div [@class='Y44OETtkQ7R6r5']")
    # add_task.click()
    time.sleep(3)

def screenshotpage():
    time.sleep(2)
    date_str = datetime.today().strftime("%y-%m-%d")
    save_path = f"{date_str}.png"
    Driver.get_screenshot_as_file(save_path)

def execute_the_main_program():
   
    Driver.get("https://trello.com")
    login()
    add_new_task()
    screenshotpage()
    input("Press any key to exit from the chrome browser..")
    Driver.close()
    


def main():
    browser = webdriver.Firefox()

    browser.get('http://www.yahoo.com')
    assert 'Yahoo' in browser.title

    elem = browser.find_element(By.NAME, 'p')  # Find the search box
    elem.send_keys('seleniumhq' + Keys.RETURN)

    browser.quit()
    
if __name__ == "__main__":
    # main()
    execute_the_main_program()
    print("function main in exection ")


