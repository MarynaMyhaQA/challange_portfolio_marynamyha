from pages.base_page import BasePage


class Dashboard(BasePage):
    Main_page_xpath = "//*[text()='Main page']"
    Activity_xpath = "//*[text()='Activity']"
    Shortcuts_xpath = "//*[text()='Shortcuts']"
    Sign_out_xpath = "//*[text()='Sign out']"
    Players_xpath = "//*[text()='Players']"
    Scouts_Panel_xpath = "//*[text()='Scouts Panel']"
    Players_count_xpath = "//main/div[2]/div[1]/div/div[1]"
    Reports_count_xpath = "//main/div[2]/div[3]/div/div[1]"
    Matches_count_xpath = "//main/div[2]/div[2]/div/div[1]"
    Events_count_xpath = "//div[1]/main/div[2]/div[4]/div/div[1]"
