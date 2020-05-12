"""
This class handles all methods for Login
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import pytest

class Login_object:

    username_field = locators.username
    password_field = locators.password
    submit = locators.submit
    transfer_fund_redirect = locators.transfer_fund_redirect
    transfer_link = locators.transfer_link
    
    result_flag = False

    @Wrapit._exceptionHandler
    def set_username(self, Username):
        "user this method to enter username"
        result_flag = self.set_text(self.username_field,Username)
        self.conditional_write(result_flag,
            positive='Set the Username to: %s'%Username,
            negative='Failed to set the name in the form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_password(self, Password):
        "user this method to enter username"
        result_flag = self.set_text(self.password_field,Password)
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
    @Wrapit._screenshot
    def Login(self, Username, Password):
        "submit the form"
        result_flag = self.set_username(Username)
        result_flag &= self.set_password(Password)
        result_flag &= self.click_submit()

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def access_transfer_fund(self):
        "check access transfer fund is avialble"
        result_flag = self.clik_transfer_funds()
        result_flag &= self.check_redirect_transfer_fund()

        return result_flag