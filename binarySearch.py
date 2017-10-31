class binarySearch(list):
	def __init__(self,highest,step):
		self.step=step
		self.highest=highest

		if highest * step in self.toTwenty():
			self.extend(self.toTwenty())
		elif highest * step in self.toForty():
			self.extend(self.toForty())
		elif highest * step in self.toOneThousand():
			self.extend(self.toOneThousand())

		self.length = len(self)



	def toTwenty(self):
		return range(1,21,1)
	def toForty(self):
	    return range(2,41,2)
	def toOneThousand(self):
		return range(10,1001,10)

	def search(self,number):
		count = 0
		index = 0
		length = len(self)
		first = 0
		last = len(self)-1
		found = False

		if number == self[first]:
			index = first
			found = True
		elif number == self[last]:
			index = last
			found =True
		elif number not in self:
			found = True
			index = -1
		while first<=last and not found:
			midpoint = (first + last)//2
			if self[midpoint] == number:
				found = True
				index = midpoint
			else:
				count+= 1
				if number < self[midpoint]:
					last = midpoint-1
				else:
					first = midpoint+ 1 
		return {'count': count, 'index': index}

