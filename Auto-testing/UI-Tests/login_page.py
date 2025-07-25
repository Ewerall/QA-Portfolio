from selenium.webdriver.common.by import By 
import allure

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
    
    @allure.step("Открыть страницу авторизации")
    def open(self):
        self.driver.get(self.url)
        
    @allure.step("Ввести пароль и логин: {username}/{password}")    
    def enter_credentials(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        
    @allure.step("Нажать кнопку логин")    
    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()
        
    @allure.step("Проверить авторизацию")    
    def is_logged_in(self):
        return "inventory" in self.driver.current_url