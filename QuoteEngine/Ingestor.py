from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .XlsxImporter import XlsxImporter
from .CSVImporter import CSVImporter
from .TxtImporter import TxtImporter
from .DocxImporter import DocxImporter
from .PDFImporter import PDFImporter


class Ingestor(IngestorInterface):
    
    importers = [CSVImporter, XlsxImporter, TxtImporter, DocxImporter, 
                PDFImporter]
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)