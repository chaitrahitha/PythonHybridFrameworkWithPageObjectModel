from selenium.webdriver.common.by import By
from pages.AccountSuccessPage import AccountSuccessPage
from pages.BasePage import BasePage
class RegisterPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    first_name_field_id = (By.ID,"input-firstname")
    last_name_field_id = (By.ID,"input-lastname")
    email_field_id = (By.ID,"input-email")
    telephone_field_id = (By.ID,"input-telephone")
    password_field_id = (By.ID,"input-password")
    confirm_password_field_id = (By.ID,"input-confirm")
    agree_field_name = (By.NAME,"agree")
    continue_button_xpath = (By.XPATH,"//input[@value='Continue']")
    yes_radio_button_xpath =(By.XPATH,"//input[@name='newsletter'][@value='1']")
    duplicate_email_warning_xpath = (By.XPATH,"//div[@id='account-register']/div[1]")
    privacy_warning_text_xpath = (By.XPATH,"//div[@id='account-register']/div[1]")
    firstname_warning_message_xpath = (By.XPATH,"//input[@id='input-firstname']/following-sibling::div")
    lastname_warning_message_xpath = (By.XPATH,"//input[@id='input-lastname']/following-sibling::div")
    email_warning_message_xpath = (By.XPATH,"//input[@id='input-email']/following-sibling::div")
    telephone_warning_message_xpath = (By.XPATH,"//input[@id='input-telephone']/following-sibling::div")
    password_warning_message_xpath = (By.XPATH,"//input[@id='input-password']/following-sibling::div")

    def enter_first_name(self, first_name_text):
        self.type_into_element(first_name_text, self.first_name_field_id)

    def enter_last_name(self, last_name_text):
        self.type_into_element(last_name_text, self.last_name_field_id)

    def enter_email_text(self, email_text):
        self.type_into_element(email_text, self.email_field_id)

    def enter_telephone_text(self, telephone_text):
        self.type_into_element(telephone_text, self.telephone_field_id)

    def enter_password_text(self, password_text):
        self.type_into_element(password_text, self.password_field_id)

    def enter_confirm_text(self, confirm_text):
        self.type_into_element(confirm_text, self.confirm_password_field_id)

    def select_agree_checkbox_field(self):
        self.element_click(self.agree_field_name)

    def click_on_continue_button(self):
        self.element_click(self.continue_button_xpath)
        return AccountSuccessPage(self.driver)

    def select_yes_radio_button(self):
        self.element_click(self.yes_radio_button_xpath)

    def retrive_duplicate_email_warning(self):
        return self.retrive_element_text(self.duplicate_email_warning_xpath)

    def retrive_privacy_warning_text(self):
        return self.retrive_element_text(self.privacy_warning_text_xpath)

    def retrive_firstname_warning_message(self):
        return self.retrive_element_text(self.firstname_warning_message_xpath)

    def retrive_lastname_warning_message(self):
        return self.retrive_element_text(self.lastname_warning_message_xpath)

    def retrive_email_warning_message(self):
        return self.retrive_element_text(self.email_warning_message_xpath)

    def retrive_telephone_warning_message(self):
        return self.retrive_element_text(self.telephone_warning_message_xpath)

    def retrive_password_warning_message(self):
        return self.retrive_element_text(self.password_warning_message_xpath)

    def register_an_account(self,first_name,last_name,email_text,
                            telephone_text,password_text,confirm_text,
                            yes_or_no,privacy_policy):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email_text(email_text)
        self.enter_telephone_text(telephone_text)
        self.enter_password_text(password_text)
        self.enter_confirm_text(confirm_text)
        if yes_or_no.__eq__("yes"):
            self.select_yes_radio_button()
        if privacy_policy.__eq__("select"):
            self.select_agree_checkbox_field()
        return self.click_on_continue_button()

    def verify_all_warnings(self,expected_privacy_warning_text,expected_firstname_warning_message,
                            expected_lastname_warning_message,expected_email_warning_message,
                            expected_telephone_warning_message,expected_password_warning_message):
        actual_privacy_warning_text = self.retrive_privacy_warning_text()
        actual_firstname_warning_message = self.retrive_firstname_warning_message()
        actual_lastname_warning_message = self.retrive_lastname_warning_message()
        actual_email_warning_message = self.retrive_email_warning_message()
        actual_telephone_warning_message = self.retrive_telephone_warning_message()
        actual_password_warning_message = self.retrive_password_warning_message()

        status = False

        if expected_privacy_warning_text.__contains__(actual_privacy_warning_text):
            if expected_firstname_warning_message.__eq__(actual_firstname_warning_message):
                if expected_lastname_warning_message.__eq__(actual_lastname_warning_message):
                    if expected_email_warning_message.__eq__(actual_email_warning_message):
                        if expected_telephone_warning_message.__eq__(actual_telephone_warning_message):
                            if expected_password_warning_message.__eq__(actual_password_warning_message):
                                status = True

        return status