from QuoteEngine import Ingestor

print("1. .pdf: ",Ingestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
quotes = Ingestor.parse('./_data/DogQuotes/DogQuotesCSV.csv')
print("2. .csv: ",quotes, type(quotes))
print("2.1 quote: ",quotes[0].body,", author: ",quotes[0].author)
print("2.2 quote: ",quotes[1].body,", author: ",quotes[1].author)
print("3. .docx: ",Ingestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))
# # print("4. .xls: ",Ingestor.parse('./data/cats.xls'))
# # print("5. .xlsx: ",Ingestor.parse('./data/cats.xlsx'))
print("6. .txt: ",Ingestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))