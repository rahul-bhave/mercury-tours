"""
This class models the altoro mutual login page

"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
from page_objects.altoromutuallogin_object import Altoromutuallogin_object

class Altoro_Mutual_Login_Page(Base_Page,Altoromutuallogin_object):
    "Page Object for the Altoro Mutual Main page"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = '/login.jsp'
        self.open(url)