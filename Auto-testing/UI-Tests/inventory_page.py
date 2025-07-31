from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        #here we save locators like atributes class (cool)
        self.inventory_container = "inventory_container"
        self.shopping_cart_badge = "shopping_cart_badge"
        self.cart_link = "shopping_cart_link"
        self.product_sort_container = "product_sort_container"
        
    @allure.step("Проверить открыта ли страница товаров")
    def is_page_opened(self):
        return "inventory.html" in self.driver.current_url
    
    @allure.step("Добавить продукт '{product_name}' в корзину")
    def add_product_to_cart(self, product_name):
        # "Sauce Labs Backpack" -> "sauce-labs-backpack"
        product_id = product_name.lower().replace(" ", "-")
        add_button_id = f"add-to-cart-{product_id}"
        self.driver.find_element(By.ID, add_button_id).click() 
    
    @allure.step("Получить количество товаров в корзине")
    def get_cart_badge_count(self):
        try:
            return int(self.driver.find_element(By.CLASS_NAME, self.shopping_cart_badge).text)
        except:
            return 0
        
    @allure.step("Открыть корзину")
    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, self.cart_link).click()
    
    @allure.step("Отсортировать продукты по параметру '{sort_option}'")
    def sort_products(self, sort_option):
        """Сортирует продукты по указанному параметру"""
        # find list-dropdown element 
        sort_dropdown_element = self.driver.find_element(By.CLASS_NAME, self.product_sort_container)
        
        # make select object for dropdown list
        sort_dropdown = Select(sort_dropdown_element)
        
        # value atribute
        sort_dropdown.select_by_value(sort_option)
        
        # wait for sort end
        WebDriverWait(self.driver, 5).until(
            EC.staleness_of(sort_dropdown_element)
        )
    
    @allure.step("Получить цены всех продуктов")
    def get_product_prices(self):
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices = [float(element.text.replace("$", "")) for element in price_elements]
        return prices
    
    @allure.step("Кликнуть по продукту '{product_name}'")
    def click_product(self, product_name, timeout=10):
        try:
            # wait for element with product name
            product_element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'inventory_item_name') and contains(., '{product_name}')]"))
            )
            product_element.click()
            return True
        except TimeoutException:
            return False
        except Exception as e:
            return False
