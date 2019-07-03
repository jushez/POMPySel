from selenium import webdriver
from src.PageObjects.Home.homePage import HomePage
from src.PageObjects.Login.loginPage import LoginPage

class TestLogin:
    # Initialise TestLogin elements
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.homePageObject = HomePage(self.driver)
        self.loginPageObject = LoginPage(self.driver)

    # Login with Email
    def test_login_withEmail(self):
        self.driver.get("http://domain.com.au")
        self.homePageObject.click_login()
        self.loginPageObject.enter_UsernameAndPassword()
        self.loginPageObject.click_NextToLogin()


startLoginTest = TestLogin()
# Login with test accounts
startLoginTest.test_login_withEmail()

