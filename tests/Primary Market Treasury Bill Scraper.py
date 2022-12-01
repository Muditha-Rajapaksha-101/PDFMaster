# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 00:17:50 2022

@author: MudithaRajapaksha
"""
from PDFTableMaster import PDFTableMaster
from ExcelMaster import ExcelTableMaster
from WebMaster import WebMaster


import re
import datetime

    
#This method should be implemented to define fltering rules
class Cleaner(PDFTableMaster.CleanMaster):
    
    def __init__(self, fileName):
        self.fileName = fileName       
        return
    
    
    def cleanListMaster(self , rows):
        #you have to implement this method with rules to filter out rows
        finalPageList = []
        date = Cleaner.getDate(self.fileName)
       
        
        for row in rows:
            if(len(row) >= 6 and len(row) <= 6):
                if(row[0].strip().startswith("LKA") and len(row[0].strip())  == 12 ):
                    row.insert(0 , date)
                    finalPageList.append(Cleaner.removeComma(row) )   
            
        tenure = [91, 182 , 364]         
        for rowNum in range(3):
            finalPageList[rowNum].insert(2 , tenure[rowNum])
            finalPageList[rowNum].insert(3 , "")
        return finalPageList

    def removeComma(row):
        newRow = []
        newRow.append(row[0])
        newRow.append(row[1])
        
        for item in row[2:]:
            itemNew = item.replace("," , "")
            itemNew = float(itemNew)
            newRow.append(itemNew)
        return newRow
    
    def getDate(fileName):
        dateStr = re.findall(r'\d+' , fileName)[0]
        date = datetime.datetime(int(dateStr[:4]), int(dateStr[4:6]), int(dateStr[-2:]))
        #formatStr = date.strftime("%d/%m/%Y")
        return date
    
    def filterFiles(fileListPrevious , newFileList):
        filteredFileList = [[], []]
        for i in range(len(newFileList[0])):
            if(newFileList[0][i] not in  fileListPrevious[0]):
                filteredFileList[0].append(newFileList[0][i])
                filteredFileList[1].append(newFileList[1][i])
        return filteredFileList


if __name__ == "__main__":
    _websites = [r"https://www.cbsl.gov.lk/en/press/press-releases/government-securities" , "https://www.cbsl.gov.lk/en/press/press-releases/government-securities?page=1" , "https://www.cbsl.gov.lk/en/press/press-releases/government-securities?page=2"]
    _downloadLocation = 'downloaded'
    
    #Downlad New Files
    fileList_previous = PDFTableMaster.getPDFList(_downloadLocation)
    web = WebMaster(_websites)
    downloadFileNameList = web.get_files(hasString="Treasury Bill Auction" , availableFileList = fileList_previous[1] , downloadLocation=_downloadLocation)
    
    #New File List
    tableMaster = ExcelTableMaster( fileName = "Tbill auctions.xlsx", workSheetIndex = 0, tableName = "Table13")
    fileList = Cleaner.filterFiles(fileListPrevious = fileList_previous , newFileList= PDFTableMaster.getPDFList(_downloadLocation))

    
    for fileIndex in range(len(fileList[0])): #for fileIndex in range(0):
        pdfTable = PDFTableMaster(fileList[0][fileIndex]) #Mandatory
        if(pdfTable.table_exists(pageNo=1)):
            pdfTable.set_parameters({'upperBoundry':10, 'lowerBoundry':10 , 'margin':3})
            page_list = pdfTable.get_data_rows_list(pages = [0], clean = True , cleanMaster= Cleaner(fileList[0][fileIndex])) 
            
            
            for row in page_list:
                print(row)
                tableMaster.writeUniqueTableRow( keyColumnLetter =  "B" , keyIndexNo = 1, dataList = row)
        else:
            print("No table found ")
        print("---------------------------------------------------------------------------")
            
            



