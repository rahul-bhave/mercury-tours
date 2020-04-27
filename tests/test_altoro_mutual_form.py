"""
This is an example automated test to help you learn Qxf2's framework
Our automated test will do the following:
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


def test_altoro_mutual_form(base_url,browser,browser_version,os_version,os_name,remote_flag,testrail_flag,tesults_flag,test_run_id,remote_project_name,remote_build_name):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #1. Create a test object and fill the example form.
        test_obj = PageFactory.get_page_object("Altoro_Mutual_Main_Page",base_url=base_url)


        #2. Setup and register a driver
        start_time = int(time.time())	#Set start_time with current time
        test_obj.register_driver(remote_flag,os_name,os_version,browser,browser_version,remote_project_name,remote_build_name)
        
        #3. Setup TestRail reporting
        if testrail_flag.lower()=='y':
            if test_run_id is None:
                test_obj.write('\033[91m'+"\n\nTestRail Integration Exception: It looks like you are trying to use TestRail Integration without providing test run id. \nPlease provide a valid test run id along with test run command using -R flag and try again. for eg: pytest -X Y -R 100\n"+'\033[0m')
                testrail_flag = 'N'   
            if test_run_id is not None:
                test_obj.register_testrail()

        if tesults_flag.lower()=='y':
            test_obj.register_tesults()
        
        #4 click on sign in link fill the form and submit the form
        test_obj.clik_signin()
        Username=credentials.Username
        Password=credentials.Password
        test_obj.driver.find_element_by_id("uid").send_keys(Username)
        test_obj.driver.find_element_by_id("passw").send_keys(Password)
        test_obj.click_submit()
        
        #5 Click on transfer fund link
        test_obj.clik_transfer_funds()

        #6 Transfer funds
        test_obj.add_from_account()
        test_obj.add_to_account()
        test_obj.transfer_fund()

        #7 Account summary
        test_obj.view_account_summary()

        #Teardown
        test_obj.wait(3)
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter
        test_obj.teardown()
                  
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
        test_altoro_mutual_form(base_url=options.url,
                        browser=options.browser,
                        browser_version=options.browser_version,
                        os_version=options.os_version,
                        os_name=options.os_name,
                        remote_flag=options.remote_flag,
                        testrail_flag=options.testrail_flag,
                        tesults_flag=options.tesults_flag,
                        test_run_id=options.test_run_id,
                        remote_project_name=options.remote_project_name,
                        remote_build_name=options.remote_build_name) 
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())