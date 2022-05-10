from typing import List
import docx

from .ImportInterface import ImportInterface
from .Cat import Cat

class DocxImporter(ImportInterface):
    allowed_extensions = ['docx']
    
    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
            
        cats = []
        doc = docx.Document(path)
        
        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.split(',')
                new_cat = Cat(parsed[0], int(parsed[1]), bool(parsed[2]))
                cats.append(new_cat)
                
        return cats