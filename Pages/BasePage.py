class BasePage():
    """ Base page for all PageObjects"""
    def __init__(self, driver):
        self.url = None
        self.driver = driver

    def open(self):
        self.driver.get(self.url)
