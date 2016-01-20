#!/usr/bin/python
import argparse
import csv



class CsvTransformer:
	def __init__(self, inputFile):
		self.description = 'Transforms the raw downloaded transactions from RBC into a useable format for my Numbers sheet'
		self.author = 'Craig Adam <craig@adam11.ca>'
		self.inputFile = inputFile


	def start(self):
		with open(self.inputFile) as csvFile:
			dialect = csv.Sniffer().sniff(csvFile.read(1024))
			csvFile.seek(0)
			reader = csv.reader(csvFile, dialect)
			for row in reader:
				self.parseRow(row)
			csvFile.close()

	def parseRow(self, row):
		print ' -- '.join(row)