# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 09:40:01 2022

@author: MudithaRajapaksha
"""
from bs4 import BeautifulSoup as bs
import requests
import re

class WebMaster:
    
    def __init__(self, websites):
        self.websites = websites       
        return
    
    def get_files(self , hasString ,  availableFileList , downloadLocation):
        downloadList = []
        for website in self.websites:
            page = requests.get(website)
            soup = bs(page.content, 'html.parser')
            for link in soup.find_all("a", text = re.compile(hasString)):
                fileName = link['href'].split("/")[-1]
                if fileName not in availableFileList:
                    print(fileName , " - Not found")
                    downloadList.append(fileName)
                    WebMaster.download_file_from_link(link['href'], fileName , downloadLocation)
                else:
                    print(fileName , " - found")
                
        return downloadList
    
    
    def download_file_from_link(URL , fileName ,downloadLocation):
        #URL = "https://instagram.com/favicon.ico"
        response = requests.get(URL)
        open("{}/{}".format(downloadLocation ,fileName), "wb").write(response.content)