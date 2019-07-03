class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.signup_link_xpath = '//*[@id="__domain_group/APP_ROOT"]/div/div/div[1]/header/div[2]/div/nav/div/div/div/button[2]'
        self.login_link_xpath = '//*[@id="__domain_group/APP_ROOT"]/div/div/div[1]/header/div[2]/div/nav/div/div/div/button[1]'

    def click_signup(self):
        # driver = self.driver
        self.driver.find_element_by_xpath(self.signup_link_xpath).click()

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_link_xpath).click()