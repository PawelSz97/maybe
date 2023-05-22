from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver
    
        self.main_page_header_selector = 'h1.woocommerce-products-header__title' # is equal to: "Shop"
        self.page_title = 'Shop'
        self.header_selector = 'h1.woocommerce-products-header__title'
        self.page_url = 'http://demostore.supersqa.com'
        self.expected_text = 'Shop'

    def get_header_text(self):
        header_element = self.driver.find_element(By.CSS_SELECTOR, self.header_selector)
        return header_element.text
        
    def open_my_account(self):
        my_account_btn = self.driver.find_element(By.LINK_TEXT, 'My account')
        my_account_btn.click()

    def add_album_to_cart(self):
        add_album_to_cart = self.driver.find_element(By.CSS_SELECTOR,'ul.products li:nth-child(3) .button')
        add_album_to_cart.click()
    
    def open_shopping_cart(self):
        shopping_cart = self.driver.find_element(By.CSS_SELECTOR,'#site-header-cart li .cart-contents')
        shopping_cart.click()

    def enter_value_into_search_bar(self):
        search_bar = self.driver.find_element(By.CSS_SELECTOR,'#woocommerce-product-search-field-0')
        search_bar.send_keys('Cap').submit()

    