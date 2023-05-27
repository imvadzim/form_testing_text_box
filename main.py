# Ссылка на страницу Text Box: https://demoqa.com/text-box
#
# Форма: Text Box
#
# Задание:
# Написать фреймворк для тестирования этой формы с использованием шаблон проектирования PageObject.
#
# Короткий план:
# Заполнить все поля рандомными данными (можно использовать дополнительные библиотеки).
# Нажать кнопку Submit
# Сравнить введенные данные с полученными данными из поля в котором будут все заполненные данные.
#
# Фреймворк закинуть в репозиторий и дать ссылку.


# Import all necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create BasePage class
class BasePage:
    def __init__(self, driver):
        self.driver = driver

# Create TextBoxPage class
class TextBoxPage(BasePage):
    full_name_input = (By.ID, "userName")
    email_input = (By.ID, "userEmail")
    current_address_input = (By.ID, "currentAddress")
    permanent_address_input = (By.ID, "permanentAddress")
    submit_button = (By.ID, "submit")

    # Create separate methods for filling the form
    def enter_full_name(self, full_name):
        self.driver.find_element(*self.full_name_input).send_keys(full_name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_current_address(self, address):
        self.driver.find_element(*self.current_address_input).send_keys(address)

    def enter_permanent_address(self, address):
        self.driver.find_element(*self.submit_button).click()

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()


# Create submit test
def test_fill_text_boxes(driver):
    url = "https://demoqa.com/text-box"
    driver.get(url)

    text_box_page = TextBoxPage(driver)
    text_box_page.enter_full_name("Lev Leschenko")
    text_box_page.enter_email("lyova.mozhet@yaschik.ru")
    text_box_page.enter_current_address("666 St.Pitersburg")
    text_box_page.enter_permanent_address("Delhi, India")
    text_box_page.click_submit()


# Initialization WebDriver with the Chrome browser
if __name__ == "__main__":
    web_driver = webdriver.Chrome()
    web_driver.implicitly_wait(10)  # Wait for elements to load TODO maybe it should be changed

    # Attempt to fill the form and submit
    try:
        test_fill_text_boxes(web_driver)
        print("Test succeeded!")
    finally:
        web_driver.quit()