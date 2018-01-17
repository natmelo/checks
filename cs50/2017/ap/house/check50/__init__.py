from check50 import *
import os

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
        # get filename
        content = File("house.txt").read()

        # get wordcount
        wordcount = len(content.split())
        raise Error(wordcount)