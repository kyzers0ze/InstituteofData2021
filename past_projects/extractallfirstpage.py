from PyPDF2 import PdfFileMerger

def extract_all_PN_first_page(no_of_pages,filename):
    merger = PdfFileMerger()
    pdf_file = open(filename,"rb")
    #append the first page
    merger.append(fileobj=pdf_file,pages=(0,no_of_pages,no_PN_pages))
    output = open("all_first_pages.pdf", "wb")
    merger.write(output)

PN_last_page = 100 # Last page of pdf file
no_PN_pages = 5 # Current number of pages in PN

extract_all_PN_first_page(PN_last_page,'target.pdf')
