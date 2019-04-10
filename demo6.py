# import PyPDF2 as pf
# f=open("pandas.pdf","rb")
# d=pf.PdfFileReader(f)
#
# e=d.getPage(0)
# s=e.extractText()
# print s
# f.close()



# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('pandas.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()
