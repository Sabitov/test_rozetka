from BasePage import BasePage
import UI

class MyCabinetPage(BasePage):
    #setting constant. Must be like (constant_value, constant_type)
    shoot_for_name = ("m-user-title","class")
    def __init__(self,driver,data):
        self.data=data
        BasePage.__init__(self,driver)

    def shoot_cabinet_name(self):
        cabinet_name = UI.BaseElement(self.shoot_for_name[0],self.shoot_for_name[1],self.driver).get_text()
        if cabinet_name == self.data[0]:
            print "OLOLOLOLOL it's all OK!!!!!!!!!!!!!!!!!!"
        else:
            print ":(((  not good"

