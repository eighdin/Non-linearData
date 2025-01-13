import PyPDF4
from datetime import datetime
def getdocumentinformationpdf():
    file = 'sample.pdf'
    fileObj = open(file,"rb")
    #The below line initialize PdfFileReader constructor with pdf file object
    pdf = PyPDF4.PdfFileReader(fileObj)
    #getDocumentInfo() is the PdfFileReader method that returns pdf doc metadata
    information = pdf.getDocumentInfo()
    print(information)
    creation_date = information["/CreationDate"].replace("'","")
    formatted_date = datetime.strptime(creation_date,"D:%Y%m%d%H%M%S%z")
    print(formatted_date)

# PDF Date format is a string of the form (D:YYYYMMDDHHmmSSOHH'mm')
# Where ,
# YYYY is the year
# MM is the month
# DD is the day (01-31)
# HH is the hour (00-23)
# mm is the minute (00-59)
# SS is the second (00-59)
# O is the relationship of local time to Universal Time (UT), denoted by one of the
# characters +, -, or Z
# HH followed by ' is the absolute value of the offset from UT in hours (00-23)
# mm followed by ' is the absolute value of the offset from UT in minutes (00-59)

def print_all_text_pdf():
    file = 'sample.pdf'
    fileObj = open(file,"rb")
    pdf = PyPDF4.PdfFileReader(fileObj)
    #.pages is an iterable attribute that returns all the pages
    for page in pdf.pages:
        print(page.extractText())

def get_text_one_page():
    file = 'sample.pdf'
    fileObj = open(file,"rb")
    pdf = PyPDF4.PdfFileReader(fileObj)
    #.getPage(index) returns specific page object. Index 0 refers to page 1
    page1 = pdf.getPage(0)
    #To extract text from page object, extractText() is used
    print(page1.extractText())

def extract_a_page():
    file1 = 'sample.pdf'
    file2 = "outputFile.pdf"
    file1Obj = open(file1,"rb")#Opening an existing file
    file2Obj = open(file2,"wb")#Creating and opening file2 (pdf)
    pdf1 = PyPDF4.PdfFileReader(file1Obj)
    pdf2 = PyPDF4.PdfFileWriter()
    #Extracting the first page from file1
    page1 = pdf1.getPage(0)
    #Adding the extracted page to PdfFileWriter object
    pdf2.addPage(page1)
    #Writing the extracted page to file2
    pdf2.write(file2Obj)

def extract_some_pages():
    file1 = 'non-linear hw assignment 3.pdf'
    file2 = "outputFile.pdf"
    file1Obj = open(file1,"rb")#Opening an existing file
    file2Obj = open(file2,"wb")#Creating and opening file2 (pdf)
    pdf1 = PyPDF4.PdfFileReader(file1Obj)
    pdf2 = PyPDF4.PdfFileWriter()
    start_page = int(input("Enter the starting page:"))
    last_page = int(input("Enter the last page:"))
    #Extracting a range of pages from file1 and adding them to PdfFileWriter
    object
    for index in range(start_page-1,last_page):
        page = pdf1.getPage(index)
        pdf2.addPage(page)
    #Writing the pages to file2
    pdf2.write(file2Obj)

def merging_multiple_pdfs():
    file_list = ['document1.pdf', 'document2.pdf']
    merged_file = "outputFile.pdf"
    merged_fileObj = open(merged_file,"wb")
    pdf_merger = PyPDF4.PdfFileMerger()
    for file in file_list:
        pdf_merger.append(file) #appends each file to PdfFileMerger object
    #Finally writing to outputFile.pdf
    pdf_merger.write(merged_fileObj)

def encrypt_pdf_w_pass():
    file1 = 'document.pdf'
    file2 = "encrypted_document.pdf"
    file1Obj = open(file1,"rb")#Opening an existing file
    file2Obj = open(file2,"wb")#Creating and opening file2 (pdf)
    pdf1 = PyPDF4.PdfFileReader(file1Obj)
    pdf2 = PyPDF4.PdfFileWriter()
    #Extracting a range of pages from file1 and adding them to PdfFileWriter
    object
    for index in range(0,pdf1.getNumPages()): #getNumPages() gives the number of pages in a pdf file
        page = pdf1.getPage(index)
        pdf2.addPage(page)
    #Encrypting all the pages with user password
    password = input("Enter the password to encrypt:")
    pdf2.encrypt(user_pwd=password)
    #Writing the pages to file2
    pdf2.write(file2Obj)