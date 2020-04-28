"""
This is an example automated test to help you learn Qxf2's framework
Automated test will do the following:
    #Open altoromutual form.
    #Click on Sign In link
    #Fill the form
    #Transfer the amount from one account to other
    #View the transfered amount
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.login_form_conf as credentials
import conf.testrail_caseid_conf as testrail_file


def test_altoro_mutual_form(test_obj):
    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #1. Create a test object and fill the example form.
        test_obj = PageFactory.get_page_object("Altoro_Mutual_Main_Page")

        #2. Setup and register a driver
        start_time = int(time.time())	#Set start_time with current time

        #3. Turn on the highlighting feature
        test_obj.turn_on_highlight()
        
        #4. Click on sign in link fill the form and submit the form
        test_obj.clik_signin()
        """
        is_screen_visible=test_obj.check_redirect_login()
        if is_screen_visible is not None:
            self.write("You are on login page")
        """
        Username=credentials.Username
        Password=credentials.Password
        test_obj.driver.find_element_by_id("uid").send_keys(Username)
        test_obj.driver.find_element_by_id("passw").send_keys(Password)
        test_obj.click_submit()
        
        #5. Click on transfer fund link
        test_obj.clik_transfer_funds()

        #6 Transfer funds
        test_obj.add_from_account()
        test_obj.add_to_account()
        test_obj.transfer_fund()

        #7 Account summary
        test_obj.view_account_summary()

        #waiting for pass counters
        test_obj.wait(3)
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter
                  
    except Exception as e:
        print("Exception when trying to run test:%s"%__file__)
        print("Python says:%s"%str(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__
       
    
#---START OF SCRIPT   
if __name__=='__main__':

  
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()
                
    #Run the test only if the options provided are valid
    if options_obj.check_options(options): 
        test_obj = PageFactory.get_page_object("Zero",base_url=options.url)

        #Setup and register a driver
        test_obj.register_driver(options.remote_flag,options.os_name,options.os_version,options.browser,options.browser_version,options.remote_project_name,options.remote_build_name)

        #Setup TestRail reporting
        if options.testrail_flag.lower()=='y':
            if options.test_run_id is None:
                test_obj.write('\033[91m'+"\n\nTestRail Integration Exception: It looks like you are trying to use TestRail Integration without providing test run id. \nPlease provide a valid test run id along with test run command using -R flag and try again. for eg: pytest -X Y -R 100\n"+'\033[0m')
                options.testrail_flag = 'N'   
            if options.test_run_id is not None:
                test_obj.register_testrail()
                test_obj.set_test_run_id(options.test_run_id)

        if options.tesults_flag.lower()=='y':
            test_obj.register_tesults()

        test_altoro_mutual_form(test_obj)
                
        #teardowm
        test_obj.wait(3)
        test_obj.teardown() 
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())