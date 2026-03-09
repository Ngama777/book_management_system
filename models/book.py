class Book:
    def __init__(self, id, title, author, isbn, publication_year, genre, available):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.genre = genre
        self.available = available
        
        
    def to_dict(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "author" : self.author,
            "isbn" : self.isbn,
            "publication_year" : self.publication_year,
            "genre" : self.genre,
            "available" : self.available
        }   
       