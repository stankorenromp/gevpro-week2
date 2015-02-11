class Country:
	"""Een land class die de naam van het land kan returnen"""
	def __init__(self,naam):
		self.naam = naam
		
	def getName(self):
		return self.naam
		
	def __str__(self):
		return "{0} {1}".format("Hello from",self.naam)
		
def main():
	nl = Country("Netherlands")
	de = Country("Germany")
	en = Country("United Kingdom")
	print(nl,de,en)

main()
