from selenium import webdriver
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
driver.implicitly_wait(20)
password_input.send_keys(password)

driver.find_element_by_css_selector('#primary > div > main > div > div > form > div.card.login__form > div.login__form-action > button').click()
