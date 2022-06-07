from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import libs.config as cf
class PDFImporter(IngestorInterface):
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse a text Quote of the form body, author """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        tmp = cf.SERVER_PATH+f'/tmp/{random.randint(0,100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])
        
        file_ref = open(tmp, "r")
        quotes = []
        
        for line in file_ref.readlines():
            try:
                line = line.strip('\n\r')
                if len(line) > 0:
                    parse = line.split('-')
                    new_quote = QuoteModel(parse[0].strip(), parse[1].strip())
            except Exception as e:
                print("Line not parsed from PDF due to: "+str(e))
            else: 
                quotes.append(new_quote)
                
        file_ref.close()
        os.remove(tmp)
        return quotes