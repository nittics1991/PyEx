import unittest

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from SiwakeData import SiwakeData

class TestSiwakeData(unittest.TestCase):
	
	def test_from_dict(self):
		#プロパティあり
		x = {'no_month': 11}
		obj = SiwakeData(x)
		
		actual = obj.has('no_month')
		self.assertTrue(actual)
		
		actual = obj.get('no_month')
		self.assertEqual(actual, 11)
		
		#プロパティなし
		x = {'XXX': 11}
		obj = SiwakeData(x)
		
		actual = obj.has('XXX')
		self.assertFalse(actual)
		
		#複数
		x = {'no_year': 11, 'no_date': 23}
		obj = SiwakeData(x)
		
		actual = obj.has('no_month')
		self.assertTrue(actual)
		
		actual = obj.has('no_date')
		self.assertTrue(actual)
		
		actual = obj.get('no_date')
		self.assertEqual(actual, 23)
		
	def test_get_exception(self):
		x = {'XXX': 11}
		obj = SiwakeData(x)
		
		with self.assertRaises(TypeError):
			obj.get('XXX')
	
	def test_column_defined(self):
		x = {'no_month': 11, 'no_date': 23}
		obj = SiwakeData(x)
		expect = [
			{'name': 'no_month', 'type': 'integer'},
			{'name': 'no_date', 'type': 'integer'},
			{'name': 'in_kamoku', 'type': 'text'},
			{'name': 'in_money', 'type': 'integer'},
			{'name': 'out_kamoku', 'type': 'text'},
			{'name': 'out_money', 'type': 'integer'},
			{'name': 'biko', 'type': 'text'},
		]
		self.assertEqual(obj.column_defined(), expect)

	def test_to_dict(self):
		x = {'no_month': 11, 'no_date': 23}
		obj = SiwakeData(x)
		expect = {'no_month': 11, 'no_date': 23}
		self.assertEqual(obj.to_dict(), expect)

	def test_column_names(self):
		obj = SiwakeData({})
		expect = [
			'no_month',
			'no_date',
			'in_kamoku',
			'in_money',
			'out_kamoku',
			'out_money',
			'biko',
		]
		self.assertEqual(obj.column_names(), expect)

	def test_column_types(self):
		obj = SiwakeData({})
		expect = [
		'integer',
		'integer',
		'text',
		'integer',
		'text',
		'integer',
		'text',
		]
		self.assertEqual(obj.column_types(), expect)
		
		