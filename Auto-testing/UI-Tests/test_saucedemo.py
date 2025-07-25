import pytest
import allure
from login_page import LoginPage
from inventory_page import InventoryPage
from card_page import CartPage
from product_page import ProductPage
from selenium.webdriver.common.by import By

@allure.epic("SauceDemo")
@allure.feature("Аутентификация")
@allure.story("Успешный вход с действительными учетными данными")
def test_valid_login(driver):
    with allure.step("Открыть страницу входа и ввести учетные данные"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_credentials("standard_user", "secret_sauce")
        login_page.click_login()
    
    with allure.step("Проверить успешный вход"):
        assert login_page.is_logged_in()

@allure.epic("SauceDemo")
@allure.feature("Корзина покупок")
@allure.story("Добавление товара в корзину")
def test_add_product_to_cart(driver):
    with allure.step("Выполнить вход в приложение"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_credentials("standard_user", "secret_sauce")
        login_page.click_login()
    
    with allure.step("Добавить товар в корзину"):
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_page_opened()
        inventory_page.add_product_to_cart("Sauce Labs Backpack")
    
    with allure.step("Проверить увеличение счетчика корзины"):
        assert inventory_page.get_cart_badge_count() == 1

@allure.epic("SauceDemo")
@allure.feature("Процесс оформления заказа")
@allure.story("Полный процесс оформления заказа")
def test_checkout_process(driver):
    with allure.step("Войти и добавить товар в корзину"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_credentials("standard_user", "secret_sauce")
        login_page.click_login()

        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart("Sauce Labs Backpack")
        inventory_page.go_to_cart()
    
    with allure.step("Проверить содержимое корзины"):
        cart_page = CartPage(driver)
        assert cart_page.is_page_opened()
        assert cart_page.get_product_count() == 1
    
    with allure.step("Начать оформление заказа"):
        cart_page.click_checkout()
    
    with allure.step("Проверить открытие страницы оформления"):
        assert cart_page.is_checkout_step_one_opened(), "Не удалось перейти на страницу оформления заказа в течение 5 секунд"

@allure.epic("SauceDemo")
@allure.feature("Управление инвентарем")
@allure.story("Сортировка товаров по цене")
def test_product_sorting_low_to_high(driver):
    with allure.step("Выполнить вход в приложение"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_credentials("standard_user", "secret_sauce")
        login_page.click_login()
    
    with allure.step("Отсортировать товары по цене (от низкой к высокой)"):
        inventory_page = InventoryPage(driver)
        inventory_page.sort_products("lohi")
    
    with allure.step("Проверить правильность сортировки"):
        prices = inventory_page.get_product_prices()
        assert prices == sorted(prices), f"Цены не отсортированы по возрастанию: {prices}"

@allure.epic("SauceDemo")
@allure.feature("Детали товара")
@allure.story("Просмотр деталей товара")
def test_product_details(driver):
    with allure.step("Выполнить вход в приложение"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_credentials("standard_user", "secret_sauce")
        login_page.click_login()
    
    with allure.step("Открыть детали товара"):
        inventory_page = InventoryPage(driver)
        inventory_page.click_product("Sauce Labs Backpack")
    
    with allure.step("Проверить страницу деталей товара"):
        product_page = ProductPage(driver)
        assert product_page.is_page_opened(), f"Не перешли на страницу деталей. Текущий URL: {driver.current_url}"
        assert product_page.get_product_name() == "Sauce Labs Backpack"
        assert product_page.get_product_price() == "$29.99"

@allure.epic("SauceDemo")
@allure.feature("Аутентификация")
@allure.story("Вход с недействительными учетными данными")
def test_invalid_login(driver):
    with allure.step("Попытка входа с недействительными учетными данными"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_credentials("invalid_user", "wrong_password")
        login_page.click_login()
    
    with allure.step("Проверить неудачный вход"):
        assert not login_page.is_logged_in()
        error_message = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
        assert "Epic sadface" in error_message