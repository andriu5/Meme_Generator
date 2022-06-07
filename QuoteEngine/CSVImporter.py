from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVImporter(IngestorInterface):
    allowed_extensions = ['csv']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse a text Quote of the form body, author """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        quotes = []
        df = pandas.read_csv(path, header=0)
        
        for index, row in df.iterrows():
            try:
                new_quote = QuoteModel(row['body'], row['author'])
            except Exception as e:
                print("Line not parsed from CSV due to: "+str(e))
            else: 
                quotes.append(new_quote)
        
        return quotes