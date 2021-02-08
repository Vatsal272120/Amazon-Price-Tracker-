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

class GenerateReport:
    def __init__(self):
        pass


class AmazonAPI :
    def __init__(self, search_term, filters, base_url, currency):

        self.base_url = base_url
        self.search_term = search_term
        options = get_web_driver_options()
        set_ignore_certificate_error(options)
        set_browser_as_incognito(options)
        self.driver = get_chrome_web_driver(options)
        self.currency = currency
        self.price_filter = f"&rh=p_36%3A{filters['min']}00-{filters['max']}00"

    def run (self):
            print("script starting")
            print(f'Looking for the {self.search_term}')
            # the function gets the links for all the products and stores in link variable
            links = self.get_products_links()

           

    def get_products_links(self):
            self.driver.get(self.base_url)
            

           










""" to run the file """
if __name__ == '__main__':
   amazon = AmazonAPI(NAME, FILTERS, BASE_URL, CURRENCY) 
   amazon.run()
   