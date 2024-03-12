from collections.abc import Iterable, Iterator

class BookCollection(Iterable):
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)
    
    def __iter__(self):
        return BookIterator(self._books)

class BookIterator(Iterator):
    def __init__(self, books):
        self._books = books
        self._index = 0
    
    def __next__(self):
        try:
            book = self._books[self._index]
        except IndexError:
            raise StopIteration()
        self._index += 1
        return book

if __name__ == "__main__":
    book_collection = BookCollection()
    book_collection.add_book("Book 1")
    book_collection.add_book("Book 2")
    book_collection.add_book("Book 3")

    for book in book_collection:
        print(book)
