from pages.HomePage import HomePage
from test1.BaseTest import BaseTest
from utilities import ExcelUtils


class TestRegister(BaseTest):
    driver = None

    def test_create_account_with_mandatory_feilds(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_register_page()
        account_success_page = (register_page.register_an_account
                                (ExcelUtils.get_cell_data("ExcelFile/excel_Demo_File.xlsx",
                                                          "RegisterTest",2,1),
                                ExcelUtils.get_cell_data("ExcelFile/excel_Demo_File.xlsx",
                                                         "RegisterTest",2,2),
                                 self.generate_email_time_stamp(),
                                ExcelUtils.get_cell_data("ExcelFile/excel_Demo_File.xlsx",
                                                         "RegisterTest",2,3),
                                                                 "12345","12345","no","select"))
        expected_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_text)



    def test_create_account_by_providing_all_feilds(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_register_page()
        account_success_page = register_page.register_an_account("Chaitra","Bn",self.generate_email_time_stamp(),
                                                                 "1234567890","12345","12345","yes","select")
        expected_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_text)
    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_register_page()
        register_page.register_an_account("Chaitra","Bn","amotooricap3@gmail.com","1234567890","12345",
                                          "12345","yes","select")
        expected_warning_text = "Warning: E-Mail Address is already registered!"
        assert register_page.retrive_duplicate_email_warning().__contains__(expected_warning_text)
    def test_register_without_entering_feilds(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_register_page()
        register_page.register_an_account("","","","","","","no","no")
        assert register_page.verify_all_warnings("Warning: You must agree to the Privacy Policy!",
                                                 "First Name must be between 1 and 32 characters!",
                                                 "Last Name must be between 1 and 32 characters!",
                                                 "E-Mail Address does not appear to be valid!",
                                                 "Telephone must be between 3 and 32 characters!",
                                                 "Password must be between 4 and 20 characters!")
