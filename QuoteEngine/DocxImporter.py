from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxImporter(IngestorInterface):
    allowed_extensions = ['docx']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
            
        quotes = []
        doc = docx.Document(path)
        
        for para in doc.paragraphs:
            try:
                if para.text != "":
                    parsed = para.text.split('-')
                    new_quote = QuoteModel(parsed[0].strip(), parsed[1].strip())
            except Exception as e:
                print("Line not parsed from DOCX due to: "+str(e))
            else: 
                quotes.append(new_quote)
                
        return quotes