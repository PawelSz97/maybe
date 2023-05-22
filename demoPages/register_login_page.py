from selenium.webdriver.common.by import By


class Login_register:


    def __init__(self, driver):
        self.driver = driver

        self.password_selector = '#password',
        self.username_login_email_selector = '#username'
        self.register_password_selector = '#reg_password'
        self.register_email_selector = '#reg_email'
        self.password = 'Ala123#@!'
        self.not_existing_login_email = 'asdasdw2@wp.pl'
        self.existing_email = 'wsx@wp.pl'

    
    def enter_login_password(self):
        login_password = self.driver.find_element(By.CSS_SELECTOR, self.password_selector)
        login_password.send_keys(self.password)

        
    def enter_not_existing_login_email(self):
        enter_not_existing_login_email = self.driver.find_element(By.CSS_SELECTOR, self.username_login_email_selector)
        enter_not_existing_login_email.send_keys(self.not_existing_login_email)

    def enter_login_email(self):
        login_email = self.driver.find_element(By.CSS_SELECTOR, self.username_login_email_selector)
        login_email.send_keys(self.existing_email) 


    def enter_register_password(self):
        register_password = self.driver.find_element(By.CSS_SELECTOR, self.register_password_selector )
        register_password.send_keys(self.password) 

    def enter_register_email(self):
        register_email = self.driver.find_element(By.CSS_SELECTOR, self.register_email_selector )
        register_email.send_keys(self.existing_email)





