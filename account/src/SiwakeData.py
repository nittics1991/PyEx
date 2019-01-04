class SiwakeData:
	__column_names = [
		'no_month',
		'no_date',
		'in_kamoku',
		'in_money',
		'out_kamoku',
		'out_money',
		'biko',
	]
	
	__column_types = [
		'integer',
		'integer',
		'text',
		'integer',
		'text',
		'integer',
		'text',
	]
	
	def __init__(self, init_dict):
		self.__data = {}
		self.from_dict(init_dict)
	
	def from_dict(self, dict_data):
		for key, val in dict_data.items():
			if key in self.__column_names:
				self.__data[key] = val
	
	def has(self, name):
		return name in self.__column_names
	
	def get(self, name):
		if not self.has(name):
			raise TypeError('not has name:' + name)
		return self.__data[name]
	
	def column_names(self):
		return self.__column_names
	
	def column_types(self):
		return self.__column_types
	
	def column_defined(self):
		result = []
		for name, typed in zip(self.__column_names, self.__column_types):
			result.append({'name': name, 'type': typed})
		return result
	
	def to_dict(self):
		return self.__data
		
