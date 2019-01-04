import unittest
import sqlite3

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from SiwakeRepository import SiwakeRepository
from SiwakeData import SiwakeData


class TestSiwakeSiwakeRepository(unittest.TestCase):
	
	#table確認
	def test_create(self):
		con = sqlite3.connect(":memory:")
		obj = SiwakeRepository(con)
		cursor = con.cursor()
		
		cursor.execute("select * from sqlite_master where type='table'")
		
		for l in cursor.fetchall():
			if 'siwakes' in l:
				self.assertTrue(True)
				return
		self.assertTrue(False)
		
	#カラム確認
	def test_create2(self):
		con = sqlite3.connect(":memory:")
		obj = SiwakeRepository(con)
		cursor = con.cursor()
		
		columns = SiwakeData({}).column_defined()
		names = list(map(lambda d: d['name'], columns))
		types = list(map(lambda d: d['type'], columns))
		
		for x in cursor.execute("PRAGMA TABLE_INFO('siwakes')"):
			if x[1] in names:
				self.assertEqual(x[2], types[names.index(x[1])])
			else:
				self.assertTrue(False)
	
	def test_import_list(self):
		con = sqlite3.connect(":memory:")
		obj = SiwakeRepository(con)
		
		data = [
			(1, 12, '預金', 1000, '売上', 1000, '1月分'),
			(2, 14, '預金', 2000, '売上', 2000, '2月分'),
		]
		obj.import_list(data)
		
		cursor = con.cursor()
		sql = "select * from siwakes ORDER BY no_month, no_date"
		i = 0
		for col in cursor.execute(sql):
			self.assertEqual(col, data[i])
			i += 1
		
	def test_unique_column(self):
		con = sqlite3.connect(":memory:")
		obj = SiwakeRepository(con)
		
		data = [
			(1, 12, '預金', 1000, '売上', 1000, '1月分'),
			(2, 14, '預金', 2000, '売上', 2000, '2月分'),
			(5, 1, '水道光熱費', 5000, '預金', 5000, '5月分'),
			(4, 6, '図書費', 4000, '現金', 4000, '4月分'),
			(3, 22, '水道光熱費', 3000, '現金', 2000, '3月分'),
		]
		obj.import_list(data)
		
		expect = [
			'図書費', '水道光熱費','預金'
		]
		
		self.assertEqual(obj.unique_column('in_kamoku'), expect)
		
	def test_find(self):
		con = sqlite3.connect(":memory:")
		obj = SiwakeRepository(con)
		
		data = [
			(1, 12, '預金', 1000, '売上', 1000, '1月分'),
			(2, 14, '預金', 2000, '売上', 2000, '2月分'),
			(5, 1, '水道光熱費', 5000, '預金', 5000, '5月分'),
			(4, 6, '図書費', 4000, '現金', 4000, '4月分'),
			(3, 22, '水道光熱費', 3000, '現金', 2000, '3月分'),
		]
		obj.import_list(data)
		
		columns = SiwakeData({}).column_names()
		
		expect_data = [
			(1, 12, '預金', 1000, '売上', 1000, '1月分'),
			(2, 14, '預金', 2000, '売上', 2000, '2月分'),
			(5, 1, '水道光熱費', 5000, '預金', 5000, '5月分'),
		]
		
		expect = []
		for ex in expect_data:
			expect.append(dict(zip(columns, ex)))
		
		i = 0
		for x in obj.find('預金'):
			self.assertEqual(x.to_dict(), expect[i])
			i += 1
		
