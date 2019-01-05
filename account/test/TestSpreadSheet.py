import unittest

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from SpreadSheet import SpreadSheet

class TestSpreadSheet(unittest.TestCase):
	
	def test_export(self):
		file_path = os.path.join(os.path.dirname(__file__), 'data.xlsx')
		obj = SpreadSheet(file_path)
		actual = obj.export('シート1')
		expect = [
			['date', 'data'],
			[1, 'A'],
			[2, 'B'],
			[3, 'C'],
		]
		self.assertEqual(actual, expect)
		
	
	def test_export(self):
		file_path = os.path.join(os.path.dirname(__file__), 'data.xlsx')
		obj = SpreadSheet(file_path)
		
		data = {'newsheet': [
			['date', 'data'],
			[1, 'A'],
			[2, 'B'],
			[3, 'C'],
		]}
		
		obj.write(data)
		
		
		
		
		
		
		
