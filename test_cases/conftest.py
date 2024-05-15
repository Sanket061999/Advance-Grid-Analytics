import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup():
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--kiosk")  #for full screen
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver



"""
#For HTML Report Generation
#It is hoook for adding environment info to HTML report
def pytest_configure(config):
    #intentionally its getting added
    config._metadata['Project Name']='nop Commerce'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='Sanket'


#It is hook for delete/Modify Environme tinfo to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    #default getting added
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins",None)

"""

"""
Giving Error

#To run the test cases in specific browser
#To pass the browser name as argument in  CLI and sent the variable value to set up method

@pytest.fixture()
def pytest_addoption(parser):
    parser.adoption("--browser")
    # and pass it to fixture

@pytest.fixture()
def browser(request):
        return request.config.getoption("--browser")  #This will return the browser value to set up method
"""
