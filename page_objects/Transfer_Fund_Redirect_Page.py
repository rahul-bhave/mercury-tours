"""
This class models the altoro mutual main page

"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
from page_objects.main_object import Main_object

class Transfer_Fund_Redirect_Page(Base_Page,Main_object):
    "Page Object for the Transfer Fund"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = '/bank/transfer.jsp'
        self.open(url)