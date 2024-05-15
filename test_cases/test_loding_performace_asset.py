import os

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
import time
import pytest

from page_objects.HomePage import HomePage
from page_objects.LoadingPerformanceAsset import LoadingPerformanceAsset
from utilities.ReadProperties import ReadConfig

from page_objects.LoginPage import LoginPage
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.CustomLogger import LogGen


class Test_001_LoadingPeformanceAsset:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    start_date = ReadConfig.get_loading_performance_asset_start_date()
    end_date = ReadConfig.get_loading_performance_asset_end_date()

    #logger = LogGen.logger()

    def test_loading_performance(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        #self.logger.info("--------click on login button")

        time.sleep(1)
        self.home_page = HomePage(self.driver)

        self.home_page.click_dashboard()
        #self.logger.info("--------click on dashboard button")

        self.home_page.click_loading_performance_asset()
        #self.logger.info("--------click on loading performance(Asset)  button")

        time.sleep(1)

        loading_performance = LoadingPerformanceAsset(self.driver)
        time.sleep(1)
        loading_performance.click_calendar()
        #self.logger.info("--------click on calendar icon")
        time.sleep(1)
        loading_performance.set_date(self.start_date,self.end_date)
        time.sleep(3)


