from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import re

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

### set up list to capture lines in pdf
lines = []
clean = []

### select pattern you want to search for
pattern = 'Ph.D.'  ##set this upto be the list of degrees
spattern = 'Johns Hopkins'


### separate each item in the list by a linebreak
for text in plain_text.split("\n"):
    lines.append(text)

## remove any items in the list that are merely spaces or commas
for line in lines:
    if line != '' and line != ' ':
        clean.append(line)


## find the indicies in clean that contain info found in pattern
indices = [i for i, s in enumerate(clean) if pattern in s]
sindices = [i for i, s in enumerate(clean) if spattern in s]

### find the line previous and the line after the idicies that contain the info i want
## find the items in clean with the indicies at those three spots
education = []
ed_final = []

for i in indices:
    for s in sindices:
        if i == s + 1 or i  == s - 1:
            education.append(i)
            education.append(s)
        if i == s:
            education.append(i)
            education.append(s)


m1 = min(education)
m2 = min(education) + 1



