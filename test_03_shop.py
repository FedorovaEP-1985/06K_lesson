from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shopping():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    driver.find_element(
        By.CSS_SELECTOR, "#user-name"
    ).send_keys("standard_user")
    driver.find_element(
        By.CSS_SELECTOR, "#password"
    ).send_keys("secret_sauce")
    driver.find_element(
        By.CSS_SELECTOR, "#login-button").click()

    # Добавление товаров в корзину
    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]
    for item in items:
        driver.find_element(
            By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button"
        ).click()

    # Переход в корзину
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    # Нажатие Checkout
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    # Заполнение формы
    driver.find_element(
        By.CSS_SELECTOR, "#first-name"
    ).send_keys("Иван")
    (driver.find_element
     (By.CSS_SELECTOR, "#last-name"
      ).send_keys("Петров"))
    driver.find_element(
        By.CSS_SELECTOR, "#postal-code"
    ).send_keys("123456")
    driver.find_element(
        By.CSS_SELECTOR, "#continue"
    ).click()

    # Проверка итоговой суммы
    total = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, ".summary_total_label")
        )
    ).text
    assert total == "Total: $58.29", (f"Итоговая сумма не равна $58.29. "
                                      f"Фактическая сумма: {total}")

    driver.quit()
