import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from main_project.base.base_class import Base


class Main_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #locators
    filt_1 = '//*[@id="catalog"]/div[1]/div[5]/a/a'
    filt_2 = '/html/body/div[2]/div[1]/div[2]/a[2]'
    filt_3 = '/html/body/div[2]/div[1]/div[2]/a[1]'
    check_filt_1 = '/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[4]/div/div/div[3]/label[4]/span[2]'
    check_filt_2 = '/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[4]/div/div/div[3]/label[5]/span[2]'
    accept = '/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div/button[1]'
    product_1 = '/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[4]/button[2]'
    product_2 = '/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]/div[4]/button[2]'
    product_3 = '/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[3]/div[4]/button[2]'
    # select_product_2 = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
    # select_product_3 = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    cart = '//*[@id="header-search"]/div/div[3]/div[1]/div/a'
    # menu = '//button[@id="react-burger-menu-btn"]'


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

    #
    # def get_select_product_2(self):
    #     return self.driver.find_element(By.XPATH, self.select_product_2)
    #
    # def get_select_product_3(self):
    #     return self.driver.find_element(By.XPATH, self.select_product_3)
    #
    # def get_cart(self):
    #     return self.driver.find_element(By.XPATH, self.cart)
    #
    # def get_menu(self):
    #     return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.menu)))
    #
    # def get_link_about(self):
    #     return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.link_about)))


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

    def click_check_filt_1(self):
        action = ActionChains(self.driver)
        action.move_by_offset(10, 200)  # 10px to the right, 20px to bottom
        action.perform()
        self.get_check_filt_1().click()
        print("check_filt_1 ")

    def click_check_filt_2(self):
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








    # def select_product(self):
    #     self.get_current_url()
    #     self.click_product_1()
    #     self.click_cart()
    #
    # def select_products_2(self):
    #     self.get_current_url()
    #     self.click_product_2()
    #     self.click_cart()
    #
    # def select_products_3(self):
    #     self.get_current_url()
    #     self.click_product_3()
    #     self.click_cart()
    #
    # def select_menu_about(self):
    #     self.get_current_url()
    #     self.click_menu()
    #     self.click_link_about()
    #     self.assert_url('https://saucelabs.com/')



    # def authorization(self, login_name, login_password):
    #
    #     user_name = self.driver.find_element(By.XPATH, '//input[@id="user-name"]')
    #     user_name.send_keys(login_name)
    #     password = self.driver.find_element(By.XPATH, '//input[@id="password"]')
    #     password.send_keys(login_password)
    #     button_login = self.driver.find_element(By.XPATH, '//input[@id="login-button"]')
    #     button_login.click()

    def assertion(self, http):
        assert self.driver.current_url == http
        print("Assert good")

    def assertion_for_locked(self):
        assert self.driver.current_url == "https://www.saucedemo.com/"
        print("Assert good")

    def logout(self):
        button_menu = self.driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
        button_menu.click()
        time.sleep(1)
        button_logout = self.driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]')
        button_logout.click()
