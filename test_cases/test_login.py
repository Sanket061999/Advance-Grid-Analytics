import os

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
import time
import pytest
from utilities.ReadProperties import ReadConfig

from page_objects.LoginPage import LoginPage
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.CustomLogger import LogGen


class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.logger()


    def test_login(self, setup):
        print("<<<<<<<<<<<<<<<<<<<<<<<<<")
        print(os.path)
        self.logger.info("===========verifying login page title test ===========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()


        act_title = self.driver.title
        self.logger.info("===========Captured login page title===========")
        if act_title == "Advanced Grid Analytics":
            self.logger.info("=========== title matched===========")
            assert True
            self.driver.close()
        else:
            self.logger.error("===========title did not matched of login page===========")
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            self.driver.close()
            assert False




