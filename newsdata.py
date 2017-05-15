#!/usr/bin/env python3

import psycopg2

# Here we define the database we will be analyzing. NOTE: Even though the
# SQL file is actually called newsdata.sql, we unpackaged it in the command
# line using
#                    psql -d news -f newsdata.sql
#
# This resulted in the renaming of our file which is now referred to as news

DBNAME = "news"

# Connect to the database and create cursor

try:
    database = psycopg2.connect(database=DBNAME)
    c = database.cursor()
except:
    print("""Cannot make connection. Database not found. Make sure you have
          downloaded it through the zip file provided in the README.md file,
          and have opened it using the command `psql -d news -f newsdata.sql`
          executed from the command line inside a virtual machine.""")
# To write strings in multiple lines, we use the three quotation """x""" method
# which also allows our editor to pick up on the PSQL command words


# WHERE log.path LIKE '%' || articles.slug uses general expression to match
# patterns of strings to each other


def popular_articles(cursor):
    """Returns top three most viewed articles."""
    c.execute("""SELECT articles.title, count(*) AS views
        FROM articles, log
        WHERE log.path LIKE '%' || articles.slug
        GROUP BY articles.title
        ORDER BY views desc
        LIMIT 3;""")

    print("Most Popular Three Articles of All Time:")
    ans = c.fetchall()
    for a in ans:
        print (str(a[0].title()) + " - " + str(a[1]) + " views")
    print("")
    return ans


def popular_authors(cursor):
    """Counts views each author received on sum of all articles."""
    c.execute("""SELECT authors.name, count(*) AS views
    FROM articles, log, authors
    WHERE log.path LIKE '%' || articles.slug
    AND articles.author = authors.id
    GROUP BY authors.name
    ORDER BY views DESC;""")

    print("Most Popular Article Authors of All Time:")
    ans = c.fetchall()
    for a in ans:
        print (str(a[0].title()) + " - " + str(a[1]) + " views")
    print("")
    return ans


def dooms_day(cursor):
    """Returns day of most errors."""
    c.execute("""SELECT failed.date, failed.fail,
        (failed.fail + succeeded.success) AS total
    FROM (SELECT DATE(time), count(*) AS fail
    FROM log
    WHERE status != '200 OK'
    GROUP BY DATE(time)) AS failed,
    (SELECT DATE(time), count(*) AS success
    FROM log
    WHERE status = '200 OK'
    GROUP BY DATE(time)) AS succeeded
    WHERE failed.date = succeeded.date
    AND failed.fail*100 > (failed.fail + succeeded.success);""")

    print("Days That More Than 1 % of Requests Lead to Errors:")
    ans = c.fetchall()
    for a in ans:
        percentage = 100*a[1]/a[2]
        percentage = "{0:.3g}".format(percentage)
        print(str(a[0]) + ": " + str(percentage) + "% failure rate")
    print("")
    return ans

popular_articles(c)
popular_authors(c)
dooms_day(c)
database.close()
