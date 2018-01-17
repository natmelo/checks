from check50 import *
import os
import readDocx

class House(Checks):

    @check()
    def submitted(self):
        """ "Around the House" submitted"""
        if not any(os.path.exists("house.{}".format(extension))
                    for extension in ["doc", "docx", "pdf", "txt"]):
            raise Error("File not found")

    @check("submitted")
    def wordcount(self):
        """ "Should be >= 400 words" """
        content = ""

#        if os.path.exists("house.pdf"):
#            pdfFileObj = open("house.pdf", "rb")
#            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        if os.path.exists("house.doc"):
            content = readDocx.getText("house.doc")
        else:
            content = File("house.txt").read()

        # get wordcount
        wordcount = len(content.split())

        raise Error(wordcount)
#        if wordcount < 400:
#            raise Error("Word count less than 400")