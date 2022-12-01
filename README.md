# PDFMaster Package

This is a PDFTableMaster package. You can use
[Github-flavored Markdown](https://github.com/Muditha-Rajapaksha-101/PDFMaster.git)


Parmeters to adjust
#pdfTable.set_parameters({'upperBoundry':10, 'lowerBoundry':10 , 'margin':3})

-->upperBoundry and lowerBoundry states the upper and lower boundries in the vertical axis to identify rows
-->These values should be modified to fit the PDF table you're about the scrape
-->Margin defines the horizontal bountries of the table ( use to identify columns)


Project will provide you with a unstrucured table structure (Lists inside a list)
-->User shoud implement the CleanMaster Class that comes with the package to define how the cleaning should be done
-->Refer the example.py to get a clear understanding on how you ca use this class
-->cleanListMaster() comes under CleanMaster class will define this functionality


class clean(CleanMaster):
        def cleanListMaster(self , rows):
            #you have to implement this method with rules to filter out rows
            finalPageList = []
            for row in rows:
                if(len(row) >= 6 and len(row) <= 6):
                    if(row[0].strip().startswith("LKA") and len(row[0].strip())  == 12 ):
                        finalPageList.append(clean.removeComma(row) )   
          
            return finalPageList