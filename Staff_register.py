import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Car_Test4(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\Program Files\chromedriver.exe')

    def test_login(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("http://samp786.pythonanywhere.com/")
        x=driver.find_element_by_xpath('//*[@id="navbarText"]/li[2]').click()
        y=driver.find_element_by_xpath('//*[@id="navbarText"]/li[2]/div').click()
        time.sleep(0.5)
        register_email_address = driver.find_element_by_id("exampleInputEmail1")
        register_email_address.send_keys("raviv@unomaha.edu")
        register_email_pwd = driver.find_element_by_id("exampleInputPassword1")
        register_email_pwd.send_keys("maverick1a")
        register_confirm_pwd = driver.find_element_by_id("exampleInputPassword2")
        register_confirm_pwd.send_keys("maverick1a")
        time.sleep(3.0)
        driver.find_element_by_xpath('/html/body/div/div/div/form/div[4]/button').click()
        time.sleep(3.0)
        try:
            # attempt to find the plus button - if found, logged in
            driver.find_element_by_xpath('//*[@id="navbarText"]/li[2]/a')
            assert True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
