from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    language_xpath = "//form/div/div[2]/div/input"
    remind_password_xpath = "//*[text()='Remind password']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
