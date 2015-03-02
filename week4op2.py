#week4op2.py

from collections import namedtuple
import json

def main():
	jsonbestand = open('blood-die.json')
	data = json.load(jsonbestand)
	lijstlijst = []
	Land = namedtuple('Land','taalnaam,classificatie,bloedwoorden,sterfwoorden')
	for lijst in data:
		landnaam = lijst[0]
		landclassificatie = lijst[1]
		woorden1 = lijst[2].split(',')
		woorden2 = lijst[3].split(',')
		[lijstlijst.append(Land(landnaam,landclassificatie,woorden1,woorden2)) for woord1 in woorden1 if woord1 in woorden2]
	print(lijstlijst)
	
main()
