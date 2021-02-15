from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import credential
import time

username = credential.psuser
password = credential.pspass

driver = webdriver.Chrome(executable_path='D:/Automation/chromedriver.exe')
driver.get('https://wordpress.com/log-in')

user_input = driver.find_element_by_css_selector('#usernameOrEmail')
user_input.send_keys(username)

driver.find_element_by_css_selector('#primary > div > main > div > div > form > div.card.login__form > div.login__form-action > button').click()

password_input = driver.find_element_by_xpath('//*[@id="password"]')
time.sleep(3)
ActionChains(driver).move_to_element(password_input).send_keys(password).perform()
time.sleep(3)

driver.find_element_by_css_selector('#primary > div > main > div > div > form > div.card.login__form > div.login__form-action > button').click()
