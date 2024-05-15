import configparser
import os

config=configparser.RawConfigParser()
#config.read('../Configuration/config.ini')
config.read(".\\Configuration\\config.ini")
#config.read('C:\\Users\\deshmuks\\PycharmProjects\\PythonSelfFramework\\nopcommerceApp\\Configuration\\config.ini')

class ReadConfig:

    @classmethod
    def getApplicationURL(cls):
        url=config.get("login_details","baseURL")
        return url

    @classmethod
    def getUseremail(cls):
        username=config.get("login_details","username")
        return username

    @classmethod
    def getPassword(cls):
        password=config.get("login_details","password")
        return password

    @classmethod
    def get_loading_performance_asset_start_date(cls):
        start_date=config.get("loading_performance_asset","start_date")
        return start_date

    @classmethod
    def get_loading_performance_asset_end_date(cls):
        end_date=config.get("loading_performance_asset","end_date")
        return end_date




