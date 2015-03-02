#week4op1.py

import xml.etree.ElementTree as ET
import sys

def main(argv):
	tree = ET.parse(argv[1])
	root = tree.getroot()
	for child in root:
		bottomhz = float(child[5].text)
		tophz = float(child[7].text)
		f0end = float(child[12].text)
		f0start = float(child[13].text)
		"""Checks if f0end and f0start are both between tophz and bottomhz
		if this is not the case, it deletes the whole child""" 
		if not (bottomhz < f0end < tophz) or not (bottomhz < f0start < tophz):
			root.remove(child)
	tree.write(argv[2])

main(sys.argv)
