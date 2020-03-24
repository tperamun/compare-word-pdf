from docx2python import docx2python
import PyPDF2


word_text = []

pdf_text = ""

hell = docx2python('sample.docx')
word_text= hell.text

with open('hehe.pdf', mode='rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(0)
    pdf_text+=page.extractText()


print(word_text)

print("\n\n")

print(pdf_text)
