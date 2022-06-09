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
        
    def get_result(self,id_key):
        service = FirefoxService(GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service)
        # get to the url
        browser.get(self.url)
        
        #make the servers think it's a human behind
        time.sleep(3)
        
        #search bar
        element = browser.find_element_by_id('resources.search')
        element.clear()
        # enter data in the bar
        element.send_keys(self.KEYS[id_key])

        #press enter (not you , the program)
        element.send_keys(Keys.ENTER)
        
        time.sleep(3)
        download_link=browser.find_element_by_xpath(
            "//a[@title='Télécharger la ressource']").get_attribute("href")
        path=""
        
        if id_key==0:
            path="Data/XLSX/Results/Departement/First_Round/"
            pass
        if id_key==1:
            path="Data/XLSX/Results/Region/First_Round/"
            pass
        if id_key==2:
            path="Data/XLSX/Results/Departement/Second_Round/"
            pass
        if id_key==3:
            path="Data/XLSX/Results/Region/Second_Round/"
            pass

        complete_filepath= os.path.join(path,self.KEYS[id_key])
        response=request.urlretrieve(download_link,complete_filepath)
            
        time.sleep(3)
        browser.close()
        browser.quit()
if __name__=="__main__":
    
    scrapFirstRound=Scraper("https://www.data.gouv.fr/fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/")
    scrapFirstRound.get_result(0)
    scrapFirstRound.get_result(1)
    scrapSecondRound=Scraper("https://www.data.gouv.fr/fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-2nd-tour/")
    scrapSecondRound.get_result(2)
    scrapSecondRound.get_result(3)
    