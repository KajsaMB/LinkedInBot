from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv("local.env")
SELENIUM_DRIVE_PATH = os.getenv("DRIVE_PATH")
LINKEDIN_JOB_URL = os.getenv("JOB_URL")

service = Service(executable_path=SELENIUM-DRIVE-PATH)
options = webdriver.ChromeOptions()
options.add_argument("--kiosk")
driver = webdriver.Chrome(service=service, options=options)

driver.get(LINKEDIN-JOB-URL)

your_user = os.getenv("YOUR_USER")
your_pass = os.getenv("YOUR_PASS")
sign_in = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in.click()
sleep(1)
username = driver.find_element(by=By.ID, value="username")
username.send_keys(f"{your_user}")
password = driver.find_element(by=By.ID, value="password")
password.send_keys(f"{your_pass}")

log_in = driver.find_element(by=By.CLASS_NAME, value="from__button--floating")
log_in.click()
sleep(3)

close_message_bar = driver.find_element(by=By.XPATH, value="/html/body/div[6]/aside/div[1]/header/div[3]/button[2]")
close_message_bar.click()

sleep(1)
jobs = driver.find_elements(by=By.CLASS_NAME, value="jobs-search-results__list-item")

for job in jobs:
    sleep(1)
    try:
        job.click()
    except ElementClickInterceptedException:
        close_popup = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/div/div/button")
        close_popup.click()
    finally:
        job.click()
        sleep(1)
    job_save = driver.find_element(by=By.CLASS_NAME, value="jobs-save-button")
    job_save_text = driver.find_element(by=By.CSS_SELECTOR, value="button.jobs-save-button span")
    if job_save_text.text == "Save":
        job_save.click()
        sleep(1)
        try:
            close_popup = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/div/div/button")
            close_popup.click()
            sleep(1)
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass
    job_detail = driver.find_element(by=By.CLASS_NAME, value="jobs-search__job-details")
    job_detail.click()
    html = driver.find_element(by=By.CSS_SELECTOR, value="html")
    html.send_keys(Keys.END)
    sleep(2)
    try:
        follow = driver.find_element(by=By.CLASS_NAME, value="follow")
        if follow.text == "Follow":
            follow.click()
            try:
                close_popup = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/div/div/button")
                close_popup.click()
                sleep(1)
            except NoSuchElementException:
                pass
    except NoSuchElementException:
        pass

