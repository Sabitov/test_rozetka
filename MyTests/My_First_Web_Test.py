import unittest
from Pages import *
from time import sleep
from selenium import webdriver

class MyTestCase(unittest.TestCase):
        #self.assertEqual(True, False)
        #driver = BaseTestConditions.setUp()

    def setUp(self):
        self.driver=webdriver.Chrome("H:\\Python\\WebDriver_Chrome\\chromedriver.exe")
        #self.driver=webdriver.Firefox()

    def tearDown(self):
        sleep(5)
        self.driver.close()

    def test1(self):
        home = HomePage(self.driver)
        home.open()
        login = home.find_login()
        cabinet = login.login_try()
        cabinet.shoot_cabinet_name()

if __name__ == '__main__':
    unittest.main()
