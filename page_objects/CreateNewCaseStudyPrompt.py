import time
from telnetlib import EC

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.CustomLogger import LogGen
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreateCaseStudyPrompt:
    textbox_case_study_name=(By.XPATH,"//input[@id='caseStudyCreationDialog-nameEditor-input']")
    textbox_case_study_description=(By.XPATH,"//textarea[@id='caseStudyCreationDialog-descriptionEditor-input']")
    button_next_page=(By.XPATH,"//div[contains(text(),'NEXT')]")

    def __init__(self,driver):
        self.driver=driver

    def enter_case_study_name(self,name):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(CreateCaseStudyPrompt.textbox_case_study_name)).send_keys(name)
        #self.driver.find_element(*CreateCaseStudyPrompt.textbox_case_study_name).send_keys(name)

    def enter_case_study_description(self, desc):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(CreateCaseStudyPrompt.textbox_case_study_description)).send_keys(desc)
        #self.driver.find_element(*CreateCaseStudyPrompt.textbox_case_study_description).send_keys(desc)

    def click_on_next_page(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(CreateCaseStudyPrompt.button_next_page)).click()
        #self.driver.find_element(*CreateCaseStudyPrompt.button_next_page).click()



