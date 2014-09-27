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
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.find_login()
        login_page = LoginPage(self.driver)
        login_page.login_try()
        my_cabinet_page = MyCabinetPage(self.driver,login_page.data)
        my_cabinet_page.shoot_cabinet_name()


if __name__ == '__main__':
    unittest.main()
