import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from main_project.base.base_class import Base


class Main_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #locators
    filt_1 = '//*[@id="catalog"]/div[1]/div[5]/a/a'
    filt_2 = '/html/body/div[2]/div[1]/div[2]/a[2]'
    filt_3 = '/html/body/div[2]/div[1]/div[2]/a[1]'
    check_filt_1 = '/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[4]/div/div/div[3]/label[3]'
    check_filt_2 = '/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[4]/div/div/div[3]/label[4]'
    accept = '/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div/button[1]'
    product_1 = '/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[4]/button[2]'
    product_2 = '/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]/div[4]/button[2]'
    product_3 = '/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[3]/div[4]/button[2]'

    cart = '//*[@id="header-search"]/div/div[3]/div[1]/div/a'



    #Getters

    def get_filt_1(self):
        return self.driver.find_element(By.XPATH, self.filt_1)

    def get_filt_2(self):
        return self.driver.find_element(By.XPATH, self.filt_2)

    def get_filt_3(self):
        return self.driver.find_element(By.XPATH, self.filt_3)

    def get_check_filt_1(self):
        return self.driver.find_element(By.XPATH, self.check_filt_1)

    def get_check_filt_2(self):
        return self.driver.find_element(By.XPATH, self.check_filt_2)

    def get_accept(self):
        return self.driver.find_element(By.XPATH, self.accept)

    def get_product_1(self):
        return self.driver.find_element(By.XPATH, self.product_1)

    def get_product_2(self):
        return self.driver.find_element(By.XPATH, self.product_2)

    def get_product_3(self):
        return self.driver.find_element(By.XPATH, self.product_3)

    def get_cart(self):
        return self.driver.find_element(By.XPATH, self.cart)


    #Actions

    def click_filt_1(self):
        self.get_filt_1().click()
        print("select_filt_1 ")

    def click_filt_2(self):
        self.get_filt_2().click()
        print("select_filt_2 ")

    def click_filt_3(self):
        self.get_filt_3().click()
        print("select_filt_3 ")

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, 300)")

    def click_check_filt_1(self):
        action = ActionChains(self.driver)
        action.move_by_offset(10, 20)  # 10px to the right, 300px to bottom
        action.perform()
        self.get_check_filt_1().click()
        print("check_filt_1 ")

    def click_check_filt_2(self):
        action = ActionChains(self.driver)
        action.move_by_offset(10, 20)  # 10px to the right, 20px to bottom
        action.perform()
        self.get_check_filt_2().click()
        print("check_filt_2 ")

    def click_accept(self):
        action = ActionChains(self.driver)
        button = self.get_accept()
        action.move_to_element(button).perform()
        self.get_accept().click()
        print("accept button ")

    def click_product_1(self):
        action = ActionChains(self.driver)
        button = self.get_product_1()
        action.move_to_element(button).perform()
        button.click()
        print("select product 1 ")

    def click_product_2(self):
        action = ActionChains(self.driver)
        button = self.get_product_2()
        action.move_to_element(button).perform()
        button.click()
        print("select product 2 ")

    def click_product_3(self):
        action = ActionChains(self.driver)
        button = self.get_product_3()
        action.move_to_element(button).perform()
        button.click()
        print("select product 3 ")

    def click_cart(self):
        action = ActionChains(self.driver)
        button = self.get_cart()
        action.move_to_element(button).perform()
        button.click()
        print("click cart ")




    def select_filt_1(self):
        self.get_current_url()
        self.click_filt_1()

    def select_filt_2(self):
        self.get_current_url()
        self.click_filt_2()

    def select_filt_3(self):
        self.get_current_url()
        self.click_filt_3()

    def select_check_filt_1(self):
        self.get_current_url()
        self.click_check_filt_1()

    def select_check_filt_2(self):
        self.get_current_url()
        self.click_check_filt_2()

    def select_accept(self):
        self.get_current_url()
        self.click_accept()

    def select_product_1(self):
        self.get_current_url()
        self.click_product_1()

    def select_product_2(self):
        self.get_current_url()
        self.click_product_2()

    def select_product_3(self):
        self.get_current_url()
        self.click_product_3()

    def select_cart(self):
        self.get_current_url()
        self.click_cart()

    def assertion(self, http):
        assert self.driver.current_url == http
        print("Assert good")

