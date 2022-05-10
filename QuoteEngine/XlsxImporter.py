from typing import List
import pandas
import openpyxl

from .ImportInterface import ImportInterface
from .Cat import Cat

class XlsxImporter(ImportInterface):
    allowed_extensions = ['xls', 'xlsx']
    
    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        cats = []
        df = pandas.read_excel(path, sheet_name=0, keep_default_na=False, header=0)

        for index, row in df.iterrows():
            new_cat = Cat(row['Name'], row['Age'], row['isIndoor'])
            cats.append(new_cat)
        
        return cats