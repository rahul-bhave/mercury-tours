"""
This class handles all methods required for all pages
"""
from .Base_Page import Base_Page
import conf.login_form_conf as credentials
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import pytest

class Main_object:

    signin = locators.signin
    login_redirect = locators.login_redirect
    transfer_fund_redirect = locators.transfer_fund_redirect
    bank_main_redirect = locators.bank_main_page_redirect
    username_field = locators.username
    password_field = locators.password
    submit = locators.submit
    transfer_link = locators.transfer_link
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
    Username=credentials.Username
    Password=credentials.Password
    Amount = credentials.Amount
   
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
    def set_username(self, username_field):
        "user this method to enter username"
        result_flag = self.set_text(self.username_field, self.Username)
        self.conditional_write(result_flag,
            positive='Set the Username to: %s'%self.Username,
            negative='Failed to set the name in the form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_password(self, password_field):
        "user this method to enter username"
        result_flag = self.set_text(self.password_field, self.Password)
        self.conditional_write(result_flag,
            positive='Password set succeefully',
            negative='Failed to set the name in the form',
            level='debug')

        return result_flag 

    @Wrapit._exceptionHandler
    def click_submit(self):
        "use this method to click submit"
        result_flag=self.click_element(self.submit, wait_time=3)
        self.conditional_write(result_flag,
            positive='succesfully clicked',
            negative='click not successful',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def submit_form(self):
        "submit the form"
        result_flag = self.set_username(self.Username)
        result_flag &= self.set_password(self.Password)
        result_flag &= self.click_submit()

        return result_flag

    @Wrapit._exceptionHandler
    def clik_transfer_funds(self):
        "use this method to click transfer funds"
        result_flag=self.click_element(self.transfer_link, wait_time=3)
        self.conditional_write(result_flag,
            positive='transfer funds link clicked',
            negative='transfer funds link can not be clicked',
            level='debug')
        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_redirect_transfer_fund(self):
        result_flag = False
        if self.check_element_present(self.transfer_fund_redirect) is not None:
           result_flag = True
           self.conditional_write(result_flag,
               positive='You are on Tranasfer Fund page',
               negative='Failed to go on Transfer Fund page',
               level='debug')
           self.switch_page("transfer_fund_redirect_page")
        return result_flag 

    @Wrapit._exceptionHandler
    def add_from_account(self, fromAccount, wait_time=3):
        "Use this method to add from Account"
        result_flag = self.click_element(self.fromAccount)
        self.wait(wait_time)
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
        self.wait(wait_time)
        result_flag &= self.click_element(self.toAccountOption)
        self.conditional_write(result_flag,
            positive='to account set',
            negative='failed to set to Account',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_transaction_amount(self, Transferamount, Amount, wait_time=1):
        "Set the transaction amount"
        result_flag = self.set_text(self.transferAmountText, self.Amount)
        self.wait(wait_time)
        self.conditional_write(result_flag,
            positive='transcations amount set',
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
    def transfer_fund(self):
        "use this method to transfer amount"
        self.add_from_account(self.fromAccountOption)
        self.wait(3)
        self.add_to_account(self.toAccountOption)
        self.wait(3)
        self.set_transaction_amount(self.transferAmountText,"300")
        self.submit_transfer_fund()
        result_flag = self.check_element_displayed(self.AmountTransferCheck)
        self.wait(3)
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

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_redirect_bank_page(self):
        result_flag = False
        if self.check_element_present(self.bank_main_redirect) is not None:
           result_flag = True
           self.conditional_write(result_flag,
               positive='You are on Bank page',
               negative='Failed to go on Bank page',
               level='debug')
           self.switch_page("bank_main_redirect_page")
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
    def view_account_summary(self):
        "View account summary"
        # self.click_view_account_summary()
        self.click_go_button()
        result_flag = self.check_element_displayed(self.account_summary_check)
        self.wait(3)
        self.conditional_write(result_flag,
            positive='Element located',
            negative='Element not located',
            level='debug')

        return result_flag  