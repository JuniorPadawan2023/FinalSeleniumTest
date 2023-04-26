from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from main_project.base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    checkout_button = '//button[@class="base-ui-button-v2_medium base-ui-button-v2_brand base-ui-button-v2_ico-none base-ui-button-v2 buy-button"]'

    # Getters

    def get_checkout_button(self):
        return self.driver.find_element(By.XPATH, self.checkout_button)

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("click checkout button ")

    # Methods

    def product_confirm(self):
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.checkout_button))
            )
            self.get_current_url()
            self.click_checkout_button()

