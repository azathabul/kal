# pytest with POM
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from Test_Data import data
from Test_Locators import locators
import pytest


class Test_azath:
    # Boot the method to run pytest using POM
    @pytest.fixture
    def startup(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()

    # login test case 1
    def test_login(self, startup):
        self.driver.get(data.Data().url)
        self.driver.find_element(by=By.NAME, value=locators.locators().username_input_box).send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value=locators.locators().password_input_box).send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=loctors.locators().submit_button ).click()
        assert self.driver.title == "OrangeHRM"
        print("SUCCESS : Logged in with Username {a} and {b}".format(a=data.Data().username, b=data.Data().password))
        
    # Test case 2
    def test_login(self, invalid employee):
        self.driver.get(data.Data().url)
        self.driver.find_element(by=By.NAME, value=locators.locators().username_input_box).send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value=locators.locators().password_input_box).send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=loctors.locators().submit_button ).click()
        assert self.driver.title == "OrangeHRM"
        print("SUCCESS : UNLogged in with Username {a} and {b}".format(a=data.Data().username, b=data.Data().password))
        
    # Test case 3 with PIM 1
    def  test_login(self, Enter new employee ):
        self.driver.get(data.Data().url)
        self.driver.find_element(by=By.NAME, value=locators.locators().username_input_box).send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value=locators.locators().password_input_box).send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=loctors.locators().submit_button ).click()
        assert self.driver.title == "OrangeHRM"
        self.driver.get(pim module)
        self.driver.add (new employee,arun)
        self.driver.add(name,photo,image)
        print("SUCCESS : Logged in with Username {a} and {b}".format(a=data.Data().username, b=data.Data().password))
        print("SUCCESS:add the employee details")
        
    # Test case 4 with pim 2 EDIT tht employee details
    def  test_login(self, Edit the employee ):
        self.driver.get(data.Data().url)
        self.driver.find_element(by=By.NAME, value=locators.locators().username_input_box).send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value=locators.locators().password_input_box).send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=loctors.locators().submit_button ).click()
        assert self.driver.title == "OrangeHRM"
        self.driver.get(pim module)
        self.driver.add (new employee,S.arun)
        self.driver.add(name,photo,image,Change)
        print("SUCCESS : Logged in with Username {a} and {b}".format(a=data.Data().username, b=data.Data().password))
        print("SUCCESS:edit the employee details") 
          
    # Test  case 5 with pim 3 DELETE the employee
    def  test_login(self, deletethe employee ):
        self.driver.get(data.Data().url)
        self.driver.find_element(by=By.NAME, value=locators.locators().username_input_box).send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value=locators.locators().password_input_box).send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=loctors.locators().submit_button ).click()
        assert self.driver.title == "OrangeHRM"
        self.driver.get(pim module)
        self.driver.get(delete name and photo)
        print("SUCCESS : Logged in with Username {a} and {b}".format(a=data.Data().username, b=data.Data().password))
        print("SUCCESS:Delete the employee details") 
    
         
           
           