import time
from selenium.webdriver.common.keys import Keys

from amazon_config import (
    get_web_driver_options,
    get_chrome_web_driver,
    set_ignore_certificate_error,
    set_browser_as_incognito,
    set_automation_as_head_less,
    NAME,
    CURRENCY,
    FILTERS,
    BASE_URL,
    DIRECTORY
)


# this class generates reports from the data from the Amazon Api 
class GenerateReport:
    def __init__(self):
        pass


# this class gets the links for the product
class AmazonAPI :
   def __init__(self) :
       pass










""" to run the file """
if __name__ == '__main__':
   amazon = AmazonAPI(NAME, FILTERS, BASE_URL, CURRENCY) 
   amazon.run()
   