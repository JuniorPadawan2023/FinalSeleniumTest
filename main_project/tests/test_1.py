import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from main_project.pages.main_page import Main_page
from main_project.pages.cart_page import Cart_page
from main_project.pages.client_info_page import  Client_info_page
from selenium.webdriver.support import expected_conditions as EC
class Test_1: #dns shop buy products test


    def test_scenario(set_up, set_group):
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option("detach", True)
        chrome_options = Options()
        options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(executable_path='./Resources/chromedriver.exe',
                                  chrome_options=options)
        base_url = 'https://www.dns-shop.ru/'
        driver.get(base_url)


        print("start test 1")


        mp = Main_page(driver)   #main page class
        cp = Cart_page(driver)  #cart page class
        cip = Client_info_page(driver)  #client info page class
        WebDriverWait(driver, timeout=10)
        mp.hover_user()     #hover to user profile button
        mp.click_user_button()
        mp.click_enter_with_password()
        mp.mail_locator_send_keys()
        mp.mail_pass_locator_send_keys()
        WebDriverWait(driver, timeout=20)
        mp.click_enter_button()
        WebDriverWait(driver, timeout=20)
        mp.select_filt_1()     #click filter 1 open computer page
        mp.select_filt_2()     #click filter 2 open components page
        mp.select_filt_3()     #click filter 3 open personal computer
        mp.assertion('https://www.dns-shop.ru/catalog/17a8932c16404e77/personalnye-kompyutery/')
        #time.sleep(2)
        WebDriverWait(driver, timeout=10)
        mp.scroll_down()
        WebDriverWait(driver, timeout=10)
        #time.sleep(3)
        mp.select_check_filt_1()    #click check_box_filter
        WebDriverWait(driver, timeout=10)
        #time.sleep(2)
        mp.select_check_filt_2()    #click check_box_filter 2
        WebDriverWait(driver, timeout=10)
        #time.sleep(2)
        mp.select_accept()          #accept search
        for i in range (10):
            try:
                WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[4]/button[2]')))
                mp.select_product_1()
                break
            except BaseException:
                print('error')

        mp.select_product_1()       #click select product 1
        WebDriverWait(driver, timeout=10)

        mp.select_product_2()       #click select product 2
        WebDriverWait(driver, timeout=10)

        mp.select_product_3()       #click select product 3

        WebDriverWait(driver, timeout=10)
        mp.select_cart()            #click cart
        mp.assertion('https://www.dns-shop.ru/cart/')
        cp.product_confirm()
        WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH,'//input[@class="base-ui-input-row__input_Gc5"]')))
        #time.sleep(5)
        cip.send_user_phone("89224530585")







