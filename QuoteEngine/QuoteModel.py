class QuoteModel():
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author

    def speak(self):
        print(f'rrr"')
    
    def __repr__(self):
        return f'<QuoteModel Object: {self.quote}, {self.author}>'

    def __str__(self):
        return f'"{self.quote}" by {self.author}.'