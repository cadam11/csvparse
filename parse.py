#!/usr/bin/python
import argparse
import csv

def main():
	parser = argparse.ArgumentParser(description='Command line utility for parsing RBC transaction export csv files')
	parser.add_argument('inputFile', help='The name of the csv file to parse')

	args = parser.parse_args()

	with open(args.inputFile) as csvFile:
		dialect = csv.Sniffer().sniff(csvFile.read(1024))
		csvFile.seek(0)
		reader = csv.reader(csvFile, dialect)
		for row in reader:
			parseRow(row)
		csvFile.close()



#------------------------------------------------------------------------------#

def parseRow(row):
	print ' -- '.join(row)




#------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()	