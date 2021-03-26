class Booklist():
	def __init__(self):
		self.books = []

	def add(self, title, author):
		book = {}
		book['title'] = title
		book['author'] = author
		self.books.append(book)


	def count_books(self):
		return f'There are {len(self.books)} books in the library.'

	def remove_title(self, title):
		for book in self.books:
			if book['title'] == title:
				self.books.pop(self.books.index(book))
				return f'Removing the book "{title}" from the booklist.'
		print(f'Removing the book "{title}" from the booklist.')

	def init_(self):
		self.nyt_bestsellers = []
        
	def count_books(self):
		return len(self.books)

	def count_books(self):
		return len(self.books) 

	def display_titles(self):
		pass
