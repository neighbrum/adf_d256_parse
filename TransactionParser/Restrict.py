import re
import types
class Restrict:
	_str = ""

	@staticmethod
	def clear():
		self._str = ""

	def __init__(self, value):
		self.value = value
		self.successful = True
		Restrict.str = ""

	def AND(self):
		if not self.successful:
			return self
		return self
	
	def OR(self):
		if not self.successful:
			self.successful = True
		return self
	
	def hasFailed(self):
		return not self.successful

	def toBe(self, cmp):
		if not self.successful:
			return self
		Restrict.str = f'restrict {self.value} to be {cmp}'
		expr = False
		try:
			expr = (self.value is cmp)
		except Exception:
			Restrict.str += " exception caught in Restrict::toBe"
			self.successful = False
			return self
		self.successful = True if expr else False
		return self

	def toEqual(self, cmp):
		if not self.successful:
			return self
		Restrict.str = f'restrict {self.value} to equal {cmp}'
		expr = False
		try:
			expr = (self.value == cmp)
		except Exception:
			Restrict.str += " exception caught in Restrict::toEqual"
			return self
		self.successful = True if expr else False
		return self

	def toBeIn(self, iteratable, key=None):
		if not self.successful:
			return self
		iter_str = str(iteratable[0:10])
		if len(iteratable[0:10]) > 11:
			iter_str = iter_str[:-1] + "..." 
		Restrict.str = f'restrict {self.value} to be in {iter_str}'
		elements = iteratable
		if isinstance(key, types.LambdaType):
			try:
				elements = map(key, iteratable)
			except ValueError:
				Restrict.str += " ValueError exception in Restrict::toBeIn"
				self.successful = False
				#raise StopIteration("Restrict::toBeIn key could not be applied")
		self.successful = True if self.value in elements else False
		return self
	
	def toBeDate(self):
		if not self.successful:
			return self
		self.toMatch(r"^[0-9]{6}$")
		Restrict.str = f'restrict {self.value} to be a date'
		return self

	def toBeDayOfYear(self):
		if not self.successful:
			return self
		self.toMatch(r"^[0-9]{3}$")
		Restrict.str = f'restrict {self.value} to be a day of year'
		return self
	
	def toBeLeftAligned(self, fillWith=r'\s'):
		if not self.successful:
			return self
		self.toMatch(re.compile(r"^[^"+fillWith+r"]*["+fillWith+r"]*$"))
		Restrict.str = f'restrict {self.value} to be left aligned and "{fillWith}" filled'
		return self

	def toBeRightAligned(self, fillWith=r'\s'):
		if not self.successful:
			return self
		self.toMatch(re.compile(r"^["+fillWith+r"]*[^"+fillWith+r"]*$"))
		Restrict.str = f'restrict {self.value} to be right aligned and "{fillWith}" filled'
		return self
	
	def haveADigit(self):
		if not self.successful:
			return self
		re.compile(r".*\d.*").match(self.value)
		Restrict.str = f'restrict {self.value} to have atleast one digit'
		return self
	
	def toBeUpperCase(self):
		if not self.successful:
			return self
		re.compile(r"[A-Z]").match(self.value)
		Restrict.str = f'restrict {self.value} to be upper case'
		return self

	def toBeLowerCase(self):
		if not self.successful:
			return self
		re.compile(r"[a-z]").match(self.value)
		Restrict.str = f'restrict {self.value} to be lower case'
		return self
	
	def haveCharAt(self, char, index):
		if not self.successful:
			return self
		Restrict.str = f'restrict {self.value} to have {char} at index {index}'
		if len(self.value) > index:
			Restrict.str += " IndexError caught in Restrict::haveCharAt"
			raise IndexError
		self.successful =  True if self.value[index] == char else False
		return self
	
	def toNotBeAll(self, char):
		if not self.successful:
			return self
		re.compile(r".*[^"+char+r"]+.*").match(self.value)
		Restrict.str = f'restrict {self.value} to have atleast one character different than "{char}"'
		return self
	
	def toSpanSubfields(self, single_char_fields):
		if not self.successful:
			return self
		Restrict.str = f'restrict {self.value} to have atleast one character in each respective field {single_char_fields}'
		split_value = self.value[::len(single_char_fields[0][0])]
		for i in range(0,len(single_char_fields)):
			if not(split_value[i] in single_char_fields[i]):
				self.successful = False
		return self

	def toMatch(self, regex):
		if not self.successful:
			return self
		Restrict.str = f'restrict {self.value} by exactly matching {str(regex)}'
		self.successful = True if re.compile(regex).match(self.value) else False 
		return self

def restrict(value):
	return Restrict(value)