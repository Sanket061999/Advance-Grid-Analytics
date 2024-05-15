import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.CustomLogger import LogGen

class LoginPage:
    #static variable or class varible
    textbox_username=(By.ID,"usernameField-input")
    textbox_password=(By.ID,"passwordField-input")
    button_login=(By.XPATH,"//div[@class='LCXO6YC-s-r'][normalize-space()='LOGIN']")
    button_change_password=(By.XPATH,"//div[contains(text(),'CHANGE PASSWORD')]")
    logger=LogGen.logger()


    def __init__(self, driver):
        self.driver=driver

    def set_username(self,username):
        ele=WebDriverWait(self.driver,2).until(EC.presence_of_element_located(LoginPage.textbox_username))
        ele.send_keys(username)
        #self.driver.find_element(*LoginPage.textbox_username).clear()
        #self.driver.find_element(*LoginPage.textbox_username).send_keys(username)

    def set_password(self,password):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(LoginPage.textbox_password)).clear()
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(LoginPage.textbox_password)).send_keys(password)

        #self.driver.find_element(*LoginPage.textbox_password).clear()
        #self.driver.find_element(*LoginPage.textbox_password).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(LoginPage.button_login)).click()
        #self.driver.find_element(*LoginPage.button_login).click()

    def click_change_password(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(LoginPage.button_change_password)).click()
        #self.driver.find_element(*LoginPage.button_change_password).click()


