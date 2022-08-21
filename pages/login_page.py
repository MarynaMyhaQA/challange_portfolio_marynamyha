from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    language_xpath = "//form/div/div[2]/div/input"
    remind_password_xpath = "//*[text()='Remind password']"
    expected_title = "Scouts panel - sign in"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    form_title = '//*[@id="__next"]/form/div/div[1]/h5'
    expected_form_title = "Scouts Panel"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_the_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_title_of_the_form(self):
        self.assert_element_text(self.driver, self.form_title, self.expected_form_title)
