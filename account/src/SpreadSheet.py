import pyexcel

class SpreadSheet:
	
	def __init__(self, book_name):
		self.__book_name = book_name
		self.open(book_name)
	
	def open(self, book_name):
		self.__sheets = pyexcel.get_book(file_name=book_name)
		
	def export(self, sheet_name):
		dic = self.__sheets.to_dict()
		return dic[sheet_name]
		

		
