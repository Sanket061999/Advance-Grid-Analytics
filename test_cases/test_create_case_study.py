import os
from random import randint

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time
import pytest

from page_objects.CreateCaseStudyJurisdictionPrompt import CreateCaseStudyByJurisdictionPrompt
from page_objects.CreateNewCaseStudyPrompt import CreateCaseStudyPrompt

from page_objects.HomePage import HomePage
from page_objects.LoadingPerformanceAsset import LoadingPerformanceAsset
from utilities import RandomStringGenerator
from utilities.ReadProperties import ReadConfig

from page_objects.LoginPage import LoginPage
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.CustomLogger import LogGen
from page_objects.CreateCaseStudyPanel import CreateCaseStudyPanel


class Test_001_CreateCaseStudy:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logger()
    randomValue = RandomStringGenerator.RandomValueGenerator.random_generator()

    @pytest.mark.systemplanning
    def test_create_system_planning_case_study(self, setup):
        self.logger.info("----Starting the system planning case study creation test")
        descOfCaseStudy = "This is Test for create system planning case study"
        nameOfCaseStudy = "systemPlanning" + self.randomValue

        self.driver = setup
        self.driver.get(self.baseURL)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        self.logger.info("--------click on login button")
        # self.driver.execute_script("document.body.style.zoom = '0.97'")
        homepage = HomePage(self.driver)
        homepage.click_dashboard()
        self.logger.info("--------click on dashboard button")
        homepage.click_create_case_study()
        self.logger.info("--------click on create case study button")
        create_case_study = CreateCaseStudyPanel(self.driver)
        create_case_study.click_on_create_case_study_icon()
        self.logger.info("--------click on create case study icon")
        create_case_study.click_on_system_planning()
        self.logger.info("--------click on system planning case study")
        create_system_planning_case_study = CreateCaseStudyPrompt(self.driver)
        create_system_planning_case_study.enter_case_study_name(nameOfCaseStudy)
        self.logger.info("--------While creation entered the name of case study")
        create_system_planning_case_study.enter_case_study_description(descOfCaseStudy)
        self.logger.info("--------While creation entered the description of case study")

        # taking screenshot
        self.driver.save_screenshot("./Screenshots/CreateCaseStudy/SystemPlanning/" + "creation_page.png")

        create_system_planning_case_study.click_on_next_page()
        self.logger.info("--------While creation clicked on next page")

        create_case_study_by_jurisdiction = CreateCaseStudyByJurisdictionPrompt(self.driver)
        self.logger.info("--------While creation entered the description of case study")
        create_case_study_by_jurisdiction.click_on_select_all_jurisdictions()
        self.logger.info("--------click on selection of all jurisdiction of case study")
        create_case_study_by_jurisdiction.click_on_select_all_substations()
        self.logger.info("--------While creation entered the substation of case study")
        #create_case_study_by_jurisdiction.click_on_select_all_feeders()
        # time.sleep(2)

        # act = ActionChains(self.driver)
        # act.key_down(Keys.CONTROL).send_keys(Keys.SUBTRACT).send_keys(Keys.SUBTRACT).send_keys(Keys.SUBTRACT).perform()
        time.sleep(5)
        create_case_study_by_jurisdiction.click_on_save()

        self.logger.info("--------Click on saved")
        self.driver.save_screenshot("./Screenshots/CreateCaseStudy/SystemPlanning/" + "createdPage.png")
        names = create_case_study.get_case_study_name()
        self.logger.info("---------Captured all the name of all created case study")
        status = create_case_study.get_case_study_status()
        self.logger.info("---------Captured all the status of all created case study")
        types = create_case_study.get_case_study_type()
        self.logger.info("---------Captured all the types of all created case study")
        flag = False
        for i in range(0, len(names)):
            if names[i] == nameOfCaseStudy and types[i] == "System Planning":
                flag = True
                break
        assert flag
        self.logger.info("Passed")
        # self.logger.info("name of newly created case study is matched")
        # if status[i] == "Ready" and types[i] == "System Planning":
        #     self.logger.info("status and the type of the newly created case study is matched")
        #     assert True
        #     self.logger.log("Case study creation is successful")
        #     break
        # else:
        #     self.logger.error("status and the type of the newly created case study is not matched")
        #     assert False

    def test_transformer_loss_of_life_case_study(self, setup):
        self.logger.info("----Starting the transformer loss of life case study creation test")
        descOfCaseStudy = "This is Test for create transformer loss of life case study"
        nameOfCaseStudy = "transformerCaseStudy" + self.randomValue

        self.driver = setup
        self.driver.get(self.baseURL)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        self.logger.info("--------click on login button")
        # self.driver.execute_script("document.body.style.zoom = '0.97'")
        homepage = HomePage(self.driver)
        homepage.click_dashboard()
        self.logger.info("--------click on dashboard button")
        homepage.click_create_case_study()
        self.logger.info("--------click on create case study button")
        create_case_study = CreateCaseStudyPanel(self.driver)
        create_case_study.click_on_create_case_study_icon()
        self.logger.info("--------click on create case study icon")
        create_case_study.click_on_transformer_loss_of_life()
        self.logger.info("--------click on transformer loss of life case study")
        create_transformer_loss_of_life_case_study = CreateCaseStudyPrompt(self.driver)
        create_transformer_loss_of_life_case_study.enter_case_study_name(nameOfCaseStudy)
        self.logger.info("--------While creation entered the name of case study")
        create_transformer_loss_of_life_case_study.enter_case_study_description(descOfCaseStudy)
        self.logger.info("--------While creation entered the description of case study")
        self.driver.save_screenshot("./Screenshots/CreateCaseStudy/TransformerLossOfLife/" + "creation_page.png")
        create_transformer_loss_of_life_case_study.click_on_next_page()
        self.logger.info("--------While creation clicked on next page")
        create_case_study_by_jurisdiction = CreateCaseStudyByJurisdictionPrompt(self.driver)
        self.logger.info("--------While creation entered the description of case study")
        create_case_study_by_jurisdiction.click_on_select_all_jurisdictions()
        self.logger.info("--------click on selection of all jurisdiction of case study")
        create_case_study_by_jurisdiction.click_on_select_all_substations()
        self.logger.info("--------While creation entered the substation of case study")
        #create_case_study_by_jurisdiction.click_on_select_all_feeders()
        # time.sleep(2)
        time.sleep(5)
        create_case_study_by_jurisdiction.click_on_save()
        self.logger.info("--------Click on saved")
        self.driver.save_screenshot("./Screenshots/CreateCaseStudy/TransformerLossOfLife/" + "created_page.png")
        names = create_case_study.get_case_study_name()
        self.logger.info("---------Captured all the name of all created case study")
        status = create_case_study.get_case_study_status()
        self.logger.info("---------Captured all the status of all created case study")
        types = create_case_study.get_case_study_type()
        self.logger.info("---------Captured all the types of all created case study")
        flag = False
        for i in range(0, len(names)):
            if names[i] == nameOfCaseStudy and types[i] == "Transformer Loss Of Life":
                flag = True
                break
        assert flag

        # self.logger.info("name of newly created case study is matched")
        # if status[i] == "Ready" and types[i] == "System Planning":
        #     self.logger.info("status and the type of the newly created case study is matched")
        #     assert True
        #     self.logger.log("Case study creation is successful")
        #     break
        # else:
        #     self.logger.error("status and the type of the newly created case study is not matched")
        #     assert False

    def test_voltage_bellwether_case_study(self, setup):
        self.logger.info("----Starting the voltage bellwether case study creation test")
        descOfCaseStudy = "This is Test for create voltage bellwether case study"
        nameOfCaseStudy = "voltageBellwether" + self.randomValue
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        self.logger.info("--------click on login button")
        # self.driver.execute_script("document.body.style.zoom = '0.97'")
        homepage = HomePage(self.driver)
        homepage.click_dashboard()
        self.logger.info("--------click on dashboard button")
        homepage.click_create_case_study()
        self.logger.info("--------click on create case study button")

        create_case_study = CreateCaseStudyPanel(self.driver)
        create_case_study.click_on_create_case_study_icon()
        self.logger.info("--------click on create case study icon")
        create_case_study.click_on_voltage_bellwether()
        self.logger.info("--------click on voltage bellwether case study")
        create_voltage_bellwether_case_study = CreateCaseStudyPrompt(self.driver)
        create_voltage_bellwether_case_study.enter_case_study_name(nameOfCaseStudy)
        self.logger.info("--------While creation entered the name of case study")
        create_voltage_bellwether_case_study.enter_case_study_description(descOfCaseStudy)
        self.logger.info("--------While creation entered the description of case study")
        self.driver.save_screenshot("./Screenshots/CreateCaseStudy/VoltageBellwether/" + "creation_page.png")
        create_voltage_bellwether_case_study.click_on_next_page()
        self.logger.info("--------While creation clicked on next page")
        create_case_study_by_jurisdiction = CreateCaseStudyByJurisdictionPrompt(self.driver)
        self.logger.info("--------While creation entered the description of case study")
        create_case_study_by_jurisdiction.click_on_select_all_jurisdictions()
        self.logger.info("--------click on selection of all jurisdiction of case study")
        create_case_study_by_jurisdiction.click_on_select_all_substations()
        self.logger.info("--------While creation entered the substation of case study")
        #create_case_study_by_jurisdiction.click_on_select_all_feeders()
        time.sleep(5)
        create_case_study_by_jurisdiction.click_on_save()
        self.logger.info("--------Click on saved")
        self.driver.save_screenshot("./Screenshots/CreateCaseStudy/VoltageBellwether/" + "created_page.png")
        names = create_case_study.get_case_study_name()
        self.logger.info("---------Captured all the name of all created case study")
        status = create_case_study.get_case_study_status()
        self.logger.info("---------Captured all the status of all created case study")
        types = create_case_study.get_case_study_type()
        self.logger.info("---------Captured all the types of all created case study")
        flag = False
        for i in range(0, len(names)):
            if names[i] == nameOfCaseStudy and types[i] == "Voltage Bellwether":
                flag = True
                break
        assert flag

        # self.logger.info("name of newly created case study is matched")
        # if status[i] == "Ready" and types[i] == "System Planning":
        #     self.logger.info("status and the type of the newly created case study is matched")
        #     assert True
        #     self.logger.log("Case study creation is successful")
        #     break
        # else:
        #     self.logger.error("status and the type of the newly created case study is not matched")
        #     assert False

    @pytest.mark.fci_placement
    def test_fci_placement_case_study(self, setup):
        self.logger.info("----Starting the fci placement case study creation test")
        descOfCaseStudy = "This is Test for create voltage bellwether case study"
        nameOfCaseStudy = "fciPlacement" + self.randomValue
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        self.logger.info("--------click on login button")
        # self.driver.execute_script("document.body.style.zoom = '0.97'")
        homepage = HomePage(self.driver)
        homepage.click_dashboard()
        self.logger.info("--------click on dashboard button")
        homepage.click_create_case_study()
        self.logger.info("--------click on create case study button")

        create_case_study = CreateCaseStudyPanel(self.driver)
        create_case_study.click_on_create_case_study_icon()
        self.logger.info("--------click on create case study icon")
        create_case_study.click_on_fci_placement()
        self.logger.info("--------click on voltage bellwether case study")
        create_fci_placement_case_study = CreateCaseStudyPrompt(self.driver)
        create_fci_placement_case_study.enter_case_study_name(nameOfCaseStudy)
        self.logger.info("--------While creation entered the name of case study")
        create_fci_placement_case_study.enter_case_study_description(descOfCaseStudy)
        self.logger.info("--------While creation entered the description of case study")
        self.driver.save_screenshot("./Screenshots/CreateCaseStudy/FCIPlacement/" + "creation_page.png")
        create_fci_placement_case_study.click_on_next_page()
        self.logger.info("--------While creation clicked on next page")
        create_case_study_by_jurisdiction = CreateCaseStudyByJurisdictionPrompt(self.driver)
        self.logger.info("--------While creation entered the description of case study")
        create_case_study_by_jurisdiction.click_on_select_all_jurisdictions()
        self.logger.info("--------click on selection of all jurisdiction of case study")
        create_case_study_by_jurisdiction.click_on_select_all_substations()
        self.logger.info("--------While creation entered the substation of case study")
        #create_case_study_by_jurisdiction.click_on_select_all_feeders()
        time.sleep(5)
        create_case_study_by_jurisdiction.click_on_save()
        self.logger.info("--------Click on saved")
        self.driver.save_screenshot("./Screenshots/CreateCaseStudy/FCIPlacement/" + "created_page.png")
        names = create_case_study.get_case_study_name()
        self.logger.info("---------Captured all the name of all created case study")
        status = create_case_study.get_case_study_status()
        self.logger.info("---------Captured all the status of all created case study")
        types = create_case_study.get_case_study_type()
        self.logger.info("---------Captured all the types of all created case study")
        flag = False
        for i in range(0, len(names)):
            if names[i] == nameOfCaseStudy and types[i] == "FCI Placement":
                flag = True
                break
        assert flag

        # self.logger.info("name of newly created case study is matched")
        # if status[i] == "Ready" and types[i] == "System Planning":
        #     self.logger.info("status and the type of the newly created case study is matched")
        #     assert True
        #     self.logger.log("Case study creation is successful")
        #     break
        # else:
        #     self.logger.error("status and the type of the newly created case study is not matched")
        #     assert False

    def test_switch_placement_case_study(self, setup):
        self.logger.info("----Starting the switch placement case study creation test")
        descOfCaseStudy = "This is Test for create switch placement case study"
        nameOfCaseStudy = "switchPlacement" + self.randomValue
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        self.logger.info("--------click on login button")
        # self.driver.execute_script("document.body.style.zoom = '0.97'")
        homepage = HomePage(self.driver)
        homepage.click_dashboard()
        self.logger.info("--------click on dashboard button")
        homepage.click_create_case_study()
        self.logger.info("--------click on create case study button")
        create_case_study = CreateCaseStudyPanel(self.driver)
        create_case_study.click_on_create_case_study_icon()
        self.logger.info("--------click on create case study icon")
        create_case_study.click_on_switch_placement()
        self.logger.info("--------click on switch placement case study")
        create_fci_placement_case_study = CreateCaseStudyPrompt(self.driver)
        create_fci_placement_case_study.enter_case_study_name(nameOfCaseStudy)
        self.logger.info("--------While creation entered the name of case study")
        create_fci_placement_case_study.enter_case_study_description(descOfCaseStudy)
        self.logger.info("--------While creation entered the description of case study")
        self.driver.save_screenshot("./Screenshots/CreateCaseStudy/SwitchPlacement/" + "creation_page.png")
        create_fci_placement_case_study.click_on_next_page()
        self.logger.info("--------While creation clicked on next page")
        create_case_study_by_jurisdiction = CreateCaseStudyByJurisdictionPrompt(self.driver)
        self.logger.info("--------While creation entered the description of case study")
        create_case_study_by_jurisdiction.click_on_select_all_jurisdictions()
        self.logger.info("--------click on selection of all jurisdiction of case study")
        create_case_study_by_jurisdiction.click_on_select_all_substations()
        self.logger.info("--------While creation entered the substation of case study")
        #create_case_study_by_jurisdiction.click_on_select_all_feeders()
        time.sleep(5)
        create_case_study_by_jurisdiction.click_on_save()
        self.logger.info("--------Click on saved")
        self.driver.save_screenshot("./Screenshots/CreateCaseStudy/SwitchPlacement/" + "created_page.png")
        names = create_case_study.get_case_study_name()
        self.logger.info("---------Captured all the name of all created case study")
        status = create_case_study.get_case_study_status()
        self.logger.info("---------Captured all the status of all created case study")
        types = create_case_study.get_case_study_type()
        self.logger.info("---------Captured all the types of all created case study")
        flag = False
        for i in range(0, len(names)):
            if names[i] == nameOfCaseStudy and types[i] == "Switch Placement":
                flag = True
                break
        assert flag

        # self.logger.info("name of newly created case study is matched")
        # if status[i] == "Ready" and types[i] == "System Planning":
        #     self.logger.info("status and the type of the newly created case study is matched")
        #     assert True
        #     self.logger.log("Case study creation is successful")
        #     break
        # else:
        #     self.logger.error("status and the type of the newly created case study is not matched")
        #     assert False


