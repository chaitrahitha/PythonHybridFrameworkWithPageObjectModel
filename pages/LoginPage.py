from selenium.webdriver.common.by import By
from pages.AccountPage import AccountPage
from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    email_add_field_id = (By.XPATH,"//input[@id='input-email']")
    password_field_id = (By.XPATH,"//input[@id='input-password']")
    login_button_xpath = (By.XPATH,"//input[@value='Login']")
    warning_message_xpath = (By.XPATH,"//div[@id='account-login']/div[1]")

    def enter_email_add(self, email_add_text):
        self.type_into_element(email_add_text, self.email_add_field_id)

    def enter_password(self, password_text):
        self.type_into_element(password_text, self.password_field_id)

    def click_on_login_button(self):
        self.element_click(self.login_button_xpath)
        return AccountPage(self.driver)

    def login(self,email,password):
        self.enter_email_add(email)
        self.enter_password(password)
        return self.click_on_login_button()

    def retrive_warning_message(self):
        return self.retrive_element_text(self.warning_message_xpath)
