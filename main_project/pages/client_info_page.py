from selenium.webdriver.common.by import By

from main_project.base.base_class import Base


class Client_info_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # user info

    user_phone = "89224530585"


    # locators

    phone_input = '//input[@class="base-ui-input-row__input_Gc5"]'
    # Getters

    def get_phone_input(self):
        return self.driver.find_element(By.XPATH, self.phone_input)


    # Actions

    def send_user_phone(self, user_phone):
        self.get_phone_input().send_keys(user_phone)
        print("send user phone info ")

