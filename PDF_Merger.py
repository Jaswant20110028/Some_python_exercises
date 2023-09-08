# This Program is a pdfmerger
import PyPDF2 as p
import os

merger=p.PdfWriter()

l=[file for file in os.listdir() if file.endswith(".pdf")]

for i in l:
    merger.append(i)

merger.write("Merged.pdf")
merger.close()


