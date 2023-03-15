import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from main_project.pages.main_page import Main_page
from main_project.pages.cart_page import Cart_page
from main_project.pages.client_info_page import  Client_info_page

class Test_1:


    def test_authorization(set_up, set_group):
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option("detach", True)
        chrome_options = Options()
        options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\Resource\\chromedriver.exe',
                                  chrome_options=options)
        base_url = 'https://www.dns-shop.ru/'
        driver.get(base_url)


        print("start test 1")


        mp = Main_page(driver) #main page class
        cp = Cart_page(driver)
        cip = Client_info_page(driver)
        mp.select_filt_1()
        mp.select_filt_2()
        mp.select_filt_3()
        mp.assertion('https://www.dns-shop.ru/catalog/17a8932c16404e77/personalnye-kompyutery/')
        time.sleep(3)
        mp.select_check_filt_1()
        time.sleep(2)
        mp.select_check_filt_2()
        mp.select_accept()
        time.sleep(2)
        mp.select_product_1()
        time.sleep(1)
        mp.select_product_2()
        time.sleep(1)
        mp.select_product_3()
        time.sleep(1)
        mp.select_cart()
        mp.assertion('https://www.dns-shop.ru/cart/')
        cp.product_confirm()
        time.sleep(5)
        cip.send_user_phone("89224530585")







