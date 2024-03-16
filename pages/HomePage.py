from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchPage import SearchPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_name = (By.NAME,"search")
    search_button_xpath = (By.XPATH,"//button[@class='btn btn-default btn-lg']")
    my_account_dropmenu_xpath = (By.XPATH,"//span[text()='My Account']")
    login_option_link_text = (By.LINK_TEXT,"Login")
    register_option_link_text = (By.LINK_TEXT,"Register")

    def enter_product_into_search_box_field(self,product_name):
        self.type_into_element(product_name,self.search_box_field_name)

    def click_on_search_button(self):
        self.element_click(self.search_button_xpath)
        return SearchPage(self.driver)

    def click_on_my_acc_drop_menu(self):
        self.element_click(self.my_account_dropmenu_xpath)

    def select_login_option(self):
        self.element_click(self.login_option_link_text)
        return LoginPage(self.driver)

    def select_register_option(self):
        self.element_click(self.register_option_link_text)
        return RegisterPage(self.driver)

    def search_for_a_product(self,product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_on_search_button()

    def navigate_login_page(self):
        self.click_on_my_acc_drop_menu()
        return self.select_login_option()

    def navigate_register_page(self):
        self.click_on_my_acc_drop_menu()
        return self.select_register_option()
