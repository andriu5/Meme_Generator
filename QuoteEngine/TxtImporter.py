from typing import List

from .ImportInterface import ImportInterface
from .Cat import Cat

class TxtImporter(ImportInterface):
    allowed_extensions = ['txt']
    
    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
       
        file_ref = open(path, encoding="UTF-8")
        cats = []
        
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split(',')
                new_cat = Cat(parse[0], int(parse[1]), bool(parse[2]))
                cats.append(new_cat)
                
        file_ref.close()
        return cats