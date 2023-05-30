# Import all necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker

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
    output = (By.ID, "output")

    # Create separate methods for interacting with elements
    def enter_full_name(self, full_name):
        self.driver.find_element(*self.full_name_input).send_keys(full_name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_current_address(self, address):
        self.driver.find_element(*self.current_address_input).send_keys(address)

    def enter_permanent_address(self, address):
        self.driver.find_element(*self.permanent_address_input).send_keys(address)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def check_the_output(self, data):
        output = self.driver.find_element(*self.output).text.split("\n")
        assert output[0] == 'Name:' + data[0]  # todo do we need replace here also?
        assert output[1] == 'Email:' + data[1]  # todo do we need replace here also?
        assert output[2] == 'Current Address :' + data[2].replace('\n', ' ')  # todo 'Current Address:'
        assert output[3] == 'Permananet Address :' + data[3].replace('\n', ' ')  # todo 'Permanent Address:'

# Create submit test
def test_fill_text_boxes(driver):
    url = "https://demoqa.com/text-box"
    driver.get(url)
    fake = Faker()

    data = [fake.name(),
            fake.email(),
            fake.address(),
            fake.address()]

    text_box_page = TextBoxPage(driver)
    text_box_page.enter_full_name(data[0])
    text_box_page.enter_email(data[1])
    text_box_page.enter_current_address(data[2])
    text_box_page.enter_permanent_address(data[3])
    text_box_page.click_submit()

    # compare the data with the input
    text_box_page.check_the_output(data)
    # todo think how to organize tests
    # todo create a proper structure
    # todo implement pytest
    # todo generate different tests with proper test strategy
    # todo other improvements

# Initialization WebDriver with the Chrome browser
if __name__ == "__main__":
    web_driver = webdriver.Chrome()
    # open the browser window in full screen
    web_driver.maximize_window()
    # wait for elements to load
    web_driver.implicitly_wait(10)  # todo change to explicit: wait for a proper page appearance

    # an attempt to fill the form and submit
    try:
        test_fill_text_boxes(web_driver)
        print("Test succeeded!")
    finally:
        web_driver.quit()
