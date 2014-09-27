from BasePage import BasePage
import UI
class HomePage(BasePage):
    #setting constant. Must be like (constant_value, constant_type)
    entrance_in_magazine = ("signin", "name")
    push_to_login = ("//*[@class='auth-f-signup']//a","xpath")

    def __init__(self,driver):
        BasePage.__init__(self, driver)
        self.url = "http://rozetka.com.ua"

    # def __init__(self, driver):
    #     super(HomePage, self).__init__(driver)
    #     self.url = "http://rozetka.com.ua"

    # def __new__(self):
    #     self.url = "http://rozetka.com.ua"

    # def __init__(self, driver):
    #     self.url = "http://rozetka.com.ua"
    #     self.driver = driver

    def find_login(self):
        base_element_object = UI.BaseElement(self.entrance_in_magazine[0], self.entrance_in_magazine[1], self.driver)
        base_element_object.click()
        base_element_object.change_find_by_param(self.push_to_login[0], self.push_to_login[1]).click()