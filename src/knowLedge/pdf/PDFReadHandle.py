from  PyPDF2 import  PdfFileReader


with open('./res/Docker入门教程.pdf', 'rb') as f:
    reader = PdfFileReader(f, strict=False)
    print(reader.numPages)
    if reader.isEncrypted:
        reader.decrypt('')
    current_page = reader.getPage(3)
    print(current_page)
    print(current_page.extractText())

