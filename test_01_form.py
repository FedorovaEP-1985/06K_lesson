from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Функция для запуска теста
def test_form_validation():
    # Инициализация драйвера
    driver = webdriver.Chrome()


# Открытие страницы
    driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    print("страница загружена")

# Явное ожидание загрузки формы
    WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'input[name="first-name"]'))
        )

    # Заполнение формы
    driver.find_element(
            By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
    driver.find_element(
            By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
    driver.find_element(
            By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(
            By.CSS_SELECTOR, 'input[name="e-mail"]'
            ).send_keys("test@skypro.com")
    driver.find_element(
            By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
    # Поле Zip code оставляем пустым
    driver.find_element(
            By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
    driver.find_element(
            By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
    driver.find_element(
            By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
    driver.find_element(
            By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")

    # Нажатие кнопки Submit
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Явное ожидание появления подсветки полей
    WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#first-name"))
        )

    # Проверка, цвета полей
    assert "alert py-2 alert-danger" in driver.find_element(
        By.CSS_SELECTOR, "#zip-code"
        ).get_attribute("class")
    assert "alert py-2 alert-success" in driver.find_element(
        By.CSS_SELECTOR, "#first-name"
        ).get_attribute("class")
    assert "alert py-2 alert-success" in driver.find_element(
        By.CSS_SELECTOR, "#last-name"
        ).get_attribute("class")
    assert "alert py-2 alert-success" in driver.find_element(
        By.CSS_SELECTOR, "#address"
        ).get_attribute("class")
    assert "alert py-2 alert-success" in driver.find_element(
        By.CSS_SELECTOR, "#city"
        ).get_attribute("class")
    assert "alert py-2 alert-success" in driver.find_element(
        By.CSS_SELECTOR, "#country"
        ).get_attribute("class")
    assert "alert py-2 alert-success" in driver.find_element(
        By.CSS_SELECTOR, "#e-mail"
        ).get_attribute("class")
    assert "alert py-2 alert-success" in driver.find_element(
        By.CSS_SELECTOR, "#phone"
        ).get_attribute("class")
    assert "alert py-2 alert-success" in driver.find_element(
        By.CSS_SELECTOR, "#job-position"
        ).get_attribute("class")
    assert "alert py-2 alert-success" in driver.find_element(
        By.CSS_SELECTOR, "#company"
        ).get_attribute("class")

    driver.quit()
    print("страница закрыта")