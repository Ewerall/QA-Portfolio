from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import allure

class CartPage:
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step("Открыта ли корзина")
    def is_page_opened(self):
        return "cart.html" in self.driver.current_url
    
    @allure.step("Получить число товаров в корзине")
    def get_product_count(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "cart_item"))
    
    @allure.step("Нажать checkout")
    def click_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
    
    @allure.step("Проверка что перешли на страницу checkout")
    def is_checkout_step_one_opened(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains("checkout-step-one.html")
            )
            return True
        except Exception as e:
            return False