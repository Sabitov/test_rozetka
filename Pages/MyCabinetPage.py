from BasePage import BasePage
import UI

class MyCabinetPage(BasePage):
    #setting constant. Must be like (constant_value, constant_type)
    shoot_for_name = ("m-user-title","class")
    def __init__(self,driver,data):
        self.data=data
        BasePage.__init__(self,driver)

    def shoot_cabinet_name(self):
        base_element_object = UI.BaseElement(self.shoot_for_name[0],self.shoot_for_name[1],self.driver)
        cabinet_name = base_element_object.get_text()
        if cabinet_name == self.data[0]:
            print "\nTest completed. Cabinet_Name is %s" %cabinet_name
        else:
            print "Test NOT completed. Cabinet_Name is %s" %cabinet_name

