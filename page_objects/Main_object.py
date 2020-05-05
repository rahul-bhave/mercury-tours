"""
This class handles all methods required for AlturoMutualMainpage
"""
from .Base_Page import Base_Page
import conf.login_form_conf as credentials
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import pytest

class Main_object:

    signin = locators.signin
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
    go = locators.go
    Username=credentials.Username
    Password=credentials.Password
    Amount = "300"
    
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
        self.add_to_account(self.toAccountOption)
        self.set_transaction_amount(self.transferAmountText,"300")
        self.submit_transfer_fund()
        result_flag= self.check_element_displayed(self.AmountTransferCheck)
        self.wait(3)
        self.conditional_write(result_flag,
            positive='Element located',
            negative='Element not located',
            level='debug')

        return result_flag
        
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def view_account_summary(self):
        "View account summary"
        self.driver.find_element_by_id("MenuHyperLink1").click()
        self.click_element(self.go)
        result_flag=self.driver.find_element_by_xpath("//html/body/table[2]/tbody/tr/td[2]/div/h1[contains(text(),'Account History - 800002 Savings')]")
        if result_flag.is_displayed():
              self.write("Account summary shown")
        else:
              self.write("Summary not shown")