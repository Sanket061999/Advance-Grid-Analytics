from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    button_dashboard=(By.XPATH,"//div[contains(text(),'Dashboard')]")   #//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]
    button_voltage_performance=(By.XPATH,"//span[normalize-space()='Voltage Performance']")
    button_loading_performance_asset=(By.XPATH,"//span[normalize-space()='Loading Performance (Asset)']")
    button_administration=(By.XPATH,"//div[@id='viewSelector-view-Administration']")
    button_create_case_study=(By.XPATH,"//span[normalize-space()='Create Case Study']")


    def __init__(self, driver):
        self.driver=driver

    def click_dashboard(self):
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located(HomePage.button_dashboard)).click()
        #self.driver.find_element(*HomePage.button_dashboard).click()

    def click_voltage_performance(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(HomePage.button_voltage_performance)).click()
        #self.driver.find_element(*HomePage.button_voltage_performance).click()

    def click_loading_performance_asset(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(HomePage.button_loading_performance_asset)).click()
        #self.driver.find_element(*HomePage.button_loading_performance_asset).click()

    def click_administration(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(HomePage.button_administration)).click()
        #self.driver.find_element(*HomePage.button_administration).click()

    def click_create_case_study(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(HomePage.button_create_case_study)).click()
        #self.driver.find_element(*HomePage.button_create_case_study).click()




