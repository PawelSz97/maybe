import unittest
from selenium import webdriver

class MainPageInit(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://demostore.supersqa.com')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()