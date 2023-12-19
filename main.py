#Merging pdfs
#Improtant thing: the files must be sorted before execution of the program unless or until you get the same order as the files present in the directory.
#PyPdf is a python library
# while in IDE of your terminal terminal:- for using PyPDF2 module type->    pip install PyPDF2
# i will recommend Pycharm IDE

from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]            #it will check all the pdf files in the folder directory

for pdf in files:
    merger.append(pdf)          #append method used to concatenate the files

merger.write("new_merged.pdf")          #it will write new file named new_merged with extension of pdf
merger.close()                          #then just close the file and you can see within your folder to open ur new pdf file