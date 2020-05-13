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


    @Wrapit._exceptionHandler
    def add_from_account(self, fromAccount, wait_time=3):
        "Use this method to add from Account"
        result_flag = self.click_element(self.fromAccount)
        self.smart_wait(wait_time, self.fromAccount)
        result_flag &= self.click_element(self.fromAccountOption)
        self.conditional_write(result_flag,
            positive='from account set',
            negative='failed to set from Account',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def add_to_account(self, toAccount, wait_time=1):
        "Use this method to add from Account"
        result_flag = self.click_element(self.toAccount)
        self.smart_wait(wait_time, self.toAccount)
        result_flag &= self.click_element(self.toAccountOption)
        self.conditional_write(result_flag,
            positive='to account set',
            negative='failed to set to Account',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_transaction_amount(self, Amount, wait_time=1):
        "Set the transaction amount"
        result_flag = self.set_text(self.transferAmountText, Amount)
        self.smart_wait(wait_time,self.transferAmountText)
        self.conditional_write(result_flag,
            positive='transcations amount set %s'%Amount,
            negative='could not set transaction amount',
            level='debug')

        return result_flag

    def submit_transfer_fund(self):
        "use this method to click on transfer fund button"
        result_flag = self.click_element(self.transferAmountButton)
        self.conditional_write(result_flag,
            positive='succesfully clicked',
            negative='click not successful',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def transfer_fund(self, Amount, wait_time=3):
        "use this method to transfer amount"
        result_flag = self.add_from_account(self.fromAccountOption)
        result_flag &= self.smart_wait(wait_time,self.fromAccountOption)
        result_flag &= self.add_to_account(self.toAccountOption)
        result_flag &= self.smart_wait(wait_time, self.toAccountOption)
        result_flag &= self.set_transaction_amount(Amount)
        result_flag &= self.submit_transfer_fund()
        result_flag &= self.check_element_displayed(self.AmountTransferCheck)
        result_flag &= self.smart_wait(wait_time, self.AmountTransferCheck)
        self.conditional_write(result_flag,
            positive='Element located',
            negative='Element not located',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def click_view_account_summary(self):
        "click on view account summary"
        result_flag = self.click_element(self.account_summary_link, wait_time=3)
        self.conditional_write(result_flag,
            positive='succesfully clicked',
            negative='click not successful',
            level='debug')

        return result_flag
 

    @Wrapit._exceptionHandler
    def click_go_button(self):
        "clicking on go button"
        result_flag = self.click_element(self.go)
        self.conditional_write(result_flag,
            positive='succesfully clicked',
            negative='click not successful',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def view_account_summary(self, wait_time=3):
        "View account summary"
        result_flag = self.click_view_account_summary()
        # result_flag &= self.check_redirect_bank_page()
        result_flag &= self.click_go_button()
        result_flag &= self.check_element_displayed(self.account_summary_check)
        result_flag &= self.smart_wait(wait_time,self.account_summary_check)
        self.conditional_write(result_flag,
            positive='Element located',
            negative='Element not located',
            level='debug')

        return result_flag  
