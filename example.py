# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 12:27:26 2022

@author: MudithaRajapaksha
"""


from PDFMaster.PDFTableMaster import PDFTableMaster
from PDFMaster.PDFTableMaster import CleanMaster





if __name__ == "__main__":
    
    
    #This method should be implemented to define fltering rules
    class clean(CleanMaster):
        def cleanListMaster(self , rows):
            #you have to implement this method with rules to filter out rows
            finalPageList = []
            for row in rows:
                if(len(row) >= 6 and len(row) <= 6):
                    if(row[0].strip().startswith("LKA") and len(row[0].strip())  == 12 ):
                        finalPageList.append(clean.removeComma(row) )   
          
            return finalPageList
    
        def removeComma(row):
            newRow = []
            newRow.append(row[0])
            
            for item in row[1:]:
                itemNew = item.replace("," , "")
                newRow.append(itemNew)
            return newRow
        
        
    
    pdfTable = PDFTableMaster("data.pdf") #Mandatory
    
    pages = pdfTable.identify_Pages_To_Scrape(["A"]) #optional
    
    #fileNew = pdfTable.extract_PDF_Pages_To_NewFile(pages) #Optional
    
    #page_layouts = pdfTable.extract_page_layouts() #Optional
    
    pdfTable.set_parameters({'upperBoundry':10, 'lowerBoundry':10 , 'margin':3})
    
    
    page_list = pdfTable.get_data_rows_list(pages = [0], clean = True , cleanMaster= clean()) 
   
    page_pandas = pdfTable.get_data_rows_pandas(pages = [0] , columns = ["A" , "B" , "C" , "D" , "E" , "F"] , clean = True ,cleanMaster= clean() )
    
    #pdfTable.write_Data_To_Excel( [0], "data.xlsx")
    
      
    for i in page_list:
        print(i)
        print("---------------------------------------------------------------------------")
    
    print(page_pandas)
    print("================================ Program Finished =========================================")
    
    


    