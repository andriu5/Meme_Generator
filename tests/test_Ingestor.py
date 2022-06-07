import unittest
from QuoteEngine import Ingestor, QuoteModel

# print("1. .pdf: ",Ingestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
# quotes = Ingestor.parse('./_data/DogQuotes/DogQuotesCSV.csv')
# print("2. .csv: ",quotes, type(quotes))
# print("2.1 quote: ",quotes[0].body,", author: ",quotes[0].author)
# print("2.2 quote: ",quotes[1].body,", author: ",quotes[1].author)
# print("3. .docx: ",Ingestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))
# # # print("4. .xls: ",Ingestor.parse('./data/cats.xls'))
# # # print("5. .xlsx: ",Ingestor.parse('./data/cats.xlsx'))
# print("6. .txt: ",Ingestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))


class TestIngestor(unittest.TestCase):
    def test_parse_pdf(self):
        pdf_quotes = Ingestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf')
        self.assertEqual(len(pdf_quotes), 4)
        self.assertIsInstance(pdf_quotes[1], QuoteModel)
        self.assertEqual(pdf_quotes[0].body, '"Treat yo self"')
        self.assertEqual(pdf_quotes[0].author, "Fluffles")

    def test_parse_csv(self):
        csv_quotes = Ingestor.parse('./_data/DogQuotes/DogQuotesCSV.csv')
        self.assertEqual(len(csv_quotes), 2)
        self.assertIsInstance(csv_quotes[1], QuoteModel)
        self.assertEqual(csv_quotes[0].body, "Chase the mailman")
        self.assertEqual(csv_quotes[0].author, "Skittle")

    def test_parse_docx(self):
        docx_quotes = Ingestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx')
        self.assertEqual(len(docx_quotes), 5)
        self.assertIsInstance(docx_quotes[1], QuoteModel)
        self.assertEqual(docx_quotes[0].body, '"Bark like no one’s listening"')
        self.assertEqual(docx_quotes[0].author, "Rex")

    # def test_parse_xls(self):
    #     pass
    
    # def test_parse_xlsx(self):
    #     pass

    def test_parse_txt(self):
        txt_quotes = Ingestor.parse('./_data/DogQuotes/DogQuotesTXT.txt')
        self.assertEqual(len(txt_quotes), 2)
        self.assertIsInstance(txt_quotes[1], QuoteModel)
        self.assertEqual(txt_quotes[1].body, 'He who smelt it...')
        self.assertEqual(txt_quotes[1].author, "Stinky")


if __name__ == '__main__':
    unittest.main()