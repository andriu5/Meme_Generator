from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TxtImporter(IngestorInterface):
    allowed_extensions = ['txt']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
       
        file_ref = open(path, encoding="UTF-8")
        quotes = []
        
        for line in file_ref.readlines():
            line = line.strip('\n\r').replace(" ", "")
            if len(line) > 0:
                parse = line.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
                
        file_ref.close()
        return quotes