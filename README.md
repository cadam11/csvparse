CSV Parse
---------

This is a little command line utility to let me quickly transform the raw output of downloaded transactions from the RBC website (in csv format) to a format that's more compatible with my budget spreadsheet in Numbers.

In particular, it does the following

 - reduces the transactions to just those that came from Chequing or MasterCard accounts
 - inverts the sign (+/-) for all transaction amounts such that cash outflows are positive
 - reduces the number of columns, eliminating excess data
 - parses the date string into an ISO date


Planned
-------

Maybe later I could make it filter based on the date value of transactions. Or maybe intelligently categorize expenses based on criteria.