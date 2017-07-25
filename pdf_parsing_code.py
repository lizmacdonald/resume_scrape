from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager() 
    retstr = StringIO()
    device = TextConverter(rsrcmgr, retstr, laparams=LAParams())
    fp = file('MacDonald_CV.pdf', 'rb') # Open the file for reading ('rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    text = retstr.getvalue()
    fp.close() # Close the file
    device.close()
    retstr.close()
    return text


plain_text = convert_pdf_to_txt("MacDonald_CV.pdf")