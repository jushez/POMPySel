class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_name = 'username'
        self.password_name = 'password'
        self.login_next_btn_xpath = '//*[@id="authUiReactRootElement"]/div/div/div[1]/div[1]/div/div/div/div/div[2]/form/div[3]/button'

    def enter_UsernameAndPassword(self):
        self.driver.find_element_by_name(self.username_name).send_keys("fillintestaccount@test.com")
        self.driver.find_element_by_name(self.password_name).send_keys("fillintestpassword")

    def click_NextToLogin(self):
        self.driver.find_element_by_xpath(self.login_next_btn_xpath).click()