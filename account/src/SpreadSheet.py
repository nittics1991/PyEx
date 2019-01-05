import pyexcel

from pyexcel_ods import save_data

class SpreadSheet:
	
	def __init__(self, book_name):
		self.__book_name = book_name
		self.open(book_name)
	
	def open(self, book_name):
		self.__book = pyexcel.get_book(file_name=book_name)
		
	def export(self, sheet_name):
		dic = self.__book.to_dict()
		return dic[sheet_name]
		
	def write(self, dict_data):
		dic = self.__book.to_dict()
		dic.update(dict_data)
		
		book = pyexcel.Book(dic)
		book.save_as(self.__book_name)
		
	def write_ods(self, dict_data):
		dic = self.__book.to_dict()
		dic.update(dict_data)
		
		save_data(self.__book_name + '.ods', dic)
