from selenium.webdriver.common.by import By 

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        
    def open(self):
        self.driver.get(self.url)
        
    def enter_credentials(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        
    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()
        
    def is_logged_in(self):
        return "inventory" in self.driver.current_url