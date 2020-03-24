from docx2python import docx2python
import PyPDF2
from docx2pdf import convert

convert("sample.docx", "output.pdf")

# word_text = []

pdf_text = ""
word_text = ""

with open('output.pdf', mode='rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(0)
    word_text+=page.extractText()

with open('hehe.pdf', mode='rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(0)
    pdf_text+=page.extractText()


# print(word_text)

# print("\n\n")

# print(pdf_text)

if word_text == pdf_text:
    print("Same")

else:
    print("dif")