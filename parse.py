#!/usr/bin/python
import argparse
import csv
import dateutil.parser

account_types = ['Chequing', 'MasterCard']
output_fields = ['Account', 'Date', 'Description', 'Category', 'Amount']

def main():
	parser = argparse.ArgumentParser(description='Command line utility for parsing RBC transaction export csv files')
	parser.add_argument('inputfile', help='The name of the csv file to parse')
	parser.add_argument('-O', '--outputfile', default='out.csv', help='The filename for writing results, defaults to out.csv')

	args = parser.parse_args()

	with open(args.inputfile) as infile, open(args.outputfile, 'w') as outfile:
		reader = csv.DictReader(infile)
		writer = csv.DictWriter(outfile, output_fields, quoting=csv.QUOTE_NONNUMERIC)
		writer.writeheader()

		for row in reader:
			newrow = parserow(row)
			if newrow:
				writer.writerow(newrow)

		infile.close()
		outfile.close()



#-----------------------------------------------------------------------------#

def parserow(row):
	if row['Account Type'] in account_types:
		amount = float(row['CAD$']) * -1
		newrow = {
			'Account': row['Account Type'],
			'Date': str(dateutil.parser.parse(row['Transaction Date'])).split()[0],
			'Description': row['Description 1'].title(),
			'Category': '',
			'Amount': amount,
		}
		return newrow




#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    main()	