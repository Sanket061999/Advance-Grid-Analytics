from utilities.CustomLogger import LogGen
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

from utilities.CustomLogger import LogGen
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateCaseStudyByJurisdictionPrompt:
    button_select_all_jurisdictions = (By.ID, "jurisdictionSelector-dualList-addAllButton")
    button_select_all_substations = (By.ID, "caseStudyCreationDialog-substationSelector-dualList-addAllButton")
    button_select_all_feeders = (By.ID, "caseStudyCreationDialog-feederSelector-dualList-addAllButton")
    button_save = (By.ID, "ID-DIALOG-BUTTON-SAVE")

    def __init__(self, driver):
        self.driver = driver

    def click_on_select_all_jurisdictions(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(CreateCaseStudyByJurisdictionPrompt.button_select_all_jurisdictions)).click()
        #self.driver.find_element(*CreateCaseStudyByJurisdictionPrompt.button_select_all_jurisdictions).click()



    def click_on_select_all_substations(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(CreateCaseStudyByJurisdictionPrompt.button_select_all_substations)).click()
        #self.driver.find_element(*CreateCaseStudyByJurisdictionPrompt.button_select_all_substations).click()

    def click_on_select_all_feeders(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(CreateCaseStudyByJurisdictionPrompt.button_select_all_feeders)).click()
        #self.driver.find_element(*CreateCaseStudyByJurisdictionPrompt.button_select_all_feeders).click()

    def click_on_save(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(CreateCaseStudyByJurisdictionPrompt.button_save)).click()
        #self.driver.find_element(*CreateCaseStudyByJurisdictionPrompt.button_save).click()
