import pdfplumber
from PyPDF2 import PdfFileMerger, PdfFileReader

def extract_investor_name(filename):
    #get number of pages from file
    page_reader = PdfFileReader(filename)
    no_of_pages = page_reader.getNumPages()
    #investor name is found on every 2nd page, PN is 5 pages long -> 20 -> 2,7,12,17
    number_of_PNs = no_of_pages // 5
    for page in range(number_of_PNs):
        page_number = page * 5 + 1
        with pdfplumber.open(filename) as pdf:
            target_page = pdf.pages[page_number]
            table = target_page.extract_tables(table_settings={})
            investor_name = table[0][1][1]
        investor_names.append(investor_name)
    return investor_names

def combine_pdf(investor_index, investor_name):
    merger = PdfFileMerger()
    # add the page 1 to output document

    PN_pg1_start = investor_index
    PN_pg1_stop = investor_index + 1

    merger.append(fileobj=allpage1, pages=(PN_pg1_start, PN_pg1_stop))

    # add the rest of the PN to output document (4 pages)

    PN_pg_2nd_half_start = (investor_index + 1) * no_PN_pages - (no_PN_pages - 1)
    PN_pg_2nd_half_stop = (investor_index + 1) * no_PN_pages

    merger.merge(position=1, fileobj=target, pages=(PN_pg_2nd_half_start, PN_pg_2nd_half_stop))
    # name the document appropriately
    doc_name = investor_name + '.pdf'

    if doc_name in file_name_count:
        file_name_count[doc_name] += 1
        new_doc_name = investor_name + str(file_name_count[doc_name]) + '.pdf'
        output = open(new_doc_name,"wb")
        merger.write(output)
        merger.close()
    else:
        output = open(doc_name,"wb")
        merger.write(output)
        merger.close()
        file_name_count[doc_name] = 1


investor_names = [] #initialize empty list to hold the list of investors
file_name_count = {} # initialize empty dictionary to check for duplicate filename
file_list = ['target.pdf']

for file in file_list:
    extract_investor_name(file)

allpage1 = open("allpage1.pdf","rb") # All of pg1 of PNs
target = open("target.pdf","rb") # All of unsigned PNs


number_of_investors = len(investor_names)
no_PN_pages = 5 # Current number of pages in PN

for investor_index in range(number_of_investors):
    investor_name = investor_names[investor_index]
    combine_pdf(investor_index,investor_name)


