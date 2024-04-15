import time

from selenium.common import NoAlertPresentException

from features.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_id = "email"
    password_id = "pass"
    login_button_xpath = "//button[.='Log in']"
    login_success_verify_xpath = "//div[@class='xg87l8a x1iymm2a']"
    password_error_verify_xpath = "//span[@class='_akzt']"
    password_error_phone_verify_xpath = "//span[.='Log in as Kane Williams']"
    email_error_verify_xpath = "//div[@class='_9kq2']"
    phone_error_verify_xpath = "//div[@class='_9ay7']"
    forgot_password_xpath = "//a[.='Forgotten password?']"
    verify_forgot_pass_xpath = "//div[@class='_9nq2 marginBottom16px']"
    create_account_xpath = "//a[.='Create new account']"
    verify_signup_xpath = "//div[text()='Sign Up']"
    verify_password_error_xpath = "//div[@class='_9axz']"

    def enter_email(self, email):
        self.type_into_element("email_id", self.email_id, email)

    def enter_phone(self, phone):
        self.type_into_element("email_id", self.email_id, phone)

    def enter_password(self, password_text):
        self.type_into_element("password_id", self.password_id, password_text)

    def click_login(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        time.sleep(50)
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            print("Alert dismissed successfully.")
        except NoAlertPresentException:
            print("No alert found.")

    def verify_login(self, a):
        self.contains("login_success_verify_xpath", self.login_success_verify_xpath, a)

    def verify_password_error(self, a):
        self.contains("password_error_verify_xpath", self.password_error_verify_xpath, a)

    def verify_email_error(self, a):
        self.contains("email_error_verify_xpath", self.email_error_verify_xpath, a)

    def verify_phone_error(self, a):
        self.contains("phone_error_verify_xpath", self.phone_error_verify_xpath, a)

    def click_on_forgot_password(self):
        self.click_on_element("forgot_password_xpath", self.forgot_password_xpath)

    def verify_forgotPass(self, a):
        self.contains("verify_forgot_pass_xpath", self.verify_forgot_pass_xpath, a)

    def click_on_createAccount(self):
        self.click_on_element("create_account_xpath", self.create_account_xpath)

    def verify_createAccount(self, a):
        self.contains("verify_signup_xpath", self.verify_signup_xpath, a)
        time.sleep(5)

    def verify_Password_error_phone(self, a):
        self.contains("password_error_phone_verify_xpath", self.password_error_phone_verify_xpath, a)

    def verify_Password_error_(self, a):
        self.contains("verify_password_error_xpath", self.verify_password_error_xpath, a)
