from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateCaseStudyPanel:
    add_new_case_study_icon = (By.XPATH,"//body[1]/div[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]")
    system_planning_case_study = (By.XPATH, "//span[@class='LCXO6YC-C-b'][normalize-space()='System Planning']")
    transformer_loss_of_life_case_study = (By.XPATH, "//span[@class='LCXO6YC-C-b'][normalize-space()='Transformer Loss Of Life']")
    voltage_bellwether_case_study=(By.XPATH,"//span[@class='LCXO6YC-C-b'][normalize-space()='Voltage Bellwether']")
    fci_placement_case_study=(By.XPATH,"//span[@class='LCXO6YC-C-b'][normalize-space()='FCI Placement']")
    switch_placement_case_study=(By.XPATH,"//span[@class='LCXO6YC-C-b'][normalize-space()='Switch Placement']")
    list_of_case_studies = (By.XPATH, "//*[@id='caseSelectionPanel-grid']/div[2]/div/table/tbody[2]/tr/td[1]/div/span")


    def __init__(self, driver):
        self.driver = driver

    def click_on_create_case_study_icon(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(CreateCaseStudyPanel.add_new_case_study_icon)).click()
        #self.driver.find_element(*CreateCaseStudyPanel.add_new_case_study_icon).click()

    def click_on_fci_placement(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(CreateCaseStudyPanel.fci_placement_case_study)).click()
        #self.driver.find_element(*CreateCaseStudyPanel.fci_placement_case_study).click()

    def click_on_system_planning(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(CreateCaseStudyPanel.system_planning_case_study)).click()
        #self.driver.find_element(*CreateCaseStudyPanel.system_planning_case_study).click()

    def click_on_switch_placement(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(CreateCaseStudyPanel.switch_placement_case_study)).click()
        #self.driver.find_element(*CreateCaseStudyPanel.switch_placement_case_study).click()

    def click_on_transformer_loss_of_life(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(CreateCaseStudyPanel.transformer_loss_of_life_case_study)).click()
        #self.driver.find_element(*CreateCaseStudyPanel.transformer_loss_of_life_case_study).click()

    def click_on_voltage_bellwether(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(CreateCaseStudyPanel.voltage_bellwether_case_study)).click()
        #self.driver.find_element(*CreateCaseStudyPanel.voltage_bellwether_case_study).click()

    def get_case_study_name(self):
        case_study_elements=WebDriverWait(self.driver,2).until(EC.presence_of_all_elements_located(CreateCaseStudyPanel.list_of_case_studies))
        #case_study_elements = self.driver.find_elements(*CreateCaseStudyPanel.list_of_case_studies)
        name_of_case_study = []
        for i in range(1, len(case_study_elements) + 1):
            row = "//*[@id='caseSelectionPanel-grid']/div[2]/div/table/tbody[2]/tr[" + str(i) + "]/td[1]/div/span"
            val = self.driver.find_element(By.XPATH, row).text
            name_of_case_study.append(val)
        return name_of_case_study

    def get_case_study_status(self):
        case_study_elements=WebDriverWait(self.driver,2).until(EC.presence_of_all_elements_located(CreateCaseStudyPanel.list_of_case_studies))
        #case_study_elements = self.driver.find_elements(*CreateCaseStudyPanel.list_of_case_studies)
        status_of_case_study = []
        for i in range(1, len(case_study_elements) + 1):
            status = "//*[@id='caseSelectionPanel-grid']/div[2]/div/table/tbody[2]/tr[" + str(i) + "]/td[3]/div/span"
            status_value = self.driver.find_element(By.XPATH, status).text
            status_of_case_study.append(status_value)
            print(status_of_case_study)
        return status_of_case_study

    def get_case_study_type(self):
        case_study_elements=WebDriverWait(self.driver,2).until(EC.presence_of_all_elements_located(CreateCaseStudyPanel.list_of_case_studies))
        #case_study_elements = self.driver.find_elements(*CreateCaseStudyPanel.list_of_case_studies)
        type_of_case_study = []
        for i in range(1, len(case_study_elements) + 1):
            status = "//*[@id='caseSelectionPanel-grid']/div[2]/div/table/tbody[2]/tr[" + str(i) + "]/td[2]/div/span"
            status_value = self.driver.find_element(By.XPATH, status).text
            type_of_case_study.append(status_value)
            print(type_of_case_study)
        return type_of_case_study
