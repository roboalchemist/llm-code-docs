# Scrapy Tutorial

In this tutorial, we’ll assume that Scrapy is already installed on your system.
If that’s not the case, see Installation guide.

We are going to scrape quotes.toscrape.com [https://quotes.toscrape.com/], a website
that lists quotes from famous authors.

This tutorial will walk you through these tasks:

- 

Creating a new Scrapy project

- 

Writing a spider to crawl a site and extract data

- 

Exporting the scraped data using the command line

- 

Changing spider to recursively follow links

- 

Using spider arguments

Scrapy is written in Python [https://www.python.org/]. The more you learn about Python, the more you
can get out of Scrapy.

If you’re already familiar with other languages and want to learn Python quickly, the
Python Tutorial [https://docs.python.org/3/tutorial] is a good resource.

If you’re new to programming and want to start with Python, the following books
may be useful to you:

- 

Automate the Boring Stuff With Python [https://automatetheboringstuff.com/]

- 

How To Think Like a Computer Scientist [http://openbookproject.net/thinkcs/python/english3e/]

- 

Learn Python 3 The Hard Way [https://learnpythonthehardway.org/python3/]

You can also take a look at this list of Python resources for non-programmers [https://wiki.python.org/moin/BeginnersGuide/NonProgrammers],
as well as the suggested resources in the learnpython-subreddit [https://www.reddit.com/r/learnpython/wiki/index#wiki_new_to_python.3F].

## Creating a project

Before you start scraping, you will have to set up a new Scrapy project. Enter a
directory where you’d like to store your code and run:

```
scrapy startproject tutorial

```