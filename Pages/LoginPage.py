from BasePage import BasePage
from MyCabinetPage import MyCabinetPage
import UI
import yaml

class LoginPage(BasePage):
    #setting constant. Must be like (constant_value, constant_type)
    enter_name = ("title","name")
    enter_email = ("email","name")
    enter_password = ("password", "name")
    push_to_log = ("button-css-green", "class")

    #input login data from login_data.yaml. Must be like : (name,email,password)
    pre_data = yaml.load(file('H:\\Python\\study\\Tetst_page_object\\login_data.yaml', 'r'))
    data = (pre_data.get('name')[0],pre_data.get('email')[0],pre_data.get('password')[0])

    def login_try(self):
        UI.BaseElement(self.enter_name[0],self.enter_name[1],self.driver).set_text(self.data[0])
        UI.BaseElement(self.enter_email[0],self.enter_email[1],self.driver).set_text(self.data[1])
        UI.BaseElement(self.enter_password[0],self.enter_password[1],self.driver).set_text(self.data[2])
        UI.BaseElement(self.push_to_log[0],self.push_to_log[1],self.driver).find_by().click()
        self.driver.implicitly_wait(30)
        return MyCabinetPage(self.driver,self.data)
