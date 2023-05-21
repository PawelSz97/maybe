from pages import main_page
from selenium.webdriver.common.by import By
from selenium import webdriver

password_selector = '#password',
username_login_email_selector = '#username'
register_password_selector = '#reg_password'
register_email_selector = '#reg_email'
password = 'Ala123#@!'
not_existing_login_email = 'asdasdw2@wp.pl'
existing_email = 'wsx@wp.pl'


class Login_register:


    def __init__(self, driver):
        self.driver = driver

    
    def enter_login_password(self):
        login_password = self.driver.find_element(By.CSS_SELECTOR, password_selector)
        login_password.send_keys(password)

        
    def enter_not_existing_login_email(self):
        enter_not_existing_login_email = self.driver.find_element(By.CSS_SELECTOR, username_login_email_selector)
        enter_not_existing_login_email.send_keys(not_existing_login_email)

    def enter_login_email(self):
        login_email = self.driver.find_element(By.CSS_SELECTOR, username_login_email_selector)
        login_email.send_keys(existing_email) 


    def enter_register_password(self):
        register_password = self.driver.find_element(By.CSS_SELECTOR, register_password_selector )
        register_password.send_keys(password) 

    def enter_register_email(self):
        register_email = self.driver.find_element(By.CSS_SELECTOR, register_email_selector )
        register_email.send_keys(existing_email)





