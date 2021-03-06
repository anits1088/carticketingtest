import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pytest


class Car_Test8(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\Program Files\chromedriver.exe')

    def test_login(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("http://samp786.pythonanywhere.com/")
        driver.find_element_by_xpath('//*[@id="navbarDropdownMenuLink"]').click()
        driver.find_element_by_xpath('//*[@id="navbarText"]/li[1]/div/a[2]').click()
        time.sleep(0.5)
        login_email_address = driver.find_element_by_id("exampleInputEmail1")
        login_email_address.send_keys("xyz@gmail.com")
        login_email_pwd = driver.find_element_by_id("exampleInputPassword1")
        login_email_pwd.send_keys("Sampath@3")
        time.sleep(3.0)
        driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/button').click()
        time.sleep(3.0)
        driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div[2]/a').click()
        time.sleep(3.0)
        driver.find_element_by_xpath('/html/body/div/div[2]/a[2]/span').click()
        time.sleep(3.0)










def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
