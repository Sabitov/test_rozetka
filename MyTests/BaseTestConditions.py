#not use
import unittest
from time import sleep
from selenium import webdriver

class BaseTestConditions(unittest.TestCase):
    driver=webdriver.Chrome("H:\\Python\\WebDriver_Chrome\\chromedriver.exe")
    def setUp(self,driver):
        #global driver
        #self.driver=webdriver.Chrome("H:\\Python\\WebDriver_Chrome\\chromedriver.exe")
        #self.driver=webdriver.Firefox()
        #self.driver.get("http://rozetka.com.ua")
        #self.driver.implicitly_wait(10)
        self.driver=driver
        print "setUp!!!!!!!!!!!!!!!!!!!"
        #print driver
    def tearDown(self):
        sleep(5)
        print "tearDown!!!!!!!!!!!!!!!!!!!"
        self.driver.close()



