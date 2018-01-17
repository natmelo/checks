from check50 import *
import os

class House(Checks):

    @check()
    def submitted(self):
        """ "Around the House" submitted"""
        if not any(os.path.exists("house.{}".format(extension))
                    for extension in ["doc", "docx", "pdf", "txt"]):
            raise Error("File not found")

#    @check("submitted")
#    def wordcount(self):
#
