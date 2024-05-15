import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoadingPerformanceAsset:
    button_calender=(By.XPATH,"//body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/img[1]")
    textbox_start_date=(By.XPATH,"//input[@id='-dateRangePanel-selectionDialog-startDateField-input']")
    textbox_end_date=(By.XPATH,"//input[@id='-dateRangePanel-selectionDialog-endDateField-input']")
    button_ok_on_date_range_selection=(By.XPATH,"//div[contains(text(),'OK')]")
    select_single_substation=(By.CSS_SELECTOR,"body > div:nth-child(61) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)")


    def __init__(self,driver):
        self.driver=driver

    def click_calendar(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(LoadingPerformanceAsset.button_calender)).click()
        #self.driver.find_element(*LoadingPerformanceAsset.button_calender).click()

    def set_date(self,start_date,end_date):
        act=ActionChains(self.driver)
        element=WebDriverWait(self.driver,2).until(EC.presence_of_element_located(LoadingPerformanceAsset.textbox_start_date)).send_keys(start_date)

        #element = self.driver.find_element(*LoadingPerformanceAsset.textbox_start_date)
        act.click(element).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(start_date).perform()
        act.click(element).send_keys(Keys.TAB,Keys.TAB).send_keys(end_date).perform()
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located(LoadingPerformanceAsset.button_ok_on_date_range_selection)).click()
        #self.driver.find_element(*LoadingPerformanceAsset.button_ok_on_date_range_selection).click()

    def set_single_substation(self):
        pass
        #Not working
        #self.driver.find_element(*LoadingPerformanceAsset.select_single_substation).click()
































        # print(("arguments[0].setAttribute('value'," + str(start_date) + ")", element))
        #self.driver.execute_script("arguments[0].setAttribute('value',"+ start_date+")", element)
        #
        # element = self.driver.find_element(*LoadingPerformanceAsset.textbox_start_date_xpath)
        # element.clear()
        # time.sleep(5)
        # element.send_keys(start_date)
        # time.sleep(5)
        # #
        #
        #
        # act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        #
        # self.logger.info("start date element captured")
        # element.send_keys(Keys.CONTROL,'a')
        # self.logger.info("all item present in the textbox is selected")
        # element.send_keys(start_date)
        # self.logger.info(start_date," this date selected")
        #
        #
        # time.sleep(10)
        # self.logger.info("----start date field of calendar is clear--")
        # self.driver.find_element(*LoadingPerformanceAsset.textbox_start_date_xpath).send_keys(start_date)
        # time.sleep(5)







