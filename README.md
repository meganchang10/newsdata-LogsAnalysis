# newsdata-LogsAnalysis

I used the following command to load the provided database:
 
psql -d news -f newsdata.sql

The database included three tables:
1) authors
2) articles
3) log

In my code, I answer three questions:
1) What are the most popular three articles of all time?
2) Who are the most popular article authors of all time?
3) On which day did more than 1% of requests lead to errors?

This Python program runs from the command line without any input from the user. It connects to the database, creates a new SQL table to allow us to join the articles and log tables. Then uses SQL queries to analyze the data and print out answers. Each question is answered using a single SQL query in a single function. Python is used for minimal "post-processing" (specifically formatting the output and calculating a more accurate % failure rate.)
