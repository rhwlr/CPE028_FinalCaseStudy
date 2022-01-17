import logging 
from pyats import aetest
 
log = logging.getLogger(__name__) 
 
class common_setup(aetest.CommonSetup): 
    """ Common Setup section """ 
 
    @aetest.subsection 
    def sample_subsection_1(self): 
        """ Common Setup subsection """ 
        log.info("Aetest Common Setup ") 
 
    @aetest.subsection 
    def sample_subsection_2(self, section): 
        """ Common Setup subsection """ 
        log.info("Inside %s" % (section)) 
 
        log.info("Inside class %s" % (self.uid)) 
 
class tc_one(aetest.Testcase): 
    """ This is user Testcases section """ 
 
    @aetest.setup 
    def prepare_testcase(self, section): 
        """ Testcase Setup section """ 
        log.info("Preparing the test") 
        log.info(section) 
 
    @ aetest.test 
    def simple_test_1(self): 
        """ Sample test section. Only print """ 
        log.info("First test section ") 
 
    @ aetest.test 
    def simple_test_2(self): 
        """ Sample test section. Only print """ 
        log.info("Second test section ") 
 
    @aetest.cleanup 
    def clean_testcase(self): 
        """ Testcase cleanup section """ 
        log.info("Pass testcase cleanup") 
 
 
class tc_two(aetest.Testcase): 
    """ This is user Testcases section """ 
 
    @ aetest.test 
    def simple_test_1(self): 
        """ Sample test section. Only print """ 
        log.info("First test section ") 
        self.failed('This is an intentional failure') 
 
    @ aetest.test 
    def simple_test_2(self): 
        """ Sample test section. Only print """ 
        log.info("Second test section ") 
 
    @aetest.cleanup 
    def clean_testcase(self): 
        """ Testcase cleanup section """ 
        log.info("Pass testcase cleanup") 
 
class common_cleanup(aetest.CommonCleanup): 
    """ Common Cleanup for Sample Test """ 
 
    @aetest.subsection 
    def clean_everything(self): 
        """ Common Cleanup Subsection """ 
        log.info("Aetest Common Cleanup ") 
 
if __name__ == '__main__': 
    result = aetest.main() 