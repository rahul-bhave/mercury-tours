"""
This class models the altoro mutual main page

"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
from page_objects.Main_object import Main_object

class Login_Redirect_Page(Base_Page,Main_object):
    "Page Object for the Altoro Mutual Login page"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = '/login.jsp'
        self.open(url)