import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
#sys.path.append("..")
#sys.path.append('/home/tester/Desktop/SeleniumProjektWSB-master/ShopProject/demoPages/main_page.py')
#from demoPages.main_page import MainPage
import os;
parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_directory)
from demoPages.main_page import MainPage

class MainPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://demostore.supersqa.com')
        self.driver.maximize_window()
        self.main_page = MainPage(self.driver)
        

    def test_main_page_header(self):
        actual_text = self.main_page.get_header_text()
        self.assertEqual(self.main_page.expected_text, actual_text)
        

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()