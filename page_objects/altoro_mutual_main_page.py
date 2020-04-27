"""
This class models the altoro mutual main page

"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
from page_objects.AlturoMutualMain import AlturoMutualMain

class Altoro_Mutual_Main_Page(Base_Page,AlturoMutualMain):
    "Page Object for the Altoro Mutual Main page"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'http://demo.testfire.net/'
        self.open(url)
    
    