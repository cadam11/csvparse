#!/usr/bin/python
import argparse
import csv
import dateutil.parser

default_category = 'Unbudgeted'


class Condition(object):
	def __init__(self, pattern, category=default_category):
		self.category = category
		self.pattern = pattern
	def test(self, row):
		return self.pattern.lower() in row["Description"].lower()

class AmountCondition(Condition):
	def __init__(self, amount, pattern, category=default_category):
		super(self.__class__, self).__init__(category)
		self.amount = amount
		self.pattern
	def test(self, row):
		return super(self.__class__, self).test(row) and float(row['Amount']) == float(self.amount)


#-----------------------------------------------------------------------------#


account_types = ['Chequing', 'MasterCard']
output_fields = ['Account', 'Date', 'Description', 'Category', 'Amount']

# First matched condition wins
conditions = [
	AmountCondition(60, 'www trf', 'Utilities'),
	AmountCondition(187, 'www trf', 'Home Insurance'),
	Condition('Moxie', 'Winesdays'),
	Condition('Sobeys', 'Groceries'),
	Condition('Extra Foods', 'Groceries'),
	Condition('Real cdn superstore', 'Groceries'),
	Condition('Costco', 'Groceries'),
	Condition('ATHABASCA UNIVERSITY', 'Education'),
	Condition('Winnipeg technical', 'Education'),
	Condition('Rogers', 'Mobile Phone'),
	Condition('misc payment', 'Hydro'),
	Condition('River park fd', 'Gas'),
	Condition('Loan interest', 'Finance Charge'),
	Condition('Transfer', 'Transfer'),
	Condition('Payment - thank you', 'Transfer'),
	Condition('Mortgage', 'Mortgage')
]

#-----------------------------------------------------------------------------#

def main():
	parser = argparse.ArgumentParser(description='Command line utility for parsing RBC transaction export csv files')
	parser.add_argument('inputfile', help='The name of the csv file to parse')
	parser.add_argument('-O', '--outputfile', default='out.csv', help='The filename for writing results, defaults to out.csv')
	parser.add_argument('-M', '--filtermonth', type=int, help='The month to limit transactions to')

	args = parser.parse_args()

	with open(args.inputfile) as infile, open(args.outputfile, 'w') as outfile:
		reader = csv.DictReader(infile)
		writer = csv.DictWriter(outfile, output_fields, quoting=csv.QUOTE_NONNUMERIC)
		writer.writeheader()

		for row in reader:
			newrow = parserow(row, args.filtermonth)
			if newrow:
				writer.writerow(newrow)

		infile.close()
		outfile.close()



#-----------------------------------------------------------------------------#

def parserow(row, filtermonth):
	if row['Account Type'] in account_types:
		amount = float(row['CAD$']) * -1
		rowdate = dateutil.parser.parse(row['Transaction Date'])
		newrow = {
			'Account': row['Account Type'],
			'Date': str(rowdate).split()[0],
			'Description': row['Description 1'].title(),
			'Category': '',
			'Amount': amount,
		}

		if filtermonth and not rowdate.month == filtermonth:
			return

		category = getcategory(newrow)
		if category:
			newrow['Category'] = category

		return newrow


def getcategory(row):
	for c in conditions:
		if c.test(row):
			return c.category





#-----------------------------------------------------------------------------#



if __name__ == "__main__":
    main()	