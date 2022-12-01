# PDFMaster
A custom and Flexible module to scrape data from an editable PDF

## Installting The Package
--------------------
pip install PDFMaster.


## Getting Started
---------------------
You need the following two modules into your project. Please note that the cleaning funciton is optional.

-from PDFMaster.PDFTableMaster import PDFTableMaster
-from PDFMaster.PDFTableMaster import CleanMaster



## Initial Step ob creating Objects
---------------------
### Project will provide you with a unstrucured table structure (Lists inside a list)

> - First you need to create a PDFTableMaster object using its constructor as folows.

`pdfTable = PDFTableMaster("data.pdf")`.


> -  If you want to scrapeonly selected set of pages in your PDF file , You can use the following method to identify those pages.
    identify_Pages_To_Scrape() excepts a list where you could provide specific keywords that can be found in your selected set of pages .

pages = pdfTable.identify_Pages_To_Scrape(["A"]).


> -  You can extract those pages to a new pdf file with the following line of code.
    
`fileNew = pdfTable.extract_PDF_Pages_To_NewFile(pages) #Optional`.


## Adjusting Parameters to fit your model
---------------------
`pdfTable.set_parameters({'upperBoundry':10, 'lowerBoundry':10 , 'margin':3})`.

> - You need to provide above 3 main parameter to help the program identify horizontal and vertical boundries of the PDF table.
> - upperBoundry and lowerBoundry states the upper and lower boundries in the vertical axis to identify rows.
> - These values should be modified to fit the PDF table you're about the scrape.
> - Margin defines the horizontal bountries of the table ( use to identify columns).


## Cleaning Your Model
----------------------

> - Cleaning should by done by the user before the table is converted into a Pandas Dataframe.
> - User must implement the abstract class "CleanMaster" that comes with the PDFMaster paachage to define your cleaning policies.
> - cleanListMaster() method comes under CleanMaster class should define this functionality .
> - Refer the example.py to get a clear understanding on how you can use this class.

`class clean(CleanMaster):
        def cleanListMaster(self , rows):
            #you have to implement this method with rules to filter out rows
            finalPageList = []
            for row in rows:
                if(len(row) >= 6 and len(row) <= 6):
                    if(row[0].strip().startswith("LKA") and len(row[0].strip())  == 12 ):
                        finalPageList.append(clean.removeComma(row) )   
          
            return finalPageList`.
