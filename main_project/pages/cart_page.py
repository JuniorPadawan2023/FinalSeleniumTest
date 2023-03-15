from selenium.webdriver.common.by import By

from main_project.base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    checkout_button = '//*[@id="buy-btn-main"]'

    # Getters

    def get_checkout_button(self):
        return self.driver.find_element(By.XPATH, self.checkout_button)

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("click checkout button ")

    # Methods

    def product_confirm(self):
        self.get_current_url()
        self.click_checkout_button()
