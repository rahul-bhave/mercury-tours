"""
This class handles all AltoroMutualMainPage
"""
from .Base_Page import Base_Page
import conf.login_form_conf as credentials
from utils.Wrapit import Wrapit
import pytest

class AlturoMutualLogin():

    
    locator_submit="xpath,//a[@id='LoginLink']"
    @Wrapit._exceptionHandler
    def Login(self):
        "use this method to login"
        
        result_flag=self.click_element(self.signin,wait_time=3)
        self.conditional_write(result_flag,
            positive='Login successful',
            negative='Login not successful',
            level='debug')
        return result_flag