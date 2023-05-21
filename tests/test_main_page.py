import unittest
from pages.init_method_page import MainPageInit
from pages import main_page 


class MainPageTest(MainPageInit):

    def assert_main_page_title(self):
        mp = main_page(self.driver)
        mp.assert_main_page_title() # veryfi is main page loaded succesfully

if __name__ == "__main__":
    unittest.main()