from BasePage import BasePage
from LoginPage import LoginPage
import UI
class HomePage(BasePage):
    #setting constant. Must be like (constant_value, constant_type)
    entrance_in_magazine = ("signin", "name")
    push_to_login = ("//*[@class='auth-f-signup']//a","xpath")

    #def __init__(self, driver):
       # self.url = "http://rozetka.com.ua"
       # super(HomePage, self).__init__(driver)

    #def __new__(self):
        #self.url = "http://rozetka.com.ua"

    #def __init__(self,driver):
        #self.url = "http://rozetka.com.ua"
        #BasePage.__init__(self,driver)

    def __init__(self, driver):
        self.url = "http://rozetka.com.ua"
        self.driver = driver

    def find_login(self):
        UI.BaseElement(self.entrance_in_magazine[0], self.entrance_in_magazine[1], self.driver).click()
        UI.BaseElement(self.push_to_login[0], self.push_to_login[1], self.driver).click()
        return LoginPage(self.driver)




