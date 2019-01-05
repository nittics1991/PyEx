import os
import pyexcel
from pyexcel_ods import save_data
from pyexcel_ods import get_data

class SpreadSheet:
	
	def __init__(self, book_name):
		self.__book_name = book_name
		self.open(book_name)
	
	def open(self, book_name):
		spited = os.path.splitext(book_name)
		self.__ext = spited[1]
		
		if self.__ext == '.ods':
			self.__book = get_data(book_name)
		else:
			self.__book = pyexcel.get_book(file_name=book_name)
		
	def export(self, sheet_name):
		dic = self.__book.to_dict()
		return dic[sheet_name]
		
	def write(self, dict_data, type = 'ods'):
		dic = self.__book.to_dict()
		dic.update(dict_data)
		
		if type == 'ods':
			save_data(self.__book_name + '.ods', dic)
		else:
			book = pyexcel.Book(dic)
			book.save_as(self.__book_name + '.xlsx')
