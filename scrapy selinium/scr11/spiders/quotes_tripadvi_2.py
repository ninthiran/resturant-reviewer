# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 11:46:05 2018

@author: naveenthiran
"""


import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

class QuotesTripadvir(scrapy.Spider):
    name = "rating_2"

    start_urls = [
            'https://www.tripadvisor.co.uk/Restaurant_Review-g186338-d1043914-Reviews-The_Blackbird-London_England.html',
        ]
    
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path = 'D:/ProjectMSc/imple/c2/c1/scr11/chromedriver.exe')
       
        

    def parse(self, response):
        csvFile = open('ReviewScraped.csv', 'a', newline='',encoding='utf-8')
        csvWriter = csv.writer(csvFile)
        self.driver.get(response.url)
        time.sleep(5)
        rating_4 = self.driver.find_element_by_id('taplc_location_review_filter_controls_0_filterRating_2')
        rating_4.click()
        time.sleep(2)
        more = self.driver.find_element_by_xpath('//p[@class="partial_entry"]/span')
        more.click()
        
        count = 0
        time.sleep(5)
        review_conts = self.driver.find_elements_by_xpath('//div[@class="review-container"]')
        review_text = (self.driver.find_elements_by_xpath('//span[@class="noQuotes"]'))
        review_content =  (self.driver.find_elements_by_xpath('//p[@class="partial_entry"]'))
        
       
        
        for re_cont in review_conts:
            a =review_text[count].text + review_content[count].text
            csvWriter.writerow([a ,'2'])
            count = count + 1
             

        self.driver.close()
        csvFile.close()