import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient
import time

client = MongoClient('127.0.0.1', 27017)
db = client['mails_collection']
mailbox = db.mailbox


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

binary_google_driver_file = 'HW5\chromedriver.exe'

driver = webdriver.Chrome(binary_google_driver_file, options=options)
driver.get('https://account.mail.ru/login')

time.sleep(1)
username = driver.find_element_by_name('username')
username.send_keys('study.ai_172@mail.ru')
username.send_keys(Keys.ENTER)

time.sleep(1)
password = driver.find_element_by_name('password')
password.send_keys('NextPassword172!?')
password.send_keys(Keys.ENTER)

all_mail_links = []
mails_checker = []
wait = WebDriverWait(driver, 10)
# Собираем ссылки
for i in range(100):
    mails_check = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, 'llc__container')))
    if mails_check:
        mails = driver.find_elements_by_class_name(
            'js-letter-list-item')
        for mail in mails:
            mail_link = mail.get_attribute('href')
            all_mail_links.append(mail_link)
        actions = ActionChains(driver)
        actions.move_to_element(mails[-1])
        actions.perform()
    # проверка, что список измненился с последней итерации
    if mails_checker == all_mail_links:
        break
    else:
        mails_checker == all_mail_links


for link in all_mail_links:
    driver.get(link)
    mails_check = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, 'letter-contact')))
    if mails_check:
        from_who = driver.find_element_by_class_name(
            'letter-contact').get_attribute('title')
        date = driver.find_element_by_class_name('letter__date').text
        subject = driver.find_element_by_class_name('thread__subject').text
        text = driver.find_element_by_xpath(
            "//div[@class='letter-body__body']/descendant::*").text
        mail_info = {
            'form': from_who,
            'date': date,
            'subject': subject,
            'text': text,
        }
        mailbox.update_one({'text': mail_info['text']}, {
            '$set': mail_info}, upsert=True)
