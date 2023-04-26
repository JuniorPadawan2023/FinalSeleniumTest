import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main_project.base.base_class import Base


class Main_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    mail = 'ivan.homyakov2017@yandex.ru'
    mail_password = 'Password123'

    #locators
    user = '//div[@class="user-profile__login"]'
    user_button = '//div[@class="user-profile__guest"]/button'
    enter_with_password = '//div[@class="base-button-container base-button-container_blue"]'
    mail_locator = '//input[@class="base-ui-input-row__input base-ui-input-row__input_with-icon"]'
    mail_pass_locator = '//input[@type="password"]'
    enter_button = '//button[@class="base-ui-button-v2_big base-ui-button-v2_brand base-ui-button-v2_ico-none base-ui-button-v2"]'
    filt_1 = '//*[@id="catalog"]/div[1]/div[5]/a/a'
    filt_2 = '//a[@href="/catalog/e33ed1823ba77fd7/kompyutery-i-po/"]'
    filt_3 = '//a[@class="subcategory__item ui-link ui-link_blue"]'
    check_filt_1 = '(//label[@class="ui-checkbox ui-checkbox_list"])[3]'
    check_filt_2 = '(//label[@class="ui-checkbox ui-checkbox_list"])[4]'
    accept = '//button[@class="button-ui button-ui_brand left-filters__button"]'
    product_1 = '(//button[@class="buy-btn"])[1]'
    product_2 = '(//button[@class="buy-btn"])[2]'
    product_3 = '(//button[@class="buy-btn"])[3]'

    cart = '//*[@id="header-search"]/div/div[3]/div[1]/div/a'



    #Getters
    def get_user(self):
        return self.driver.find_element(By.XPATH, self.user)

    def get_user_button(self):
        return self.driver.find_element(By.XPATH, self.user_button)

    def get_enter_with_password(self):
        return self.driver.find_element(By.XPATH, self.enter_with_password)

    def get_mail_locator(self):
        return self.driver.find_element(By.XPATH, self.mail_locator)

    def get_mail_pass_locator(self):
        return self.driver.find_element(By.XPATH, self.mail_pass_locator)

    def get_enter_button(self):
        return self.driver.find_element(By.XPATH, self.enter_button)

    def get_filt_1(self):
        return self.driver.find_element(By.XPATH, self.filt_1)

    def get_filt_2(self):
        return self.driver.find_element(By.XPATH, self.filt_2)

    def get_filt_3(self):
        return self.driver.find_element(By.XPATH, self.filt_3)

    def get_check_filt_1(self):
        return self.driver.find_elements(By.XPATH, self.check_filt_1)[2]

    def get_check_filt_2(self):
        return self.driver.find_elements(By.XPATH, self.check_filt_2)[3]

    def get_accept(self):
        return self.driver.find_element(By.XPATH, self.accept)

    def get_product_1(self):
        return self.driver.find_elements(By.CLASS_NAME, "buy-btn")[0]

    def get_product_2(self):
        return self.driver.find_elements(By.CLASS_NAME, "buy-btn")[1]

    def get_product_3(self):
        return self.driver.find_elements(By.CLASS_NAME, "buy-btn")[2]

    def get_cart(self):
        return self.driver.find_element(By.XPATH, self.cart)


    #Actions
    def hover_user(self):
        hover = ActionChains(self.driver).move_to_element(self.get_user())
        hover.perform()
        print("hover to user ")

    def click_user_button(self):
        self.get_user_button().click()
        print("click user button")

    def click_enter_with_password(self):
        self.get_enter_with_password().click()
        print("click user button")

    def mail_locator_send_keys(self):
        self.get_mail_locator().send_keys('ivan.homyakov2017@yandex.ru')
        print("send keys to mail")

    def mail_pass_locator_send_keys(self):
        self.get_mail_pass_locator().send_keys('Password123')
        print("send keys to mail password")

    def click_enter_button(self):
        self.get_enter_button().click()
        print("click enter button")

    def click_filt_1(self):
        try:
            self.get_filt_1().click()
            print("select_filt_1 ")
            WebDriverWait(self.driver, timeout=10)
        except:
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
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.check_filt_1))
        )
        element.click()
        print("check_filt_1 ")

    def click_check_filt_2(self):
        action = ActionChains(self.driver)
        action.move_by_offset(10, 20)  # 10px to the right, 20px to bottom
        action.perform()
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.check_filt_2))
        )
        element.click()
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

