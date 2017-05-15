# newsdata-LogsAnalysis

To run this program, the user needs to setup the news database.

1. Download the schema and data file here:
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
2. Create and setup the database with the command:
`psql -d news -f newsdata.sql`

The database should include three tables:
1. authors
2. articles
3. log

The *newsdata.py* program answers three questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which day did more than 1% of requests lead to errors?

This Python program runs from the command line without any input from the user. It connects to the database, creates a new SQL table to allow us to join the articles and log tables. Then uses SQL queries to analyze the data and print out answers. Each question is answered using a single SQL query in a single function. Python is used for minimal "post-processing" (specifically formatting the output and calculating a more accurate % failure rate.)

The program must be run from within a VM environment such as vagrant. To execute the program, type into the command line:
`python3 newsdata.py`

Also included is *output.txt* containing the output of the *newsdata.py* code.
