"""
This class models the altoro mutual login page

"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
from page_objects.AlturoMutualLogin import AlturoMutualLogin

class Altoro_Mutual_Main_Page(Base_Page,AlturoMutualLogin):
    "Page Object for the Altoro Mutual Main page"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = '/login.jsp'
        self.open(url)