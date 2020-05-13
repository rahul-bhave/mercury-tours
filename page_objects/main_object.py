"""
This class handles all methods required for all pages
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import pytest

class Main_object:

    signin = locators.signin
    login_redirect = locators.login_redirect
    
    fromAccount = locators.fromaccount_dropdown
    fromAccountOption = locators.fromaccount_option
    toAccount = locators.toaccount_dropdown
    toAccountOption = locators.toaccount_option
    transferAmountText = locators.transferammount_text
    transferAmountButton = locators.transferamount_button
    AmountTransferCheck = locators.transfer_amount_check
    account_summary_link = locators.view_account_summary_link
    go = locators.go
    account_summary_check = locators.view_account_summary_check
   
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

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_redirect_login(self):
        result_flag = False
        if self.check_element_present(self.login_redirect) is not None:
           result_flag = True
           self.conditional_write(result_flag,
               positive='You are on Login page',
               negative='Failed to go on Login page',
               level='debug')
           self.switch_page("login_redirect_page")
        return result_flag 

    @Wrapit._exceptionHandler
    def access_login_page(self):
        "method to access login page"
        result_flag = self.clik_signin()
        result_flag &= self.check_redirect_login()

        return result_flag
