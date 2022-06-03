from requests import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from urllib import request
import os
import time

class Scraper:
    KEYS = ["resultats-par-niveau-dpt-t1-france-entiere.xlsx", "resultats-par-niveau-reg-t1-france-entiere.xlsx",
        "resultats-par-niveau-dpt-t2-france-entiere.xlsx", "resultats-par-niveau-reg-t2-france-entiere.xlsx"]

    def __init__(self, url):
        self.url = url
        
    def get_result(url,key,result_filename):
        service = FirefoxService(GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service)
        # get to the url
        browser.get(url)
        
        #make the servers think it's a human behind
        time.sleep(3)
        
        #search bar
        element = browser.find_element_by_id('resources.search')
        element.clear()
        # enter data in the bar
        element.send_keys(key)

        #press enter (not you , the program)
        element.send_keys(Keys.ENTER)
        
        time.sleep(3)
        download_link=browser.find_element_by_xpath(
            "//a[@title='Télécharger la ressource']").get_attribute("href")
        complete_filepath= os.path.join("Data/CSV/Results",result_filename)
        response=request.urlretrieve(download_link,complete_filepath)
        
        time.sleep(3)
        browser.close()
        browser.quit()

    