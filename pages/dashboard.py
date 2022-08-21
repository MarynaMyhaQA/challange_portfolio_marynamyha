import time

from pages.base_page import BasePage

class Dashboard(BasePage):
    main_page_xpath = "//*[text()='Main page']"
    activity_xpath = "//*[text()='Activity']"
    shortcuts_xpath = "//*[text()='Shortcuts']"
    sign_out_xpath = "//*[text()='Sign out']"
    players_xpath = "//*[text()='Players']"
    scouts_Panel_xpath = "//*[text()='Scouts Panel']"
    players_count_xpath = "//main/div[2]/div[1]/div/div[1]"
    reports_count_xpath = "//main/div[2]/div[3]/div/div[1]"
    matches_count_xpath = "//main/div[2]/div[2]/div/div[1]"
    events_count_xpath = "//div[1]/main/div[2]/div[4]/div/div[1]"

    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
