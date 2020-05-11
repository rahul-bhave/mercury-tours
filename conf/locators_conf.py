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

#Locators for the Main Page
signin="xpath,//a[@id='LoginLink']"
login_redirect = "xpath//h1[contains(text(),'Online Banking Login')]"

#Locators for login page
username = "xpath,//input[@id='uid']"
password = "xpath,//input[@id='passw']"
submit="xpath,//input[@value='Login']"
transfer_link = "xpath,//a[@id='MenuHyperLink3']"
transfer_fund_redirect = "xpath//h1[contains(text(),'Transfer Funds')]"

#Locators for Transfer Fund Page
fromaccount_dropdown = "xpath,//select[@id='fromAccount']"
fromaccount_option = "xpath,//option[@value='800002']"
toaccount_dropdown = "xpath,//select[@id='toAccount']"
toaccount_option = "xpath,//option[@value='800003']"
transferammount_text = "xpath,//input[@id='transferAmount']"
transferamount_button = "xpath,//input[@id='transfer']"
transfer_amount_check="xpath,//span[@id='_ctl0__ctl0_Content_Main_postResp']"

#Locators for Bank Main Page
view_account_summary_link = "xpath,//a[@id='MenuHyperLink1']"
bank_main_page_redirect = "xpath,//p[contains(text(),'Welcome to Altoro Mutual Online.')]"

#Locators for View Account Summary
go="xpath,//input[@value='   GO   ']"
view_account_summary_check = "xpath,//h1[contains(text(),'Account History')]"