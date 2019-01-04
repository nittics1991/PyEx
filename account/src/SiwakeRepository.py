import sqlite3
from SiwakeData import SiwakeData

class SiwakeRepository:
	def __init__(self, connection):
		self.__connection = connection
		self.clean().create()
	
	def clean(self):
		sql = 'DROP TABLE IF EXISTS siwakes'
		cursor = self.__connection.cursor()
		cursor.execute(sql)
		return self
	
	def create(self):
		sql = 'CREATE TABLE siwakes ('
		tmp = ''
		
		for items in SiwakeData({}).column_defined():
			tmp += ',' + items['name'] + ' ' + items['type']
		
		sql += tmp[1:len(tmp)]
		sql += ')'
		
		cursor = self.__connection.cursor()
		cursor.execute(sql)
		return self
	
	def import_list(self, list_data):
		sql = 'INSERT INTO siwakes ('
		tmp = ''
		
		columns = SiwakeData({}).column_defined()
		
		for dic in columns:
			tmp += ',' + dic['name']
		sql += tmp[1:len(tmp)]
		
		sql += ') values ('
		
		tmp = ',?' * len(columns)
		sql += tmp[1:len(tmp)]
		
		sql += ')'
		
		cursor = self.__connection.cursor()
		cursor.executemany(sql, list_data)
		return self
		
	def unique_column(self, column_name):
		sql = 'SELECT DISTINCT ' + column_name
		sql += ' FROM siwakes ORDER BY ' + column_name
		
		self.__connection.row_factory = sqlite3.Row
		cursor = self.__connection.cursor()
		cursor.execute(sql)
		
		result = []
		for x in cursor.fetchall():
			result.append(x[0])
		
		return result
	
	def find(self, kamoku):
		sql = '''
			SELECT *
			FROM siwakes
			WHERE in_kamoku = ?
				OR out_kamoku = ?
			ORDER BY no_month, no_date, in_kamoku, out_kamoku
		'''
		
		self.__connection.row_factory = sqlite3.Row
		cursor = self.__connection.cursor()
		result = []
		for l in cursor.execute(sql, (kamoku, kamoku)):
			result.append(SiwakeData({
				'no_month': l['no_month'],
				'no_date': l['no_date'],
				'in_kamoku': l['in_kamoku'],
				'in_money': l['in_money'],
				'out_kamoku': l['out_kamoku'],
				'out_money': l['out_money'],
				'biko': l['biko'],
			}))
		
		return result
