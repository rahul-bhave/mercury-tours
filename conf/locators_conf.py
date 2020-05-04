#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

#Locators for the form object(AlturoMutualMain.py)
signin="xpath,//a[@id='LoginLink']"
username = "xpath,//input[@id='uid']"
password = "xpath,//input[@id='passw']"
submit="xpath,//input[@value='Login']"
fromAccount="xpath,//select[@name='fromAccount']/option[text()='800002 Savings']"
toAccount="xpath,//select[@name='toAccount']/option[text()='800003 Checking']"
go="xpath,//input[@value='   GO   ']"
transfer_fund="xpath,//a[@id='MenuHyperLink3']"
#----
