"""
This class handles all methods required for AlturoMutualMainpage
"""
from .Base_Page import Base_Page
import conf.login_form_conf as credentials
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import pytest

class Altoromutualmain_object:

    signin = locators.signin
    submit = locators.submit
    fromAccount = locators.fromAccount
    toAccount = locators.toAccount
    go = locators.go
    transfer_fund = locators.transfer_fund
    Username=credentials.Username
    Password=credentials.Password

    result_flag = False

    @Wrapit._exceptionHandler
    def clik_signin(self):
        "use this method to click on sign in"
        result_flag=self.click_element(self.signin,wait_time=3)
        self.conditional_write(result_flag,
            positive='click success',
            negative='click not success',
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    def click_submit(self):
        "use this method to click submit"
        self.driver.find_element_by_id("uid").send_keys(self.Username)
        self.driver.find_element_by_id("passw").send_keys(self.Password)
        result_flag=self.click_element(self.submit,wait_time=3)
        self.conditional_write(result_flag,
            positive='succesfully clicked',
            negative='click not successful',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def clik_transfer_funds(self):
        "use this method to click transfer funds"
        result_flag=self.driver.find_element_by_id("MenuHyperLink3").click()
        self.write("Transfer fund link clicked")
        return result_flag
  
    @Wrapit._exceptionHandler
    def transfer_fund(self):
        "use this method to transfer amount"
        self.click_element(self.fromAccount)
        self.click_element(self.toAccount)
        self.driver.find_element_by_id("transferAmount").send_keys("300")
        self.driver.find_element_by_id("transfer").click()
        result_flag = self.driver.find_element_by_id("_ctl0__ctl0_Content_Main_postResp")
        self.driver.save_screenshot("C:\\Users\\Rahul Bhave Qxf2\\code\\rahul-qxf2\\altoro-mutual-pom\\screenshots\\Transferamount.png")
        if result_flag.is_displayed():
                self.write ("Transaction successful" )
        else:
                self.write ("Transaction unsuccessful")

    @Wrapit._exceptionHandler
    def view_account_summary(self):
        "View account summary"
        self.driver.find_element_by_id("MenuHyperLink1").click()
        self.click_element(self.go)
        result_flag=self.driver.find_element_by_xpath("//html/body/table[2]/tbody/tr/td[2]/div/h1[contains(text(),'Account History - 800002 Savings')]")
        if result_flag.is_displayed():
              self.write("Account summary shown")
        else:
              self.write("Summary not shown")