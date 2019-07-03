from selenium import webdriver
from src.PageObjects.Home.homePage import HomePage
from src.PageObjects.Registration.registrationPage import RegistrationPage

class TestRegistration:
    # Initialize TestRegistration elements
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.homePageObject = HomePage(self.driver)
        self.registerPageObject = RegistrationPage(self.driver)

    # Register with Email
    def test_registration_withEmail(self):
        self.driver.get("http://domain.com.au")
        self.homePageObject.click_signup()
        self.registerPageObject.enter_UsernameAndPassword()
        self.registerPageObject.click_NextToRegister()


startRegistrationTest = TestRegistration()
# Register with test accounts
startRegistrationTest.test_registration_withEmail()