from selenium.webdriver.common.by import By
import allure

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        
    @allure.step("Открыта ли страница продукта")    
    def is_page_opened(self):
        return "inventory-item.html" in self.driver.current_url and "id=" in self.driver.current_url
        
    @allure.step("Получить имя продукта")    
    def get_product_name(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_details_name").text #can make it in constructor attribute
        
    @allure.step("Получить цену продукта")    
    def get_product_price(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_details_price").text #can make it in constructor attribute