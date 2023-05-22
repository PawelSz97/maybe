from selenium.webdriver.common.by import By


class CartPage:
        
    def __init__(self, driver):
        self.driver = driver

        self.expected_text = 'Album'
    
    def get_product_name_text(self):
        element = self.driver.find_element_by_link_text('Album')
        actual_text = element.text
        return actual_text