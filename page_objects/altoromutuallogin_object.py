"""
This class handles all methods required for AlturoMutualLoginPage
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import pytest

class Altoromutuallogin_object:

    submit = locators.submit
    
    @Wrapit._exceptionHandler
    def click_submit(self):
        "use this method to click submit"
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
