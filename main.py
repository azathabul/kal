#main.py
#project 1

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data import data
from Test_Locators import locators
from selenium.webdriver.common.by import By


class azath:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        
        def login(self):
            self.driver.find_element(by=by.NAME, value=locators.Locators().username_input_box).send_keys(data.Data().username)
            self.driver.find_element(by=by.NAME, value=locators.locators().password_input_box).send_keys(data.Data().password)
            self.driver.find_element(by=by.XPATH, value=locators().submit_button).click()
            
            def shutdown(self):
                self.driver.quit()
            
            azath = azath(data.Data() .url)
            
            azath.login()
            
            azath.shutdown()
            
            
            
        
