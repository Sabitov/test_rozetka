from selenium.common.exceptions import NoSuchElementException
from time import sleep

class BaseElement():
    #BaseElement's methods for all project
    def __init__(self, locator, locator_type, driver):
        self.locator = locator
        self.driver = driver
        self.locator_type = locator_type

    def change_find_by_param(self,new_locator, new_locator_type):
        self.locator = new_locator
        self.locator_type = new_locator_type
        return self

    def find_by(self):
        #locator_type must be in (id,name,class,xpath)
        if self.locator_type == "id":
            return self.driver.find_element_by_id(self.locator)
        elif self.locator_type == "name" :
            return self.driver.find_element_by_name(self.locator)
        elif self.locator_type == "class":
            return self.driver.find_element_by_class_name(self.locator)
        elif self.locator_type == "xpath":
            return self.driver.find_element_by_xpath(self.locator)

    def get_text(self):
        return self.find_by().text

    def set_text(self, some_text):
        self.find_by().clear()
        self.find_by().send_keys(some_text)

    def click(self):
        sleep(.5)
        self.find_by().click()
