# Scrapy shell

The Scrapy shell is an interactive shell where you can try and debug your
scraping code very quickly, without having to run the spider. It’s meant to be
used for testing data extraction code, but you can actually use it for testing
any kind of code as it is also a regular Python shell.

The shell is used for testing XPath or CSS expressions and see how they work
and what data they extract from the web pages you’re trying to scrape. It
allows you to interactively test your expressions while you’re writing your
spider, without having to run the spider to test every change.

Once you get familiarized with the Scrapy shell, you’ll see that it’s an
invaluable tool for developing and debugging your spiders.

## Configuring the shell

If you have IPython [https://ipython.org/] installed, the Scrapy shell will use it (instead of the
standard Python console). The IPython [https://ipython.org/] console is much more powerful and
provides smart auto-completion and colorized output, among other things.

We highly recommend you install IPython [https://ipython.org/], especially if you’re working on
Unix systems (where IPython [https://ipython.org/] excels). See the IPython installation guide [https://ipython.org/install.html]
for more info.

Scrapy also has support for bpython [https://bpython-interpreter.org/], and will try to use it where IPython [https://ipython.org/]
is unavailable.

Through Scrapy’s settings you can configure it to use any one of
`ipython`, `bpython` or the standard `python` shell, regardless of which
are installed. This is done by setting the `SCRAPY_PYTHON_SHELL` environment
variable; or by defining it in your scrapy.cfg:

```
[settings]
shell = bpython

```