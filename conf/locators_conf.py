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

#Locators for the form object(Main_Page.py)
signin="xpath,//a[@id='LoginLink']"
username = "xpath,//input[@id='uid']"
password = "xpath,//input[@id='passw']"
submit="xpath,//input[@value='Login']"
transfer_link = "xpath,//a[@id='MenuHyperLink3']"
fromaccount_dropdown = "xpath,//select[@id='fromAccount']"
fromaccount_option = "xpath,//option[@value='800002']"
toaccount_dropdown = "xpath,//select[@id='toAccount']"
toaccount_option = "xpath,//option[@value='800003']"
transferammount_text = "xpath,//input[@id='transferAmount']"
transferamount_button = "xpath,//input[@id='transfer']"
transfer_amount_check="xpath,//span[@id='_ctl0__ctl0_Content_Main_postResp']"
view_account_summary_link = "xpath,//a[@id='MenuHyperLink1']"
go="xpath,//input[@value='   GO   ']"
view_account_summary_check = "xpath,//h1[contains(text(),'Account History')]"
fromAccount="xpath,//select[@name='fromAccount']/option[text()='800002 Savings']"
toAccount="xpath,//select[@name='toAccount']/option[text()='800003 Checking']"
#----
