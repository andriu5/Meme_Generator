from typing import List
import pandas
import openpyxl

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class XlsxImporter(IngestorInterface):
    allowed_extensions = ['xls', 'xlsx']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        quotes = []
        df = pandas.read_excel(path, sheet_name=0, keep_default_na=False, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)
        
        return quotes